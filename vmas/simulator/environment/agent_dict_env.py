from vmas.simulator.environment.environment import Environment

class AgentDictVMASWrapper:
    # metadata
    metadata = Environment.metadata

    def __init__(self, env):
        self._env = env
        self.num_vec_envs = self._env.num_envs
        self.agent_ids = [agent.name for agent in self._env.agents]

    def reset(self):
        return self._env.reset()

    def step(self, actions):
        observations, rewards, terminated, truncated, infos = \
                self._env.step(actions)
        terminations = {agent_id: terminated
                        for agent_id in self.agent_ids}
        truncations = {agent_id: truncated
                       for agent_id in self.agent_ids}
        # Reset done environments
        dones = (terminated | truncated)
        for env_idx, done in enumerate(dones):
            if done:
                reset_obs = self._env.reset_at(env_idx)
                for agent_id, agent_obs in reset_obs.items():
                    observations[agent_id] = agent_obs
        return observations, rewards, terminations, truncations, infos

    def global_obs(self):
        return None

    @property
    def action_space(self):
        return next(iter(self._env.action_space.values()))

    @property
    def observation_space(self):
        return next(iter(self._env.observation_space.values()))

    def render(self, mode="human"):
        ...
