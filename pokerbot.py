from pypokerengine.api.game import setup_config, start_poker

from pathlib import Path
# import os
# import sys
# print('getcwd:      ', os.getcwd())

# sys.path.append(str(os.getcwd()))
# print(sys.path)
from fish_player import FishPlayer
from consoleplayer import ConsolePlayer
from random_player import RandomPlayer
from honest_player import HonestPlayer
from chen_player import ChenPlayer

config = setup_config(max_round=100, initial_stack=1000, small_blind_amount=20)
config.register_player(name="f1", algorithm=FishPlayer())
config.register_player(name="f2", algorithm=FishPlayer())
config.register_player(name="f3", algorithm=FishPlayer())
config.register_player(name="f4", algorithm=FishPlayer())
config.register_player(name="f5", algorithm=RandomPlayer())
config.register_player(name="r1", algorithm=RandomPlayer())
config.register_player(name="r2", algorithm=RandomPlayer())
config.register_player(name="r3", algorithm=RandomPlayer())
config.register_player(name="ch", algorithm=ChenPlayer())
config.register_player(name="H", algorithm=HonestPlayer())
game_result = start_poker(config, verbose=1)