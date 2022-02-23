import numpy as np
from project.config import (
    ROWS
    , COLUMNS
    , NUM_CONSECUTIVE_FOR_WIN
    , PLAYER_1
    , PLAYER_2
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
        , player_to_act = PLAYER_1
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
        print(f'Player 1 won: {len([result for result in games.values() if result == PLAYER_1_WIN_STATUS])} game(s)')
        print(f'Player 2 won: {len([result for result in games.values() if result == PLAYER_2_WIN_STATUS])} game(s)')
        print(f'Draws       : {len([result for result in games.values() if result == DRAW_STATUS])} games\n')
    
    
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
        
        if positions_still_available:
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