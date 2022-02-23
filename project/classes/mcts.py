import random
from copy import deepcopy
import numpy as np
import time

from project.config import (
    MCTS_DECISION_TIME
    , MIN_MCTS_SIMULATIONS
    , ONGOING_GAME_STATUS
    , DRAW_STATUS
    , OPPONENT
    , PLAYERS
    , BOARD_VALUE
    , WIN_STATUS
)
from project.classes.board import Board
from project.classes.state import State
from project.classes.node import Node


class Mcts:
    
    def __init__(self, root_node: Node, mcts_decision_time: int = MCTS_DECISION_TIME, min_mcts_simulations = MIN_MCTS_SIMULATIONS):
        self.root_node = root_node
        self.mcts_decision_time = mcts_decision_time
        self.min_mcts_simulations = min_mcts_simulations
    
    
    def select_best_move(self):
        
        original_player_to_act = self.root_node.player_to_act()
        
        simulation_num = 1
        start_time = time.time()
        current_time = time.time()
        
        while ((current_time - start_time) < self.mcts_decision_time) or (simulation_num <= self.min_mcts_simulations):
            selected_node: Node = self.selection()
            expanded_node: Node = self.expansion(selected_node)
            simulation_result_status = self.simulation(expanded_node, original_player_to_act)
            self.back_propogation(expanded_node, simulation_result_status, original_player_to_act)
            
            simulation_num += 1
            current_time = time.time()
        
        best_child = self.select_best_child()
        for c in self.root_node.child_nodes:
            print(c.state.board, c.state.num_wins, c.state.num_visits, c.calculate_ucb())
        move = self.convert_best_child_to_move(best_child)
        return move
    
    
    def selection(self):
        
        selected_node = self.root_node
        while selected_node.child_nodes != []:
            child_nodes = selected_node.child_nodes
            max_ucb_node = max(child_nodes, key= lambda x: x.calculate_ucb())
            max_ucb_nodes = [child_node for child_node in child_nodes if child_node.calculate_ucb() == max_ucb_node.calculate_ucb()]
            selected_node = random.choice(max_ucb_nodes)
        
        return selected_node
    
    
    def expansion(self, selected_node: Node):
        
        if not selected_node.node_is_terminal():
            available_board_positions = selected_node.get_available_board_positions()
            for available_board_position in available_board_positions:
                selected_node.child_nodes.append(
                    Node(
                        state = State(
                            Board(
                                rows = selected_node.state.board.rows
                                , columns = selected_node.state.board.columns
                                , num_consecutive_for_win = selected_node.state.board.num_consecutive_for_win
                                , board_positions = available_board_position
                                , player_to_act = selected_node.opponent()
                                , win_combos = selected_node.state.board.win_combos
                            )
                            , num_wins = 0
                            , num_visits = 0
                        )
                        , parent_node = selected_node
                        , child_nodes = []
                    )
                )
            
            return random.choice(selected_node.child_nodes)
        
        else:
            return selected_node
    
    
    def simulation(self, expanded_node: Node, original_player_to_act):
        
        original_opponent = PLAYERS[original_player_to_act][OPPONENT]
        
        if expanded_node.parent_node is not None:
            # Should always be this case
            pn = expanded_node.parent_node
        else:
            pn = None
        
        temp_node = Node(expanded_node.state, parent_node = pn, child_nodes = expanded_node.child_nodes)
        # If expanded node is a win for the opponent, provide the lowest possible reward value, so the node is never searched again
        if temp_node.state.board.check_game_status() == PLAYERS[original_opponent][WIN_STATUS]:
            temp_node.parent_node.state.num_wins = float('-inf')
            return PLAYERS[original_opponent][WIN_STATUS]
        
        # simulate game
        temp_board = deepcopy(expanded_node.state.board)
        while temp_board.check_game_status() == ONGOING_GAME_STATUS:
            available_moves = temp_board.get_valid_moves()
            if len(available_moves) > 1:
                selected_move = random.choice(available_moves)
            
            elif len(available_moves) == 1:
                selected_move = available_moves[0]
            
            selected_row_indx = str(selected_move[0])
            selected_column_indx = str(selected_move[1])
            selected_move_str = f'{selected_row_indx},{selected_column_indx}'
            
            temp_board.play_move(selected_move_str)
            temp_board.player_to_act = temp_board.opponent()
        
        # update statistics
        expanded_node.state.num_visits += 1
        
        simulation_result_status = temp_board.check_game_status()
        if simulation_result_status == DRAW_STATUS:
            expanded_node.state.num_wins += 0.5
        elif simulation_result_status == PLAYERS[original_player_to_act][BOARD_VALUE]:
            expanded_node.state.num_wins += 1
        elif simulation_result_status == PLAYERS[original_opponent][BOARD_VALUE]:
            expanded_node.state.num_wins -= 1
                
        return simulation_result_status
    
    
    def back_propogation(self, expanded_node: Node, simulation_result_status, original_player_to_act):
        
        current_node: Node = expanded_node
        original_opponent = PLAYERS[original_player_to_act][OPPONENT]
        
        while current_node.parent_node is not None:
            current_node.parent_node.state.num_visits += 1
            
            if simulation_result_status == DRAW_STATUS:
                current_node.parent_node.state.num_wins += 0.5
            elif simulation_result_status == PLAYERS[original_player_to_act][BOARD_VALUE]:
                current_node.parent_node.state.num_wins += 1
            elif simulation_result_status == PLAYERS[original_opponent][BOARD_VALUE]:
                current_node.parent_node.state.num_wins -= 1
            
            current_node = current_node.parent_node
    

    def select_best_child(self):
        max_visits_node = max(self.root_node.child_nodes, key= lambda x: x.state.num_visits)
        max_visits_nodes = [child_node for child_node in self.root_node.child_nodes if child_node.state.num_visits == max_visits_node.state.num_visits]
        selected_child_node = random.choice(max_visits_nodes)
        return selected_child_node
    

    def convert_best_child_to_move(self, selected_child_node: Node):

        root_node_board_positions = self.root_node.state.board.board_positions
        selected_child_node_board_positions = selected_child_node.state.board.board_positions
        move_tuple = list(zip(*[x.tolist() for x in np.where(root_node_board_positions != selected_child_node_board_positions)]))
        move_row_indx = move_tuple[0][0]
        move_column_indx = move_tuple[0][1]
        move = f'{move_row_indx},{move_column_indx}'

        return move

