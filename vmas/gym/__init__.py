import gym
from gym.envs.registration import register
import vmas
pitch_lengths = [2, 3]

class EPyMARLVMAS(gym.Env):
    def __init__(
        self,
        **kwargs
    ):
        super().__init__()
        self._env = vmas.make_env(
                scenario="football",
                num_envs=1,
                device="cpu",
                continuous_actions=False,
                wrapper=vmas.Wrapper.GYM,
                max_steps=1024,
                dict_spaces=False,
                **kwargs,
                )

        #self.observation_space = self._env.observation_space
        #self.action_space = self._env.action_space
        # need to convert to gym spaces.
        self.observation_space = gym.spaces.Tuple(tuple(
            gym.spaces.Box(space.low, space.high)
            for space in self._env.observation_space
        ))
        self.action_space = gym.spaces.Tuple(tuple(
            gym.spaces.Discrete(space.n)
            for space in self._env.action_space
        ))
        self.n_agents = len(self.action_space)

    def step(self, action):
        obs, rews, done, infos = self._env.step(action)
        dones = [done] * self.n_agents
        info = infos[0]
        return obs,rews,dones,info

    def reset(self):
        return self._env.reset()

for pitch_length in pitch_lengths:
    register(
        id=f"VMASFootball-{pitch_length}-v0",
        entry_point="vmas.gym:EPyMARLVMAS",
        max_episode_steps=1024,
        #autoreset=True,
        kwargs = {
            "obs_mode": "full",
            "dense_reward_ratio": 0,
            "pitch_length": pitch_length,
            "pitch_width": pitch_length/2,
            "ball_at_feet": True,
            "restrict_half": True,
            # Blue Team
            "n_blue_agents": 4,
            "max_n_blue_agents": 4,
            "blue_agent_names": ["LB", "RB", "LF", "RF"],
            "blue_pos": {
                #     x     y     l     w
                "LB": [-0.7,  0.2,  0.1,  0.5], # Left-Back
                "RB": [-0.7, -0.2,  0.1, -0.5], # Right-Back
                "LF": [-0.3,  0.2,  0.1,  0.3], # Left-Forward
                "RF": [-0.3, -0.2,  0.1, -0.3], # Right-Forward
                },
            # Red Team
            "n_red_agents": 4,
            "max_n_red_agents": 4,
            "red_agent_names": ["RedLB", "RedRB", "RedLF", "RedRF"],
            "red_pos": {
                #          x     y     l     w
                "RedLB": [-0.7,  0.2,  0.1,  0.5], # Left-Back
                "RedRB": [-0.7, -0.2,  0.1, -0.5], # Right-Back
                "RedLF": [-0.3,  0.2,  0.1,  0.3], # Left-Forward
                "RedRF": [-0.3, -0.2,  0.1, -0.3], # Right-Forward
                },
            "builtin_ai": {
                "start_vel_mag": 1.5,
                "dribble_speed": 0.75,
                "initial_vel_dist_behind_target_frac": 0.3,
                },
        },
    )
