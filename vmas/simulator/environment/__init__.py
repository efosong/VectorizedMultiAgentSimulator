#  Copyright (c) 2022.
#  ProrokLab (https://www.proroklab.org/)
#  All rights reserved.
from enum import Enum

from vmas.simulator.environment.environment import Environment


class Wrapper(Enum):
    RLLIB = 0
    GYM = 1
    ADE = 2

    def get_env(self, env: Environment, **kwargs):
        if self is self.RLLIB:
            from vmas.simulator.environment.rllib import VectorEnvWrapper
            return VectorEnvWrapper(env)

        elif self is self.GYM:
            from vmas.simulator.environment.gym import GymWrapper
            return GymWrapper(env)

        elif self is self.ADE:
            from vmas.simulator.environment.agent_dict_env import AgentDictVMASWrapper
            return AgentDictVMASWrapper(env)
