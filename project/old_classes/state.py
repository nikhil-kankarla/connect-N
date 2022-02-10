import numpy as np

from classes.board import Board
from config import (
    BOARD_VALUE
    , PLAYERS
    , PLAYER_1
    , PLAYER_2
    , PLAYER_1_WIN_STATUS
    , PLAYER_2_WIN_STATUS
    , ONGOING_GAME_STATUS
    , DRAW_STATUS
)

class State:
    
    def __init__(self, board: Board, player_to_act):
        self.board = board
        self.player_to_act = player_to_act
