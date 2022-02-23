from math import log, sqrt
from project.classes.board import Board
from project.classes.state import State
from project.config import EXPLORATION_CONSTANT

class Node:
    
    def __init__(self, state: State, parent_node = None, child_nodes = []):
        self.state = state
        self.parent_node = parent_node
        self.child_nodes = child_nodes
    
    
    def player_to_act(self):
        return self.state.player_to_act()
    
    
    def opponent(self):
        return self.state.opponent()
    
    
    def board_positions(self):
        return self.state.board_positions()
    
    
    def node_is_terminal(self):
        return self.state.state_is_terminal()
    

    def get_available_board_positions(self):
        return self.state.get_available_board_positions()
    
    
    def add_child_nodes(self):
        if not self.node_is_terminal():
            available_board_positions = self.get_available_board_positions()
            child_nodes = []
            for available_board_position in available_board_positions:
                child_nodes.append(
                    Node(
                        state = State(
                            Board(
                                rows = self.state.board.rows
                                , columns = self.state.board.columns
                                , num_consecutive_for_win = self.state.board.num_consecutive_for_win
                                , board_positions = available_board_position
                                , player_to_act = self.opponent()
                                , win_combos = self.state.board.win_combos
                            )
                            , num_wins = 0
                            , num_visits = 0
                        )
                        , parent_node = self
                        , child_nodes = []
                    )
                )
            self.child_nodes = child_nodes
    
    
    def calculate_ucb(self):
        if self.state.num_visits == 0:
            ucb = float('inf') # try to ensure each child is explored at least once
        else:
            if self.parent_node is not None:
                exploitation_term = self.state.num_wins / (self.state.num_visits * 1.0) 
                exploration_term = sqrt(log(self.parent_node.state.num_visits) / (self.state.num_visits) * 1.0)
                ucb = exploitation_term + EXPLORATION_CONSTANT * exploration_term
            else:
                ucb = 0
        return ucb
    
    
    def get_node_str(self):
        
        state_str = self.state.__str__()
        
        if self.parent_node: 
            parent_node_board_positions = self.parent_node.state.board.get_board_string()
            parent_node_num_visits = self.parent_node.state.num_visits
        else:
            parent_node_board_positions = 'None'
            parent_node_num_visits = 0

        if self.child_nodes != []: 
            child_nodes_board_positions = []
            for cn in self.child_nodes:
                child_nodes_board_positions.append(cn.board_positions())
        else: child_nodes_board_positions = []
        
        node_str = (
            state_str + '\n' +
            f'UCB: {self.calculate_ucb()}\n' +
            f"Parent board: \n{parent_node_board_positions}\n" +
            f"Number of visits to parent board: {parent_node_num_visits}\n"
            f"Child nodes' board positions: \n{child_nodes_board_positions}\n"
        )
    
        return node_str
    
    
    def __repr__(self):
        return self.get_node_str()
    
    
    def __str__(self):
        return self.get_node_str()
