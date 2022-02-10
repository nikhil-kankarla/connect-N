import numpy as np

from copy import deepcopy
from project.classes.board import Board


class State:
    
    def __init__(self, board: Board, num_wins = 0, num_visits = 0):
        self.board = board
        self.player_to_act = self.board.player_to_act
        self.num_wins = num_wins
        self.num_visits = num_visits
    
    
    def get_available_moves(self):
        return self.board.get_valid_moves()
    
    
    def get_available_board_positions(self):
        
        available_moves = self.get_available_moves()
        available_board_positions = []
        for available_move in available_moves:
            new_board_positions = deepcopy(self.board.board_positions)
            row_index = available_move[0]
            column_index = available_move[1]
            new_board_positions[row_index, column_index] = 1
    
        return available_board_positions
    
    
    def state_is_terminal(self):
        available_moves = self.board.get_valid_moves()
        return len(available_moves) == 0
