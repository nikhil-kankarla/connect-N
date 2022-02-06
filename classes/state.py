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
        self.game_status = self.get_game_positions()


    def get_game_status(self, win_combos):
        
        player_1_positions = list(zip(*[x.tolist() for x in np.where(self.board.board_positions == PLAYERS[PLAYER_1][BOARD_VALUE])]))
        player_2_positions = list(zip(*[x.tolist() for x in np.where(self.board.board_positions == PLAYERS[PLAYER_2][BOARD_VALUE])]))

        for win_combo in win_combos:
            if set(win_combo).issubset(player_1_positions):
                return PLAYER_1_WIN_STATUS
            elif set(win_combo).issubset(player_2_positions):
                return PLAYER_2_WIN_STATUS
        
        if len(np.where(self.board.board_positions == 0)[0]) > 0: # If there are any unselected positions, the game is yet to finish
            return ONGOING_GAME_STATUS
        else: # If there are no unselected positions, and neither player has won, the game is a draw
            return DRAW_STATUS
