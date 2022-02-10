from math import log, sqrt
from project.classes.board import Board
from project.classes.state import State
from project.config import EXPLORATION_CONSTANT

class Node:
    
    def __init__(self, state: State, parent_node = None, child_nodes = []):
        self.state = state
        self.parent_node = parent_node
        self.child_nodes = child_nodes
    
    
    def node_is_terminal(self):
        return self.state.state_is_terminal()
    
    
    def add_child_nodes(self):
        if not self.node_is_terminal():
            _, available_board_positions = self.state.get_available_moves()
            for available_board_position in available_board_positions:
                self.child_nodes.append(
                    State(
                        Board(
                            board_positions = available_board_position
                            , player_to_act = self.state.board.opponent()
                        )
                    )
                )
    
    
    def calculate_ucb(self):
        exploitation_term = self.state.num_wins / (self.state.num_visits * 1.0) 
        exploration_term = sqrt(log(self.parent_state.num_visits) / (self.state.num_visits) * 1.0)
        return exploitation_term + EXPLORATION_CONSTANT * exploration_term
