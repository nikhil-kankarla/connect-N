import numpy as np
import pytest
from copy import deepcopy
from project.config import PLAYERS, PLAYER_1, PLAYER_2, BOARD_VALUE, DRAW_STATUS, PLAYER_1_WIN_STATUS, PLAYER_2_WIN_STATUS, ONGOING_GAME_STATUS
from project.classes.board import Board
from project.classes.state import State
from project.win_combos import get_win_combos

class TestState:
    
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
    
    default_state = State(board = default_board, num_wins = 0, num_visits = 0)
    
    
    available_board_positions_test_cases = [
        pytest.param(
            default_state
            , [
                np.array([[1, 0, 0],[0, 0, 0],[0, 0, 0]])
                , np.array([[0, 1, 0],[0, 0, 0],[0, 0, 0]])
                , np.array([[0, 0, 1],[0, 0, 0],[0, 0, 0]])
                , np.array([[0, 0, 0],[1, 0, 0],[0, 0, 0]])
                , np.array([[0, 0, 0],[0, 1, 0],[0, 0, 0]])
                , np.array([[0, 0, 0],[0, 0, 1],[0, 0, 0]])
                , np.array([[0, 0, 0],[0, 0, 0],[1, 0, 0]])
                , np.array([[0, 0, 0],[0, 0, 0],[0, 1, 0]])
                , np.array([[0, 0, 0],[0, 0, 0],[0, 0, 1]])
            ]
        )
        , pytest.param(
            State(
                Board(
                    rows = default_rows
                    , columns = default_columns
                    , num_consecutive_for_win = default_num_consecutive_for_win
                    , board_positions = np.array(
                        [
                            [PLAYERS[PLAYER_1][BOARD_VALUE], PLAYERS[PLAYER_2][BOARD_VALUE], PLAYERS[PLAYER_1][BOARD_VALUE]]
                            , [0, PLAYERS[PLAYER_2][BOARD_VALUE], 0]
                            , [PLAYERS[PLAYER_2][BOARD_VALUE], PLAYERS[PLAYER_1][BOARD_VALUE], PLAYERS[PLAYER_2][BOARD_VALUE]]
                        ]
                    )
                    , player_to_act = PLAYER_1
                    , win_combos = default_win_combos
                )
            )
            , [
                np.array(
                    [
                        [PLAYERS[PLAYER_1][BOARD_VALUE], PLAYERS[PLAYER_2][BOARD_VALUE], PLAYERS[PLAYER_1][BOARD_VALUE]]
                        , [PLAYERS[PLAYER_1][BOARD_VALUE], PLAYERS[PLAYER_2][BOARD_VALUE], 0]
                        , [PLAYERS[PLAYER_2][BOARD_VALUE], PLAYERS[PLAYER_1][BOARD_VALUE], PLAYERS[PLAYER_2][BOARD_VALUE]]
                    ]
                )
                , np.array(
                    [
                        [PLAYERS[PLAYER_1][BOARD_VALUE], PLAYERS[PLAYER_2][BOARD_VALUE], PLAYERS[PLAYER_1][BOARD_VALUE]]
                        , [0, PLAYERS[PLAYER_2][BOARD_VALUE], PLAYERS[PLAYER_1][BOARD_VALUE]]
                        , [PLAYERS[PLAYER_2][BOARD_VALUE], PLAYERS[PLAYER_1][BOARD_VALUE], PLAYERS[PLAYER_2][BOARD_VALUE]]
                    ]
                )
            ]
        )
        , pytest.param(
            State(
                Board(
                    rows = default_rows
                    , columns = default_columns
                    , num_consecutive_for_win = default_num_consecutive_for_win
                    , board_positions = np.array(
                        [
                            [PLAYERS[PLAYER_1][BOARD_VALUE], PLAYERS[PLAYER_2][BOARD_VALUE], PLAYERS[PLAYER_1][BOARD_VALUE]]
                            , [0, PLAYERS[PLAYER_2][BOARD_VALUE], 0]
                            , [PLAYERS[PLAYER_2][BOARD_VALUE], PLAYERS[PLAYER_1][BOARD_VALUE], PLAYERS[PLAYER_2][BOARD_VALUE]]
                        ]
                    )
                    , player_to_act = PLAYER_2
                    , win_combos = default_win_combos
                )
            )
            , [
                np.array(
                    [
                        [PLAYERS[PLAYER_1][BOARD_VALUE], PLAYERS[PLAYER_2][BOARD_VALUE], PLAYERS[PLAYER_1][BOARD_VALUE]]
                        , [PLAYERS[PLAYER_2][BOARD_VALUE], PLAYERS[PLAYER_2][BOARD_VALUE], 0]
                        , [PLAYERS[PLAYER_2][BOARD_VALUE], PLAYERS[PLAYER_1][BOARD_VALUE], PLAYERS[PLAYER_2][BOARD_VALUE]]
                    ]
                )
                , np.array(
                    [
                        [PLAYERS[PLAYER_1][BOARD_VALUE], PLAYERS[PLAYER_2][BOARD_VALUE], PLAYERS[PLAYER_1][BOARD_VALUE]]
                        , [0, PLAYERS[PLAYER_2][BOARD_VALUE], PLAYERS[PLAYER_2][BOARD_VALUE]]
                        , [PLAYERS[PLAYER_2][BOARD_VALUE], PLAYERS[PLAYER_1][BOARD_VALUE], PLAYERS[PLAYER_2][BOARD_VALUE]]
                    ]
                )
            ]
        )
        , pytest.param(
            State(
                Board(
                    rows = default_rows
                    , columns = default_columns
                    , num_consecutive_for_win = default_num_consecutive_for_win
                    , board_positions = np.array(
                        [
                            [PLAYERS[PLAYER_1][BOARD_VALUE], PLAYERS[PLAYER_2][BOARD_VALUE], PLAYERS[PLAYER_1][BOARD_VALUE]]
                            , [PLAYERS[PLAYER_2][BOARD_VALUE], PLAYERS[PLAYER_2][BOARD_VALUE], PLAYERS[PLAYER_1][BOARD_VALUE]]
                            , [PLAYERS[PLAYER_1][BOARD_VALUE], PLAYERS[PLAYER_1][BOARD_VALUE], PLAYERS[PLAYER_2][BOARD_VALUE]]
                        ]
                    )
                    , player_to_act = PLAYER_1
                    , win_combos = default_win_combos
                )
            )
            , []
        )
    ]
    @pytest.mark.parametrize('inp, expected', available_board_positions_test_cases)
    def test_available_board_positions(self, inp: State, expected):
        for actual_board_position, expected_board_position in zip(inp.get_available_board_positions(), expected):
            assert np.array_equal(actual_board_position, expected_board_position)
    
    
    state_is_terminal_test_cases = [
        pytest.param(
            default_state
            , False
        )
        , pytest.param(
            State(
                Board(
                    rows = default_rows
                    , columns = default_columns
                    , num_consecutive_for_win = default_num_consecutive_for_win
                    , board_positions = np.array([[0,0,-1], [0,1,-1], [1,0,0]])
                    , player_to_act = default_player_to_act
                    , win_combos = default_win_combos
                )
            )
            , False
        ), pytest.param(
            State(
                Board(
                    rows = default_rows
                    , columns = default_columns
                    , num_consecutive_for_win = default_num_consecutive_for_win
                    , board_positions = np.array([[1,1,1], [-1,-1,0], [0,0,0]])
                    , player_to_act = default_player_to_act
                    , win_combos = default_win_combos
                )
            )
            , True
        ), pytest.param(
            State(
                Board(
                    rows = default_rows
                    , columns = default_columns
                    , num_consecutive_for_win = default_num_consecutive_for_win
                    , board_positions = np.array([[1,-1,1], [-1,-1,1], [1,1,-1]])
                    , player_to_act = default_player_to_act
                    , win_combos = default_win_combos
                )
            )
            , True
        )
    ]
    @pytest.mark.parametrize('inp, expected', state_is_terminal_test_cases)
    def test_state_is_terminal(self, inp: State, expected):
        return inp.state_is_terminal() == expected
    

    state_str_test_cases = [
        pytest.param(
            default_state
            , (
                default_board.__str__() + '\n' +
                f'Number of wins: 0\n' +
                f'Number of visits: 0\n' +
                f'Win ratio: 0'
            )
        )
        , pytest.param(
            State(
                board = default_board
                , num_wins = 10
                , num_visits = 50
            )
            , (
                default_board.__str__() + '\n' +
                f'Number of wins: 10\n' +
                f'Number of visits: 50\n' +
                f'Win ratio: 0.2'
            )
        )
    ]
    @pytest.mark.parametrize('inp, expected', state_str_test_cases)
    def test_state_str(self, inp: State, expected):
        return inp.get_state_str() == expected