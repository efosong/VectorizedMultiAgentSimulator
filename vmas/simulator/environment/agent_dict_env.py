from vmas.simulator.environment.environment import Environment

class AgentDictVMASWrapper:
    # metadata
    metadata = Environment.metadata

    def __init__(self, env, agent_ids):
        self._env = env
        self.num_vec_envs = self._env.num_envs
        self.agent_ids = agent_ids
        # action space
        # observation space
        # joint space
        # num_vec_envs or vec_envs (this is called num_envs...)


    def reset(self):
        raw_observations = self._env.reset()
        observations = self._list_to_agent_dict(raw_observations)
        return observations

    def step(self, actions):
        action_list = self._agent_dict_to_list(actions)
        raw_observations, raw_rewards, raw_terminations, raw_truncations, raw_infos = \
                self._env.step(action_list)
        observations = self._list_to_agent_dict(raw_observations)
        rewards = self._list_to_agent_dict(raw_rewards)
        terminations = self._list_to_agent_dict(raw_terminations)
        truncations = self._list_to_agent_dict(raw_truncations)
        infos = self._list_to_agent_dict(raw_infos)
        
        return observations, rewards, terminations, truncations, infos

    def global_obs(self):
        return None

    @property
    def action_space(self):
        return self._env.action_space[0]

    @property
    def observation_space(self):
        return self._env.observation_space[0]

    def render(self, mode="human"):
        ...

    def _agent_dict_to_list(self, agent_dict):
        return [agent_dict[agent_id] for agent_id in self.agent_ids]

    def _list_to_agent_dict(self, data_list):
        return dict(zip(self.agent_ids, data_list))
