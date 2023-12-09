import argparse

from snake.game import Game, GameConf, GameMode

dict_solver = {
    "greedy": "GreedySolver",  # greedy solver
    "hamilton": "HamiltonSolver",  # hamilton solver
    "dqn": "DQNSolver",  # deep Q-network solver
}

dict_mode = {
    "play": GameMode.NORMAL,  # normal mode: play game with choosen solver
    "bcmk": GameMode.BENCHMARK,  # benchmark mode: evaluate the results of choosen solver
    "train_dqn": GameMode.TRAIN_DQN,  # training deep Q-network without GUI
    "train_dqn_gui": GameMode.TRAIN_DQN_GUI,  # training deep Q-network with GUI
}

dict_map_mode = {
    "0": 0,  # normal map mode: no walls
    "1": 1,  # map mode 1: 4 walls are located near 4 corners
    "2": 2,  # map mode 2: 8 walls form 2 parallel lines
    "3": 3,  # map mode 3: 8 random walls
}

dict_map_size = {
    "8": 8,  # normal size: 8x8
    "12": 12,  # map size: 12x12
    "24": 24,  # map size: 24x24
}

parser = argparse.ArgumentParser(description="Run snake game agent.")
parser.add_argument(
    "-s",
    default="hamilton",
    choices=dict_solver.keys(),
    help="name of the solver to direct the snake (default: hamilton)",
)
parser.add_argument(
    "-m", default="play", choices=dict_mode.keys(), help="game mode (default: normal)"
)
parser.add_argument(
    "-w",
    default="0",
    choices=dict_map_mode.keys(),
    help="walls mode (default: normal)",
)
parser.add_argument(
    "-p",
    default="8",
    choices=dict_map_size.keys(),
    help="proportion of map (default: normal)",
)
args = parser.parse_args()

conf = GameConf()
conf.solver_name = dict_solver[args.s]
conf.mode = dict_mode[args.m]
conf.map_rows = dict_map_size[args.p]
conf.map_cols = conf.map_rows
conf.map_mode = dict_map_mode[args.w]
print(
    "Solver: %s    Mode: %s   Map: %s   Map_size: %s"
    % (conf.solver_name, conf.mode, args.w, args.p)
)

Game(conf).run()
