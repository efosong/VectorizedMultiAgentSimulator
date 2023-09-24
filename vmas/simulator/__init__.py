#  Copyright (c) 2022.
#  ProrokLab (https://www.proroklab.org/)
#  All rights reserved.
# import gym
# import vmas
# 
# class EPyMARLVMAS(gym.Env):
#     def __init__(
#         self,
#         **kwargs
#     ):
#         super().__init__()
#         self._env = vmas.make_env(
#                 scenario="football",
#                 num_envs=1,
#                 device="cpu",
#                 continuous_actions=False,
#                 wrapper=vmas.Wrapper.GYM,
#                 max_steps=1024,
#                 dict_spaces=False,
#                 **kwargs,
#                 )
# 
#         #self.observation_space = self._env.observation_space
#         #self.action_space = self._env.action_space
#         # need to convert to gym spaces.
#         self.observation_space = gym.spaces.Tuple(tuple(
#             gym.spaces.Box(space.low, space.high)
#             for space in self._env.observation_space
#         ))
#         self.action_space = gym.spaces.Tuple(tuple(
#             gym.spaces.Discrete(space.n)
#             for space in self._env.action_space
#         ))
#         self.n_agents = len(self.action_space)
# 
#     def step(self, action):
#         obs, rews, done, infos = self._env.step(action)
#         dones = [done] * self.n_agents
#         info = infos[0]
#         print("x")
#         return obs,rews,dones,info
# 
#     def reset(self):
#         return self._env.reset()
