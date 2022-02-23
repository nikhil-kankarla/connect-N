import numpy as np
import pytest
from copy import deepcopy
from project.config import PLAYERS, PLAYER_1, PLAYER_2, BOARD_VALUE, DRAW_STATUS, PLAYER_1_WIN_STATUS, PLAYER_2_WIN_STATUS, ONGOING_GAME_STATUS
from project.classes.board import Board
from project.win_combos import get_win_combos

class TestBoard:
    
    default_rows = 3
    default_columns = 3
    default_num_consecutive_for_win = 3
    default_board_positions = np.array([[0,0,0], [0,0,0], [0,0,0]])
    default_player_to_act = PLAYER_1
    default_win_combos = get_win_combos(rows = default_rows, columns = default_columns, num_consecutive_for_win = default_num_consecutive_for_win)
    default_board = Board(
        rows = default_rows
        , columns = default_columns
        , num_consecutive_for_win = default_num_consecutive_for_win
        , board_positions = default_board_positions
        , player_to_act = default_player_to_act
        , win_combos = default_win_combos
    )
    
    
    opponent_test_cases = [
        pytest.param(default_board, PLAYER_2)
        , pytest.param(
            Board(
                rows = default_rows
                , columns = default_columns
                , num_consecutive_for_win = default_num_consecutive_for_win
                , board_positions = default_board_positions
                , player_to_act = PLAYER_2
                , win_combos = default_win_combos
            )
            , PLAYER_1
        )
    ]
    @pytest.mark.parametrize('inp, expected', opponent_test_cases) 
    def test_opponent(self, inp, expected):
        assert inp.opponent() == expected
    
    
    new_game_bool_test_cases = [
        pytest.param(default_board, True)
        , pytest.param(
            Board(
                rows = default_rows
                , columns = default_columns
                , num_consecutive_for_win = default_num_consecutive_for_win
                , board_positions = np.array([[0, 0, 1], [0, 0, 0], [0, 0, 0]])
                , win_combos = default_win_combos
            )
            , False
        )
    ]
    @pytest.mark.parametrize('inp, expected', new_game_bool_test_cases)
    def test_new_game_bool(self, inp, expected):
        assert inp.new_game_bool() == expected
    
    
    input_is_valid_test_cases = [
        pytest.param('', 'Invalid input: Please ensure the row index and column index are separated by a comma\n')
        , pytest.param('a', 'Invalid input: Please ensure the row index and column index are separated by a comma\n')
        , pytest.param(',', 'Invalid input: Please ensure the row index is numeric\nInvalid input: Please ensure the column index is numeric\n')
        , pytest.param('a,', 'Invalid input: Please ensure the row index is numeric\nInvalid input: Please ensure the column index is numeric\n')
        , pytest.param('7', 'Invalid input: Please ensure the row index and column index are separated by a comma\n')
        , pytest.param('7,', 'Invalid input: Row index of 7 exceeds number of rows\nInvalid input: Please ensure the column index is numeric\n')
        , pytest.param('7,6', 'Invalid input: Row index of 7 exceeds number of rows\nInvalid input: Column index of 6 exceeds number of columns\n')
        , pytest.param('1, 8', 'Invalid input: Column index of 8 exceeds number of columns\n')
        , pytest.param('1,8', 'Invalid input: Column index of 8 exceeds number of columns\n')
        , pytest.param('1,8,', 'Invalid input: Please ensure there is only ONE comma in the input\n---The input should be of the form "X,Y", where X is the row index and Y is the column index\n')
        , pytest.param('1,2', '')
        , pytest.param(' 1,2', '')
        , pytest.param('1 ,2', '')
        , pytest.param('1, 2', '')
        , pytest.param('1,2 ', '')
        , pytest.param(' 1 , 2 ', '')
    ]
    @pytest.mark.parametrize('inp, expected_print', input_is_valid_test_cases)
    def test_input_is_valid(self, inp, expected_print, capfd):
        self.default_board.check_input_is_valid_format(inp)
        out, _ = capfd.readouterr()
        assert out == expected_print
    
    
    valid_moves_test_cases = [
        pytest.param(
            default_board
            , [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
        )
        , pytest.param(
            Board(
                rows = default_rows
                , columns = default_columns
                , num_consecutive_for_win = default_num_consecutive_for_win
                , board_positions = np.array(([1,0,0], [0,0,0], [0,0,0]))
                , win_combos = default_win_combos
            )
            , [(0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
        )
        , pytest.param(
            Board(
                rows = default_rows
                , columns = default_columns
                , num_consecutive_for_win = default_num_consecutive_for_win
                , board_positions = np.array(([0,0,0], [0,0,0], [0,0,-1]))
                , win_combos = default_win_combos
            )
            , [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1)]
        )
        , pytest.param(
            Board(
                rows = default_rows
                , columns = default_columns
                , num_consecutive_for_win = default_num_consecutive_for_win
                , board_positions = np.array(([1,0,0], [0,0,0], [0,0,-1]))
                , win_combos = default_win_combos
            )
            , [(0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1)]
        )
    ]
    @pytest.mark.parametrize('inp, expected', valid_moves_test_cases)
    def test_valid_moves(self, inp, expected):
        assert inp.get_valid_moves() == expected
    
    
    convert_move_to_position_test_cases = [pytest.param('1,1', (1,1))]
    @pytest.mark.parametrize('inp, expected', convert_move_to_position_test_cases)
    def test_convert_move_input_to_position(self, inp, expected):
        assert self.default_board.convert_move_input_to_position(inp) == expected
    
    
    check_move_is_valid_test_cases = [
        pytest.param('1,1', True)
        , pytest.param('5,5', False)
    ]
    @pytest.mark.parametrize('inp, expected', check_move_is_valid_test_cases)
    def test_move_is_valid(self, inp, expected):
        self.default_board.check_move_is_valid(inp) == expected
    
    
    play_move_test_cases = [
        pytest.param(
            default_board
            , '1,1'
            , Board(
                rows = default_rows
                , columns = default_columns
                , num_consecutive_for_win = default_num_consecutive_for_win
                , board_positions = np.array([[0,0,0], [0,PLAYERS[default_player_to_act][BOARD_VALUE],0], [0,0,0]])
                , win_combos = default_win_combos
            )
        )
        , pytest.param(
            Board(player_to_act=PLAYER_2)
            , '0,2'
            , Board(
                rows = default_rows
                , columns = default_columns
                , num_consecutive_for_win = default_num_consecutive_for_win
                , board_positions = np.array([[0,0,PLAYERS[PLAYER_2][BOARD_VALUE]], [0,0,0], [0,0,0]])
                , win_combos = default_win_combos
            )
        )
    ]
    @pytest.mark.parametrize('input_board, move, expected_board', play_move_test_cases)
    def test_play_move(self, input_board, move, expected_board):
        temp_board = deepcopy(input_board)
        temp_board.play_move(move)
        assert np.array_equal(temp_board.board_positions, expected_board.board_positions)
    
    
    game_status_test_cases = [
        pytest.param(
            Board(
                rows = default_rows
                , columns = default_columns
                , num_consecutive_for_win = default_num_consecutive_for_win
                , board_positions = np.array([[1,0,-1], [-1,0,1], [1,0,-1]])
                , win_combos = default_win_combos
            )
            , ONGOING_GAME_STATUS
        )
        , pytest.param(
            Board(
                rows = default_rows
                , columns = default_columns
                , num_consecutive_for_win = default_num_consecutive_for_win
                , board_positions = np.array(
                    [
                        [PLAYERS[PLAYER_1][BOARD_VALUE],PLAYERS[PLAYER_1][BOARD_VALUE],PLAYERS[PLAYER_1][BOARD_VALUE]]
                        , [0,0,0]
                        , [0,0,0]
                    ]
                )
                , win_combos = default_win_combos
            )
            , PLAYER_1_WIN_STATUS
        )
        , pytest.param(
            Board(
                rows = default_rows
                , columns = default_columns
                , num_consecutive_for_win = default_num_consecutive_for_win
                , board_positions = np.array(
                    [
                        [PLAYERS[PLAYER_2][BOARD_VALUE],PLAYERS[PLAYER_2][BOARD_VALUE],PLAYERS[PLAYER_2][BOARD_VALUE]]
                        , [0,0,0]
                        , [0,0,0]
                    ]
                )
                , win_combos = default_win_combos
            )
            , PLAYER_2_WIN_STATUS
        )
        , pytest.param(
            Board(
                rows = default_rows
                , columns = default_columns
                , num_consecutive_for_win = default_num_consecutive_for_win
                , board_positions = np.array(
                    [
                        [PLAYERS[PLAYER_1][BOARD_VALUE],PLAYERS[PLAYER_2][BOARD_VALUE],PLAYERS[PLAYER_1][BOARD_VALUE]]
                        , [PLAYERS[PLAYER_2][BOARD_VALUE],PLAYERS[PLAYER_2][BOARD_VALUE],PLAYERS[PLAYER_1][BOARD_VALUE]]
                        , [PLAYERS[PLAYER_1][BOARD_VALUE],PLAYERS[PLAYER_1][BOARD_VALUE],PLAYERS[PLAYER_2][BOARD_VALUE]]
                    ]
                )
                , win_combos = default_win_combos
            )
            , DRAW_STATUS
        )
        , pytest.param(
            Board(
                rows = default_rows
                , columns = default_columns
                , num_consecutive_for_win = default_num_consecutive_for_win
                , board_positions = np.array(
                    [
                        [PLAYERS[PLAYER_1][BOARD_VALUE],PLAYERS[PLAYER_2][BOARD_VALUE],PLAYERS[PLAYER_1][BOARD_VALUE]]
                        , [PLAYERS[PLAYER_1][BOARD_VALUE],PLAYERS[PLAYER_1][BOARD_VALUE],PLAYERS[PLAYER_2][BOARD_VALUE]]
                        , [PLAYERS[PLAYER_1][BOARD_VALUE],PLAYERS[PLAYER_2][BOARD_VALUE],PLAYERS[PLAYER_2][BOARD_VALUE]]
                    ]
                )
                , win_combos = default_win_combos
            )
            , PLAYER_1_WIN_STATUS
        )
    ]
    @pytest.mark.parametrize('input_board, expected_game_status', game_status_test_cases)
    def test_game_status(self, input_board, expected_game_status):
        assert input_board.check_game_status() == expected_game_status
    
    
    board_string_test_cases = [
        pytest.param(
            default_board
            ,   '     |  0  |  1  |  2  |\n' + 
                '------------------------\n' + 
                '0    |     |     |     |\n' + 
                '-----|  -  |  -  |  -  |\n' + 
                '1    |     |     |     |\n' + 
                '-----|  -  |  -  |  -  |\n' + 
                '2    |     |     |     |\n' + 
                '-----|  -  |  -  |  -  |\n' + 
                '------------------------\n'
        )
        , pytest.param(
            Board(
                4,4,3
                , board_positions = np.array([[1,0,-1,0],[0,-1,0,1],[1,0,-1,0],[0,-1,0,1]])
            )
            ,   '     |  0  |  1  |  2  |  3  |\n' +
                '------------------------------\n' +
                '0    |  X  |     |  O  |     |\n' +
                '-----|  -  |  -  |  -  |  -  |\n' +
                '1    |     |  O  |     |  X  |\n' +
                '-----|  -  |  -  |  -  |  -  |\n' +
                '2    |  X  |     |  O  |     |\n' +
                '-----|  -  |  -  |  -  |  -  |\n' +
                '3    |     |  O  |     |  X  |\n' +
                '-----|  -  |  -  |  -  |  -  |\n' +
                '------------------------------\n'
        )
    ]
    @pytest.mark.parametrize('input_board, expected_board_string', board_string_test_cases)
    def test_board_string(self, input_board, expected_board_string, capfd):
        print(input_board)
        out, _ = capfd.readouterr()
        assert out == expected_board_string
