from copy import deepcopy
from math import log, sqrt
import random
import numpy as np
from config import (
    EXPLORATION_CONSTANT,
    ROWS
    , COLUMNS
    , NUM_CONSECUTIVE_FOR_WIN
    , PLAYER_1
    , PLAYER_2
    , PLAYER_NUM
    , BOARD_VALUE
    , BOARD_STR
    , PLAYERS
    , WIN_COMBOS
    , DRAW_STATUS
    , ONGOING_GAME_STATUS
    , PLAYER_1_WIN_STATUS
    , PLAYER_2_WIN_STATUS
    , OPPONENT
)

class Board:

    def __init__(
        self
        , rows = ROWS
        , columns = COLUMNS
        , num_consecutive_for_win = NUM_CONSECUTIVE_FOR_WIN
        , board_positions = None
        , player_to_act = None
        , win_combos = WIN_COMBOS
    ):
        self.rows = rows
        self.columns = columns
        self.board_shape = [self.rows, self.columns]
        self.num_consecutive_for_win = num_consecutive_for_win
        if board_positions is None:
            board_positions = np.array([[0] * self.columns] * self.rows)
        self.board_positions = board_positions
        self.player_to_act = player_to_act
        self.win_combos = win_combos
        
    
    
    def opponent(self):
        return PLAYERS[self.player_to_act][OPPONENT]
    
    
    def new_game_bool(self):
        return len(np.where(self.board_positions == 0)[0]) == (self.rows * self.columns)
    
    
    def new_game_message(self, games):
        
        print('Starting new game')
        if len(games.keys()) == 0: game_num = 1
        else: game_num = max(games.keys()) + 1
        print(f'Game number: {game_num}')
        print(f'Player to act: {self.player_to_act} ({PLAYERS[self.player_to_act][BOARD_STR]}) \n')

        return game_num
    

    def print_match_outcome(self, games):
        print('')
        print('Ending match')
        print(f'Player 1 won: {len([result for result in games.values() if result == PLAYER_1_WIN_STATUS])} games')
        print(f'Player 2 won: {len([result for result in games.values() if result == PLAYER_2_WIN_STATUS])} games')
        print(f'Draws: {len([result for result in games.values() if result == DRAW_STATUS])} games\n')
    
    
    def check_input_is_valid_format(self, move_input: str):
        
        move_row_indx, move_column_indx = None, None
        
        move_input_despaced = move_input.replace(' ', '')
        move_input_is_comma_delimited = ',' in move_input_despaced
        if move_input_is_comma_delimited:
            if move_input_despaced.count(',') == 1:
                move_indices = move_input_despaced.split(',')
                
                try:
                    move_row_indx = int(move_indices[0])
                    if move_row_indx >= self.rows:
                        print(f'Invalid input: Row index of {move_row_indx} exceeds number of rows')
                except ValueError:
                    print('Invalid input: Please ensure the row index is numeric')
                
                try:
                    move_column_indx = int(move_indices[1])
                    if move_column_indx >= self.columns:
                        print(f'Invalid input: Column index of {move_column_indx} exceeds number of columns')
                except ValueError:
                    print('Invalid input: Please ensure the column index is numeric')
            
            else:
                print('Invalid input: Please ensure there is only ONE comma in the input')
                print('---The input should be of the form "X,Y", where X is the row index and Y is the column index')
        
        else:
            print('Invalid input: Please ensure the row index and column index are separated by a comma')
        
        return (move_row_indx is not None) and (move_column_indx is not None)


    def get_valid_moves(self):
        return list(zip(*[x.tolist() for x in np.where(self.board_positions == 0)]))


    def convert_move_input_to_position(self, move: str):
        move_indices = move.split(',')
        move_row_indx = int(move_indices[0])
        move_column_indx = int(move_indices[1])
        return move_row_indx, move_column_indx


    def check_move_is_valid(self, move):
        move_row_indx, move_column_indx = self.convert_move_input_to_position(move)
        if (move_row_indx, move_column_indx) in self.get_valid_moves():
            return True
        else:
            print(f'{move_row_indx},{move_column_indx} is an invalid move. Please select a valid move')
            print(f'Valid moves are: {self.get_valid_moves()}')
            return False


    def play_move(self, move):
        move_row_indx, move_column_indx = self.convert_move_input_to_position(move)
        self.board_positions[move_row_indx, move_column_indx] = PLAYERS[self.player_to_act][BOARD_VALUE]


    def check_game_status(self):
        player_to_act = self.player_to_act
        opponent = PLAYERS[self.player_to_act][OPPONENT]
        
        if len(np.where(self.board_positions == 0)[0]) == 0: positions_still_available = False
        else: positions_still_available = True

        if positions_still_available:
            player_to_act_positions = list(zip(*[x.tolist() for x in np.where(self.board_positions == PLAYERS[player_to_act][BOARD_VALUE])]))
            opponent_positions = list(zip(*[x.tolist() for x in np.where(self.board_positions == PLAYERS[opponent][BOARD_VALUE])]))
            
            for win_combo in self.win_combos:
                if set(win_combo).issubset(player_to_act_positions):
                    if player_to_act == PLAYER_1:
                        return PLAYER_1_WIN_STATUS
                    else:
                        return PLAYER_2_WIN_STATUS
                elif set(win_combo).issubset(opponent_positions):
                    if opponent == PLAYER_1:
                        return PLAYER_1_WIN_STATUS
                    else:
                        return PLAYER_2_WIN_STATUS
            
            return ONGOING_GAME_STATUS
            
        else:
            return DRAW_STATUS


    def get_separator_line(self):
        return ['-']*(self.columns*6 + 6)


    def convert_row_to_print_string(
        self
        , row
        , row_indx
    ):
        return (
            f"{str(row_indx).ljust(5, ' ')}" +
            '|' + 
            (
                '|'\
                .join(row)\
                .replace(str(PLAYERS[PLAYER_2][BOARD_VALUE]), f'  {PLAYERS[PLAYER_2][BOARD_STR]}  ')\
                .replace(str(PLAYERS[PLAYER_1][BOARD_VALUE]), f'  {PLAYERS[PLAYER_1][BOARD_STR]}  ')\
                .replace('0', '     ')
            ) +
            '|\n' +
            '-----|' + 
            (
                '|'\
                .join(row)\
                .replace(str(PLAYERS[PLAYER_2][BOARD_VALUE]), '  -  ')\
                .replace(str(PLAYERS[PLAYER_1][BOARD_VALUE]), '  -  ')\
                .replace('0', '  -  ')
            ) +
            '|'
        )


    def get_board_string(self):
        
        board_header = (
            '     |' +
            "|".join([f'  {str(column_indx)}  ' for column_indx in range(self.columns)]) +
            '|\n' +
            ''.join(self.get_separator_line())
        )
        
        board_strings = [board_header]
        for row_indx, row in enumerate(self.board_positions):
            row = [str(x) for x in row]
            board_strings.append(self.convert_row_to_print_string(row, row_indx))
        
        board_footer = ''.join(self.get_separator_line())
        board_strings.append(board_footer)
        
        return '\n'.join(board_strings)


    def __repr__(self):
        return self.get_board_string()


    def __str__(self):
        return self.get_board_string()


class State:
    
    def __init__(self, board: Board, num_wins = 0, num_visits = 0):
        self.board = board
        self.player_to_act = self.board.player_to_act
        self.num_wins = num_wins
        self.num_visits = num_visits
    

    def get_available_moves(self):
        
        available_moves = list(zip(*[indx.tolist() for indx in np.where(self.board.board_positions == 0)]))
        available_board_positions = []
        for available_move in available_moves:
            new_board_positions = deepcopy(self.board.board_positions)
            row_index = available_move[0]
            column_index = available_move[1]
            new_board_positions[row_index, column_index] = 1

        return available_moves, available_board_positions
    

    def state_is_terminal(self):
        available_moves, _ = self.get_available_moves()
        return len(available_moves) == 0


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


class Mcts:
    
    def __init__(self, root_node: Node):
        self.root_node = root_node
    
    
    def select_best_move(self):
        # self.selection()
        # self.expansion()
        # self.simulation()
        # self.back_propogation()

        # 0. while time and computational resources are available, and total simulations of root node < threshold:
        # 1. Take current state as root node
        # 2. [selection] If root node has any possible child nodes
            # 2.1. [selection] go down the tree by repeatedly (1) selecting a legal move, and (2) advancing to the corresponding child node,
            #      until a node without any further children is reached. This will be called the selected node
            # 2.2. [selection] if the selected node is a terminal node:
                # 2.2.1. [back propogation] Update the statistics of the selected node (wins, simulations, UCB)
                # 2.2.2. [back propogation] Update the statistics of ALL parent nodes of the selected node (wins, simulations, UCB)
            # 2.3. [selection] If not:
                # 2.3.1. [expansion] get list of available moves, and add these as children of the selected node 
                # 2.3.2. [expansion] ensure each of these children are initialised with a "w" of 0, "n" of 0 and UCB of ???
                # 2.3.3. [expansion] select a child at random
                # 2.3.4. [simulation] continuing from the selected child node, play moves at random and repeatedly advance the game state.
                #        until the game is finished and (a winner emerges or the game ends in a draw). No new nodes are created in this phase.
                #        No part of this process is stored
                # 2.3.5. [back propogation] Update the statistics of this node that was selected during expansion (wins, simulations, UCB)
                # 2.3.6. [back propogation] Update the statistics of ALL parent nodes of the node selected during expansion

        # 3. [selection] If not:
            # 3.1. if the root node is a terminal node (i.e. game has ended):
                # ! 3.1.1. the game should've already ended # check this !!!!
            # 3.2. if not:
                # 3.2.1. [expansion] get list of available moves, and add these as children of the root
                # 3.2.2. [expansion] ensure each of these children are initialised with a "w" of 0, "n" of 0 and UCB of ???
                # 3.2.3. [expansion] select a child at random
                # 3.2.4. [simulation] continuing from the selected child node, play moves at random and repeatedly advance the game state.
                #        until the game is finished and (a winner emerges or the game ends in a draw). No new nodes are created in this phase.
                #        No part of this process is stored
                # 3.2.5. [back propogation] Update the statistics of this node that was selected during expansion (wins, simulations, UCB)
                # 3.2.6. [back propogation] Update the statistics of ALL parent nodes of the node selected during expansion
        
        NotImplemented
    
    
    def selection(self):
        
        selected_node = self.root_node
        if selected_node.child_nodes == []:
            if selected_node.node_is_terminal():
                # ! The game should've already ended # check this !!!!
                print("Something's gone wrong... Check the code in the selection phase of MCTS")
                return self
            else:
                return self
        else:
            child_nodes = deepcopy(selected_node.child_nodes)
            while child_nodes != []:
                max_ucb = max(child_nodes, key= lambda x: x.state.calculate_ucb())
                max_ucb_nodes = [child_node for child_node in child_nodes if child_node.state.calculate_ucb() == max_ucb]
                selected_node = random.choice(max_ucb_nodes)
            
            return selected_node
    
    
    def expansion(self):
        return
    
    
    def simulation(self):
        return
    
    
    def back_propogation(self):
        return








