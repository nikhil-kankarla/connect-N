import numpy as np

from copy import deepcopy
from project.config import PLAYER_1_WIN_STATUS, PLAYER_2, PLAYER_2_WIN_STATUS, PLAYERS, BOARD_VALUE
from project.classes.board import Board


class State:
    
    def __init__(self, board: Board, num_wins = 0, num_visits = 0):
        self.board = board
        self.num_wins = num_wins
        self.num_visits = num_visits
    

    def player_to_act(self):
        return self.board.player_to_act
    
    
    def opponent(self):
        return self.board.opponent()
    
    
    def board_positions(self):
        return self.board.board_positions
    
    
    def get_available_moves(self):
        return self.board.get_valid_moves()
    
    
    def get_available_board_positions(self):
        
        available_moves = self.get_available_moves()
        available_board_positions = []
        for available_move in available_moves:
            new_board_positions = deepcopy(self.board.board_positions)
            row_index = available_move[0]
            column_index = available_move[1]
            new_board_positions[row_index, column_index] = PLAYERS[self.board.player_to_act][BOARD_VALUE]
            available_board_positions.append(new_board_positions)
    
        return available_board_positions
    
    
    def state_is_terminal(self):
        if self.board.check_game_status() in [PLAYER_1_WIN_STATUS, PLAYER_2_WIN_STATUS]:
            return True
        else:
            available_moves = self.board.get_valid_moves()
            return len(available_moves) == 0
    

    def get_state_str(self):
    
        board_str = self.board.__str__()
        if self.num_visits == 0: win_ratio = 0
        else: win_ratio = (self.num_wins * 1.0 / self.num_visits)

        state_str = (
            board_str + '\n' +
            f'Number of wins: {self.num_wins}\n' +
            f'Number of visits: {self.num_visits}\n' +
            f'Win ratio: {win_ratio}'
        )
        
        return state_str
    
    
    def __repr__(self):
        return self.get_state_str()
    

    def __str__(self):
        return self.get_state_str()
