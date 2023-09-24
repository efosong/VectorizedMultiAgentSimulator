#  Copyright (c) 2022-2023.
#  ProrokLab (https://www.proroklab.org/)
#  All rights reserved.

from vmas.interactive_rendering import render_interactively
from vmas.make_env import make_env
from vmas.simulator.environment import Wrapper

from vmas.simulator.utils import _init_pyglet_device

_init_pyglet_device()

__all__ = [
    "make_env",
    "render_interactively",
    "Wrapper",
    "scenarios",
    "debug_scenarios",
    "mpe_scenarios",
]

scenarios = sorted(
    [
        "dropout",
        "dispersion",
        "transport",
        "reverse_transport",
        "give_way",
        "wheel",
        "balance",
        "football",
        "discovery",
        "flocking",
        "passage",
        "joint_passage_size",
        "joint_passage",
        "ball_passage",
        "ball_trajectory",
        "buzz_wire",
        "multi_give_way",
        "navigation",
        "sampling",
        "wind_flocking",
    ]
)

debug_scenarios = sorted(
    [
        "asym_joint",
        "circle_trajectory",
        "goal",
        "het_mass",
        "line_trajectory",
        "vel_control",
        "waterfall",
        "diff_drive",
    ]
)

mpe_scenarios = sorted(
    [
        "simple",
        "simple_adversary",
        "simple_crypto",
        "simple_push",
        "simple_reference",
        "simple_speaker_listener",
        "simple_spread",
        "simple_tag",
        "simple_world_comm",
    ]
)


# # register football gym
# from gym.envs.registration import register
# pitch_lengths = [2, 3]
# 
# for pitch_length in pitch_lengths:
#     register(
#         id=f"VMASFootball-{pitch_length}-v0",
#         entry_point="vmas.simulator:EPyMARLVMAS", # TODO
#         max_episode_steps=1024,
#         #autoreset=True,
#         kwargs = {
#             "obs_mode": "full",
#             "dense_reward_ratio": 0,
#             "pitch_length": pitch_length,
#             "pitch_width": pitch_length/2,
#             "ball_at_feet": True,
#             "restrict_half": True,
#             # Blue Team
#             "n_blue_agents": 4,
#             "max_n_blue_agents": 4,
#             "blue_agent_names": ["LB", "RB", "LF", "RF"],
#             "blue_pos": {
#                 #     x     y     l     w
#                 "LB": [-0.7,  0.2,  0.1,  0.5], # Left-Back
#                 "RB": [-0.7, -0.2,  0.1, -0.5], # Right-Back
#                 "LF": [-0.3,  0.2,  0.1,  0.3], # Left-Forward
#                 "RF": [-0.3, -0.2,  0.1, -0.3], # Right-Forward
#                 },
#             # Red Team
#             "n_red_agents": 4,
#             "max_n_red_agents": 4,
#             "red_agent_names": ["RedLB", "RedRB", "RedLF", "RedRF"],
#             "red_pos": {
#                 #          x     y     l     w
#                 "RedLB": [-0.7,  0.2,  0.1,  0.5], # Left-Back
#                 "RedRB": [-0.7, -0.2,  0.1, -0.5], # Right-Back
#                 "RedLF": [-0.3,  0.2,  0.1,  0.3], # Left-Forward
#                 "RedRF": [-0.3, -0.2,  0.1, -0.3], # Right-Forward
#                 },
#             "builtin_ai": {
#                 "start_vel_mag": 1.5,
#                 "dribble_speed": 0.75,
#                 "initial_vel_dist_behind_target_frac": 0.3,
#                 },
#         },
#     )
