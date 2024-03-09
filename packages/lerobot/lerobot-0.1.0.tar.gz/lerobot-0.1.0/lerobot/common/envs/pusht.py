import importlib
from collections import deque
from typing import Optional

import einops
import torch
from tensordict import TensorDict
from torchrl.data.tensor_specs import (
    BoundedTensorSpec,
    CompositeSpec,
    DiscreteTensorSpec,
    UnboundedContinuousTensorSpec,
)
from torchrl.envs import EnvBase
from torchrl.envs.libs.gym import _gym_to_torchrl_spec_transform

from lerobot.common.utils import set_seed

_has_gym = importlib.util.find_spec("gym") is not None
_has_diffpolicy = importlib.util.find_spec("diffusion_policy") is not None and _has_gym


class PushtEnv(EnvBase):
    def __init__(
        self,
        frame_skip: int = 1,
        from_pixels: bool = False,
        pixels_only: bool = False,
        image_size=None,
        seed=1337,
        device="cpu",
        num_prev_obs=0,
        num_prev_action=0,
    ):
        super().__init__(device=device, batch_size=[])
        self.frame_skip = frame_skip
        self.from_pixels = from_pixels
        self.pixels_only = pixels_only
        self.image_size = image_size
        self.num_prev_obs = num_prev_obs
        self.num_prev_action = num_prev_action

        if pixels_only:
            assert from_pixels
        if from_pixels:
            assert image_size

        if not _has_diffpolicy:
            raise ImportError("Cannot import diffusion_policy.")
        if not _has_gym:
            raise ImportError("Cannot import gym.")

        # TODO(rcadene) (PushTEnv is similar to PushTImageEnv, but without the image rendering, it's faster to iterate on)
        # from diffusion_policy.env.pusht.pusht_env import PushTEnv

        if not from_pixels:
            raise NotImplementedError("Use PushTEnv, instead of PushTImageEnv")
        from diffusion_policy.env.pusht.pusht_image_env import PushTImageEnv

        self._env = PushTImageEnv(render_size=self.image_size)

        self._make_spec()
        self._current_seed = self.set_seed(seed)

        if self.num_prev_obs > 0:
            self._prev_obs_image_queue = deque(maxlen=self.num_prev_obs)
            self._prev_obs_state_queue = deque(maxlen=self.num_prev_obs)
        if self.num_prev_action > 0:
            raise NotImplementedError()
            # self._prev_action_queue = deque(maxlen=self.num_prev_action)

    def render(self, mode="rgb_array", width=384, height=384):
        if width != height:
            raise NotImplementedError()
        tmp = self._env.render_size
        self._env.render_size = width
        out = self._env.render(mode)
        self._env.render_size = tmp
        return out

    def _format_raw_obs(self, raw_obs):
        if self.from_pixels:
            image = torch.from_numpy(raw_obs["image"])
            obs = {"image": image}

            if not self.pixels_only:
                obs["state"] = torch.from_numpy(raw_obs["agent_pos"]).type(torch.float32)
        else:
            # TODO:
            obs = {"state": torch.from_numpy(raw_obs["observation"]).type(torch.float32)}

        return obs

    def _reset(self, tensordict: Optional[TensorDict] = None):
        td = tensordict
        if td is None or td.is_empty():
            # we need to handle seed iteration, since self._env.reset() rely an internal _seed.
            self._current_seed += 1
            self.set_seed(self._current_seed)
            raw_obs = self._env.reset()
            assert self._current_seed == self._env._seed

            obs = self._format_raw_obs(raw_obs)

            if self.num_prev_obs > 0:
                stacked_obs = {}
                if "image" in obs:
                    self._prev_obs_image_queue = deque(
                        [obs["image"]] * (self.num_prev_obs + 1), maxlen=(self.num_prev_obs + 1)
                    )
                    stacked_obs["image"] = torch.stack(list(self._prev_obs_image_queue))
                if "state" in obs:
                    self._prev_obs_state_queue = deque(
                        [obs["state"]] * (self.num_prev_obs + 1), maxlen=(self.num_prev_obs + 1)
                    )
                    stacked_obs["state"] = torch.stack(list(self._prev_obs_state_queue))
                obs = stacked_obs

            td = TensorDict(
                {
                    "observation": TensorDict(obs, batch_size=[]),
                    "done": torch.tensor([False], dtype=torch.bool),
                },
                batch_size=[],
            )
        else:
            raise NotImplementedError()
        return td

    def _step(self, tensordict: TensorDict):
        td = tensordict
        action = td["action"].numpy()
        # step expects shape=(4,) so we pad if necessary
        # TODO(rcadene): add info["is_success"] and info["success"] ?
        sum_reward = 0

        if action.ndim == 1:
            action = einops.repeat(action, "c -> t c", t=self.frame_skip)
        else:
            if self.frame_skip > 1:
                raise NotImplementedError()

        num_action_steps = action.shape[0]
        for i in range(num_action_steps):
            raw_obs, reward, done, info = self._env.step(action[i])
            sum_reward += reward

            obs = self._format_raw_obs(raw_obs)

            if self.num_prev_obs > 0:
                stacked_obs = {}
                if "image" in obs:
                    self._prev_obs_image_queue.append(obs["image"])
                    stacked_obs["image"] = torch.stack(list(self._prev_obs_image_queue))
                if "state" in obs:
                    self._prev_obs_state_queue.append(obs["state"])
                    stacked_obs["state"] = torch.stack(list(self._prev_obs_state_queue))
                obs = stacked_obs

        td = TensorDict(
            {
                "observation": TensorDict(obs, batch_size=[]),
                "reward": torch.tensor([sum_reward], dtype=torch.float32),
                # succes and done are true when coverage > self.success_threshold in env
                "done": torch.tensor([done], dtype=torch.bool),
                "success": torch.tensor([done], dtype=torch.bool),
            },
            batch_size=[],
        )
        return td

    def _make_spec(self):
        obs = {}
        if self.from_pixels:
            image_shape = (3, self.image_size, self.image_size)
            if self.num_prev_obs > 0:
                image_shape = (self.num_prev_obs + 1, *image_shape)

            obs["image"] = BoundedTensorSpec(
                low=0,
                high=1,
                shape=image_shape,
                dtype=torch.float32,
                device=self.device,
            )
            if not self.pixels_only:
                state_shape = self._env.observation_space["agent_pos"].shape
                if self.num_prev_obs > 0:
                    state_shape = (self.num_prev_obs + 1, *state_shape)

                obs["state"] = BoundedTensorSpec(
                    low=0,
                    high=512,
                    shape=state_shape,
                    dtype=torch.float32,
                    device=self.device,
                )
        else:
            # TODO(rcadene): add observation_space achieved_goal and desired_goal?
            state_shape = self._env.observation_space["observation"].shape
            if self.num_prev_obs > 0:
                state_shape = (self.num_prev_obs + 1, *state_shape)

            obs["state"] = UnboundedContinuousTensorSpec(
                # TODO:
                shape=state_shape,
                dtype=torch.float32,
                device=self.device,
            )
        self.observation_spec = CompositeSpec({"observation": obs})

        self.action_spec = _gym_to_torchrl_spec_transform(
            self._env.action_space,
            device=self.device,
        )

        self.reward_spec = UnboundedContinuousTensorSpec(
            shape=(1,),
            dtype=torch.float32,
            device=self.device,
        )

        self.done_spec = CompositeSpec(
            {
                "done": DiscreteTensorSpec(
                    2,
                    shape=(1,),
                    dtype=torch.bool,
                    device=self.device,
                ),
                "success": DiscreteTensorSpec(
                    2,
                    shape=(1,),
                    dtype=torch.bool,
                    device=self.device,
                ),
            }
        )

    def _set_seed(self, seed: Optional[int]):
        set_seed(seed)
        self._env.seed(seed)
