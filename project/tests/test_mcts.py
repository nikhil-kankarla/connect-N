from copy import deepcopy
import numpy as np
import pytest
from project.classes.board import Board
from project.classes.mcts import Mcts
from project.classes.node import Node
from project.classes.state import State
from project.config import BOARD_VALUE, OPPONENT, PLAYER_1, PLAYERS
from project.win_combos import get_win_combos

class TestMcts:

    default_rows = 3
    default_columns = 3
    default_num_consecutive_for_win = 3
    default_board_positions = np.array([[0,0,0], [0,0,0], [0,0,0]])
    default_player_to_act = PLAYER_1
    default_opponent = PLAYERS[default_player_to_act][OPPONENT]
    default_win_combos = get_win_combos(rows = default_rows, columns = default_columns, num_consecutive_for_win = default_num_consecutive_for_win)
    
    default_board = Board(
        rows = default_rows
        , columns = default_columns
        , num_consecutive_for_win = default_num_consecutive_for_win
        , board_positions = default_board_positions
        , player_to_act = default_player_to_act
        , win_combos = default_win_combos
    )
    
    default_num_wins = 0
    default_num_visits = 0
    default_state = State(board = default_board, num_wins = default_num_wins, num_visits = default_num_visits)
    
    default_parent_node = None
    default_child_nodes = []
    default_node = Node(state = default_state, parent_node = default_parent_node, child_nodes = default_child_nodes)

    default_mcts_decision_time = 1
    default_mcts = Mcts(
        root_node = default_node
        , mcts_decision_time = default_mcts_decision_time
    )
    
    
    selection_test_cases = [
        pytest.param(
            default_mcts
            , [default_node]
        )
        , pytest.param(
            Mcts(
                Node(
                    state = default_state
                    , parent_node = None
                    , child_nodes = [
                        Node(
                            State(
                                Board(
                                    rows = default_rows
                                    , columns = default_columns
                                    , num_consecutive_for_win = default_num_consecutive_for_win
                                    , board_positions = np.array([
                                        [PLAYERS[default_player_to_act][BOARD_VALUE],0,0]
                                        , [0,0,0]
                                        , [0,0,0]
                                    ])
                                    , player_to_act = default_player_to_act
                                    , win_combos = default_win_combos
                                )
                                , num_wins = 0
                                , num_visits = 0
                            )
                            , parent_node = default_node
                            , child_nodes = []
                        )
                        , Node(
                            State(
                                Board(
                                    rows = default_rows
                                    , columns = default_columns
                                    , num_consecutive_for_win = default_num_consecutive_for_win
                                    , board_positions = np.array([
                                        [0,PLAYERS[default_player_to_act][BOARD_VALUE],0]
                                        , [0,0,0]
                                        , [0,0,0]
                                    ])
                                    , player_to_act = default_player_to_act
                                    , win_combos = default_win_combos
                                )
                                , num_wins = 0
                                , num_visits = 0
                            )
                            , parent_node = default_node
                            , child_nodes = []
                        )
                        , Node(
                            State(
                                Board(
                                    rows = default_rows
                                    , columns = default_columns
                                    , num_consecutive_for_win = default_num_consecutive_for_win
                                    , board_positions = np.array([
                                        [0,0,PLAYERS[default_player_to_act][BOARD_VALUE]]
                                        , [0,0,0]
                                        , [0,0,0]
                                    ])
                                    , player_to_act = default_player_to_act
                                    , win_combos = default_win_combos
                                )
                                , num_wins = 0
                                , num_visits = 0
                            )
                            , parent_node = default_node
                            , child_nodes = []
                        )
                        , Node(
                            State(
                                Board(
                                    rows = default_rows
                                    , columns = default_columns
                                    , num_consecutive_for_win = default_num_consecutive_for_win
                                    , board_positions = np.array([
                                        [0,0,0]
                                        , [PLAYERS[default_player_to_act][BOARD_VALUE],0,0]
                                        , [0,0,0]
                                    ])
                                    , player_to_act = default_player_to_act
                                    , win_combos = default_win_combos
                                )
                                , num_wins = 0
                                , num_visits = 0
                            )
                            , parent_node = default_node
                            , child_nodes = []
                        )
                        , Node(
                            State(
                                Board(
                                    rows = default_rows
                                    , columns = default_columns
                                    , num_consecutive_for_win = default_num_consecutive_for_win
                                    , board_positions = np.array([
                                        [0,0,0]
                                        , [0,PLAYERS[default_player_to_act][BOARD_VALUE],0]
                                        , [0,0,0]
                                    ])
                                    , player_to_act = default_player_to_act
                                    , win_combos = default_win_combos
                                )
                                , num_wins = 0
                                , num_visits = 0
                            )
                            , parent_node = default_node
                            , child_nodes = []
                        )
                        , Node(
                            State(
                                Board(
                                    rows = default_rows
                                    , columns = default_columns
                                    , num_consecutive_for_win = default_num_consecutive_for_win
                                    , board_positions = np.array([
                                        [0,0,0]
                                        , [0,0,PLAYERS[default_player_to_act][BOARD_VALUE]]
                                        , [0,0,0]
                                    ])
                                    , player_to_act = default_player_to_act
                                    , win_combos = default_win_combos
                                )
                                , num_wins = 0
                                , num_visits = 0
                            )
                            , parent_node = default_node
                            , child_nodes = []
                        )
                        , Node(
                            State(
                                Board(
                                    rows = default_rows
                                    , columns = default_columns
                                    , num_consecutive_for_win = default_num_consecutive_for_win
                                    , board_positions = np.array([
                                        [0,0,0]
                                        , [0,0,0]
                                        , [PLAYERS[default_player_to_act][BOARD_VALUE],0,0]
                                    ])
                                    , player_to_act = default_player_to_act
                                    , win_combos = default_win_combos
                                )
                                , num_wins = 0
                                , num_visits = 0
                            )
                            , parent_node = default_node
                            , child_nodes = []
                        )
                        , Node(
                            State(
                                Board(
                                    rows = default_rows
                                    , columns = default_columns
                                    , num_consecutive_for_win = default_num_consecutive_for_win
                                    , board_positions = np.array([
                                        [0,0,0]
                                        , [0,0,0]
                                        , [0,PLAYERS[default_player_to_act][BOARD_VALUE],0]
                                    ])
                                    , player_to_act = default_player_to_act
                                    , win_combos = default_win_combos
                                )
                                , num_wins = 0
                                , num_visits = 0
                            )
                            , parent_node = default_node
                            , child_nodes = []
                        )
                        , Node(
                            State(
                                Board(
                                    rows = default_rows
                                    , columns = default_columns
                                    , num_consecutive_for_win = default_num_consecutive_for_win
                                    , board_positions = np.array([
                                        [0,0,0]
                                        , [0,0,0]
                                        , [0,0,PLAYERS[default_player_to_act][BOARD_VALUE]]
                                    ])
                                    , player_to_act = default_player_to_act
                                    , win_combos = default_win_combos
                                )
                                , num_wins = 0
                                , num_visits = 0
                            )
                            , parent_node = default_node
                            , child_nodes = []
                        )
                    ]
                )
            )
            , [
                Node(
                    State(
                        Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([
                                [PLAYERS[default_player_to_act][BOARD_VALUE],0,0]
                                , [0,0,0]
                                , [0,0,0]
                            ])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 0
                    )
                    , parent_node = default_node
                    , child_nodes = []
                )
                , Node(
                    State(
                        Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([
                                [0,PLAYERS[default_player_to_act][BOARD_VALUE],0]
                                , [0,0,0]
                                , [0,0,0]
                            ])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 0
                    )
                    , parent_node = default_node
                    , child_nodes = []
                )
                , Node(
                    State(
                        Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([
                                [0,0,PLAYERS[default_player_to_act][BOARD_VALUE]]
                                , [0,0,0]
                                , [0,0,0]
                            ])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 0
                    )
                    , parent_node = default_node
                    , child_nodes = []
                )
                , Node(
                    State(
                        Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([
                                [0,0,0]
                                , [PLAYERS[default_player_to_act][BOARD_VALUE],0,0]
                                , [0,0,0]
                            ])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 0
                    )
                    , parent_node = default_node
                    , child_nodes = []
                )
                , Node(
                    State(
                        Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([
                                [0,0,0]
                                , [0,PLAYERS[default_player_to_act][BOARD_VALUE],0]
                                , [0,0,0]
                            ])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 0
                    )
                    , parent_node = default_node
                    , child_nodes = []
                )
                , Node(
                    State(
                        Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([
                                [0,0,0]
                                , [0,0,PLAYERS[default_player_to_act][BOARD_VALUE]]
                                , [0,0,0]
                            ])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 0
                    )
                    , parent_node = default_node
                    , child_nodes = []
                )
                , Node(
                    State(
                        Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([
                                [0,0,0]
                                , [0,0,0]
                                , [PLAYERS[default_player_to_act][BOARD_VALUE],0,0]
                            ])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 0
                    )
                    , parent_node = default_node
                    , child_nodes = []
                )
                , Node(
                    State(
                        Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([
                                [0,0,0]
                                , [0,0,0]
                                , [0,PLAYERS[default_player_to_act][BOARD_VALUE],0]
                            ])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 0
                    )
                    , parent_node = default_node
                    , child_nodes = []
                )
                , Node(
                    State(
                        Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([
                                [0,0,0]
                                , [0,0,0]
                                , [0,0,PLAYERS[default_player_to_act][BOARD_VALUE]]
                            ])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 0
                    )
                    , parent_node = default_node
                    , child_nodes = []
                )
            ]
        )
    ]
    @pytest.mark.parametrize('inp, expected', selection_test_cases)
    def test_selection(self, inp, expected):
        assert set([n.__str__() for n in expected]).issuperset([inp.selection().__str__()])
    
    
    expansion_test_cases = [
        pytest.param(
            Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                            , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                            , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                )
                , child_nodes = []
            )
            , Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE]]
                            , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                            , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                    , parent_node = Node(
                        state = State(
                            board = Board(
                                rows = default_rows
                                , columns = default_columns
                                , num_consecutive_for_win = default_num_consecutive_for_win
                                , board_positions = np.array(
                                    [[PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                    , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                    , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]]
                                )
                                , player_to_act = default_player_to_act
                                , win_combos = default_win_combos
                            )
                        )
                    )
                    , child_nodes = []
                )
                , child_nodes = []
            )
        )
        , pytest.param(
            Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                            , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                            , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                )
                , child_nodes = []
            )
            , Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                            , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE]]
                            , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                    , parent_node = Node(
                        state = State(
                            board = Board(
                                rows = default_rows
                                , columns = default_columns
                                , num_consecutive_for_win = default_num_consecutive_for_win
                                , board_positions = np.array(
                                    [[PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                    , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                    , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]]
                                )
                                , player_to_act = default_player_to_act
                                , win_combos = default_win_combos
                            )
                        )
                    )
                    , child_nodes = []
                )
                , child_nodes = []
            )
        )
        , pytest.param(
            Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                            , [0, 0, 0]
                            , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                , [0, 0, 0]
                                , [0, 0, 0]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                )
                , child_nodes = []
            )
            , Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                            , [0, 0, 0]
                            , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                , [0, 0, 0]
                                , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                    , parent_node = Node(
                        state = State(
                            board = Board(
                                rows = default_rows
                                , columns = default_columns
                                , num_consecutive_for_win = default_num_consecutive_for_win
                                , board_positions = np.array(
                                    [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                    , [0, 0, 0]
                                    , [0, 0, 0]]
                                )
                                , player_to_act = default_player_to_act
                                , win_combos = default_win_combos
                            )
                        )
                    )
                    , child_nodes = []
                )
                , child_nodes = []
            )
        )
        , pytest.param(
            Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                            , [0, 0, 0]
                            , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                , [0, 0, 0]
                                , [0, 0, 0]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                )
                , child_nodes = []
            )
            , Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, PLAYERS[default_player_to_act][BOARD_VALUE]]
                            , [0, 0, 0]
                            , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                , [0, 0, 0]
                                , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                    , parent_node = Node(
                        state = State(
                            board = Board(
                                rows = default_rows
                                , columns = default_columns
                                , num_consecutive_for_win = default_num_consecutive_for_win
                                , board_positions = np.array(
                                    [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                    , [0, 0, 0]
                                    , [0, 0, 0]]
                                )
                                , player_to_act = default_player_to_act
                                , win_combos = default_win_combos
                            )
                        )
                    )
                    , child_nodes = []
                )
                , child_nodes = []
            )
        )
        , pytest.param(
            Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                            , [0, 0, 0]
                            , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                , [0, 0, 0]
                                , [0, 0, 0]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                )
                , child_nodes = []
            )
            , Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                            , [PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                            , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                , [0, 0, 0]
                                , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                    , parent_node = Node(
                        state = State(
                            board = Board(
                                rows = default_rows
                                , columns = default_columns
                                , num_consecutive_for_win = default_num_consecutive_for_win
                                , board_positions = np.array(
                                    [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                    , [0, 0, 0]
                                    , [0, 0, 0]]
                                )
                                , player_to_act = default_player_to_act
                                , win_combos = default_win_combos
                            )
                        )
                    )
                    , child_nodes = []
                )
                , child_nodes = []
            )
        )
        , pytest.param(
            Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                            , [0, 0, 0]
                            , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                , [0, 0, 0]
                                , [0, 0, 0]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                )
                , child_nodes = []
            )
            , Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                            , [0, PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                            , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                , [0, 0, 0]
                                , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                    , parent_node = Node(
                        state = State(
                            board = Board(
                                rows = default_rows
                                , columns = default_columns
                                , num_consecutive_for_win = default_num_consecutive_for_win
                                , board_positions = np.array(
                                    [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                    , [0, 0, 0]
                                    , [0, 0, 0]]
                                )
                                , player_to_act = default_player_to_act
                                , win_combos = default_win_combos
                            )
                        )
                    )
                    , child_nodes = []
                )
                , child_nodes = []
            )
        )
        , pytest.param(
            Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                            , [0, 0, 0]
                            , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                , [0, 0, 0]
                                , [0, 0, 0]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                )
                , child_nodes = []
            )
            , Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                            , [0, 0, PLAYERS[default_player_to_act][BOARD_VALUE]]
                            , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                , [0, 0, 0]
                                , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                    , parent_node = Node(
                        state = State(
                            board = Board(
                                rows = default_rows
                                , columns = default_columns
                                , num_consecutive_for_win = default_num_consecutive_for_win
                                , board_positions = np.array(
                                    [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                    , [0, 0, 0]
                                    , [0, 0, 0]]
                                )
                                , player_to_act = default_player_to_act
                                , win_combos = default_win_combos
                            )
                        )
                    )
                    , child_nodes = []
                )
                , child_nodes = []
            )
        )
        , pytest.param(
            Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                            , [0, 0, 0]
                            , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                , [0, 0, 0]
                                , [0, 0, 0]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                )
                , child_nodes = []
            )
            , Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                            , [0, 0, 0]
                            , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                , [0, 0, 0]
                                , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                    , parent_node = Node(
                        state = State(
                            board = Board(
                                rows = default_rows
                                , columns = default_columns
                                , num_consecutive_for_win = default_num_consecutive_for_win
                                , board_positions = np.array(
                                    [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                    , [0, 0, 0]
                                    , [0, 0, 0]]
                                )
                                , player_to_act = default_player_to_act
                                , win_combos = default_win_combos
                            )
                        )
                    )
                    , child_nodes = []
                )
                , child_nodes = []
            )
        )
        , pytest.param(
            Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                            , [0, 0, 0]
                            , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                , [0, 0, 0]
                                , [0, 0, 0]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                )
                , child_nodes = []
            )
            , Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                            , [0, 0, 0]
                            , [PLAYERS[default_opponent][BOARD_VALUE], 0, PLAYERS[default_player_to_act][BOARD_VALUE]]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                , [0, 0, 0]
                                , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                    , parent_node = Node(
                        state = State(
                            board = Board(
                                rows = default_rows
                                , columns = default_columns
                                , num_consecutive_for_win = default_num_consecutive_for_win
                                , board_positions = np.array(
                                    [[PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                    , [0, 0, 0]
                                    , [0, 0, 0]]
                                )
                                , player_to_act = default_player_to_act
                                , win_combos = default_win_combos
                            )
                        )
                    )
                    , child_nodes = []
                )
                , child_nodes = []
            )
        )
        , pytest.param(
            Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]
                            , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE]]
                            , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]
                                , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                                , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                )
                , child_nodes = []
            )
            , Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]
                            , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE]]
                            , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]
                                , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                                , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                )
                , child_nodes = []
            )
        )
        , pytest.param(
            Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE]]
                            , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                            , [0, 0, 0]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                                , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                , [0, 0, 0]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                )
                , child_nodes = []
            )
            , Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array(
                            [[PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE]]
                            , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                            , [0, 0, 0]]
                        )
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array(
                                [[PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                                , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                , [0, 0, 0]]
                            )
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                    )
                )
                , child_nodes = []
            )
        )
    ]
    @pytest.mark.parametrize('inp, expected', expansion_test_cases)
    def test_expansion(self, inp, expected):
        mcts = Mcts(inp)
        selected_node = mcts.selection()
        expanded_node = mcts.expansion(selected_node)

        if expanded_node.node_is_terminal():
            assert inp.__str__() == expected.__str__()
        else:
            assert set([n.__str__() for n in mcts.root_node.child_nodes]).issuperset([expected.__str__()])
    
    
    simulation_test_cases = [
        pytest.param(
            Node(
                State(
                    Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array([
                            [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]
                            , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                            , [PLAYERS[default_player_to_act][BOARD_VALUE], 0, PLAYERS[default_opponent][BOARD_VALUE]]
                        ])
                        , player_to_act = default_opponent
                        , win_combos = default_win_combos
                    )
                    , num_wins = 0
                    , num_visits = 0
                )
                , parent_node = Node(
                    State(
                        Board(
                            rows = 3
                            , columns = 3
                            , num_consecutive_for_win = 3
                            , board_positions = np.array([
                                [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]
                                , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]
                                , [PLAYERS[default_player_to_act][BOARD_VALUE], 0, PLAYERS[default_opponent][BOARD_VALUE]]
                            ])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 1
                    )
                    , child_nodes = []
                )
                , child_nodes = []
            )
            , default_opponent
            , [
                Node(
                    State(
                        Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([
                                [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]
                                , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                                , [PLAYERS[default_player_to_act][BOARD_VALUE], 0, PLAYERS[default_opponent][BOARD_VALUE]]
                            ])
                            , player_to_act = default_opponent
                            , win_combos = default_win_combos
                        )
                        , num_wins = 1
                        , num_visits = 1
                    )
                    , parent_node = Node(
                        State(
                            Board(
                                rows = 3
                                , columns = 3
                                , num_consecutive_for_win = 3
                                , board_positions = np.array([
                                    [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]
                                    , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]
                                    , [PLAYERS[default_player_to_act][BOARD_VALUE], 0, PLAYERS[default_opponent][BOARD_VALUE]]
                                ])
                                , player_to_act = default_player_to_act
                                , win_combos = default_win_combos
                            )
                            , num_wins = 0
                            , num_visits = 1
                        )
                        , child_nodes = []
                    )
                    , child_nodes = []
                )
                , Node(
                    State(
                        Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([
                                [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]
                                , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                                , [PLAYERS[default_player_to_act][BOARD_VALUE], 0, PLAYERS[default_opponent][BOARD_VALUE]]
                            ])
                            , player_to_act = default_opponent
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0.5
                        , num_visits = 1
                    )
                    , parent_node = Node(
                        State(
                            Board(
                                rows = 3
                                , columns = 3
                                , num_consecutive_for_win = 3
                                , board_positions = np.array([
                                    [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]
                                    , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]
                                    , [PLAYERS[default_player_to_act][BOARD_VALUE], 0, PLAYERS[default_opponent][BOARD_VALUE]]
                                ])
                                , player_to_act = default_player_to_act
                                , win_combos = default_win_combos
                            )
                            , num_wins = 0
                            , num_visits = 1
                        )
                        , child_nodes = []
                    )
                    , child_nodes = []
                )
            ]
        )
        , pytest.param(
            Node(
                State(
                    Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array([
                            [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]
                            , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]
                            , [PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                        ])
                        , player_to_act = default_opponent
                        , win_combos = default_win_combos
                    )
                    , num_wins = 0
                    , num_visits = 0
                )
                , parent_node = Node(
                    State(
                        Board(
                            rows = 3
                            , columns = 3
                            , num_consecutive_for_win = 3
                            , board_positions = np.array([
                                [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]
                                , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]
                                , [PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                            ])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 1
                    )
                    , child_nodes = []
                )
                , child_nodes = []
            )
            , default_opponent
            , [
                Node(
                    State(
                        Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([
                                [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]
                                , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]
                                , [PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                            ])
                            , player_to_act = default_opponent
                            , win_combos = default_win_combos
                        )
                        , num_wins = 1
                        , num_visits = 1
                    )
                    , parent_node = Node(
                        State(
                            Board(
                                rows = 3
                                , columns = 3
                                , num_consecutive_for_win = 3
                                , board_positions = np.array([
                                    [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]
                                    , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]
                                    , [PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                ])
                                , player_to_act = default_player_to_act
                                , win_combos = default_win_combos
                            )
                            , num_wins = 0
                            , num_visits = 1
                        )
                        , child_nodes = []
                    )
                    , child_nodes = []
                )
                , Node(
                    State(
                        Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([
                                [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]
                                , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]
                                , [PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                            ])
                            , player_to_act = default_opponent
                            , win_combos = default_win_combos
                        )
                        , num_wins = -1
                        , num_visits = 1
                    )
                    , parent_node = Node(
                        State(
                            Board(
                                rows = 3
                                , columns = 3
                                , num_consecutive_for_win = 3
                                , board_positions = np.array([
                                    [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE]]
                                    , [PLAYERS[default_opponent][BOARD_VALUE], 0, 0]
                                    , [PLAYERS[default_player_to_act][BOARD_VALUE], 0, 0]
                                ])
                                , player_to_act = default_player_to_act
                                , win_combos = default_win_combos
                            )
                            , num_wins = 0
                            , num_visits = 1
                        )
                        , child_nodes = []
                    )
                    , child_nodes = []
                )
            ]
        )
    ]
    @pytest.mark.parametrize('expanded_node, original_player_to_act, expected', simulation_test_cases)
    def test_simulation(self, expanded_node: Node, original_player_to_act, expected):
        test_mcts = Mcts(expanded_node, self.default_mcts_decision_time)
        test_mcts.simulation(expanded_node, original_player_to_act)
        assert set([n.__str__() for n in expected]).issuperset([expanded_node.__str__()])
    
    
    # TODO !!!
    # back_propogation_test_cases = [
    #     pytest.param(
    #         default_node
    #         , Node(
    #             State(
    #                 default_board
    #                 , num_wins 
    #             )
    #         )
    #     )
    # ]
    # @pytest.mark.parametrize('inp, expected', back_propogation_test_cases)
    # def test_back_propogation(self, inp, expected):
    #     assert 1==1
    
    
    select_best_child_test_cases = [
        pytest.param(
            Mcts(
                Node(
                    State(
                        Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([
                                [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                            ])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = default_num_wins
                        , num_visits = default_num_visits
                    )
                    , parent_node = default_parent_node
                    , child_nodes = [
                        Node(
                            State(
                                Board(
                                    rows = default_rows
                                    , columns = default_columns
                                    , num_consecutive_for_win = default_num_consecutive_for_win
                                    , board_positions = np.array([
                                        [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE]]
                                        , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                        , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                                    ])
                                    , player_to_act = default_player_to_act
                                    , win_combos = default_win_combos
                                )
                                , num_wins = 0
                                , num_visits = 100
                            )
                            , parent_node = Node(
                                State(
                                    Board(
                                        rows = default_rows
                                        , columns = default_columns
                                        , num_consecutive_for_win = default_num_consecutive_for_win
                                        , board_positions = np.array([
                                            [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                            , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                            , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                                        ])
                                        , player_to_act = default_player_to_act
                                        , win_combos = default_win_combos
                                    )
                                    , num_wins = 1150
                                    , num_visits = 1300
                                )
                                , parent_node = default_parent_node
                                , child_nodes = []
                            )
                            , child_nodes = []
                        )
                        , Node(
                            State(
                                Board(
                                    rows = default_rows
                                    , columns = default_columns
                                    , num_consecutive_for_win = default_num_consecutive_for_win
                                    , board_positions = np.array([
                                        [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                        , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE]]
                                        , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                                    ])
                                    , player_to_act = default_player_to_act
                                    , win_combos = default_win_combos
                                )
                                , num_wins = 150
                                , num_visits = 200
                            )
                            , parent_node = Node(
                                State(
                                    Board(
                                        rows = default_rows
                                        , columns = default_columns
                                        , num_consecutive_for_win = default_num_consecutive_for_win
                                        , board_positions = np.array([
                                            [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                            , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                            , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                                        ])
                                        , player_to_act = default_player_to_act
                                        , win_combos = default_win_combos
                                    )
                                    , num_wins = 1150
                                    , num_visits = 1300
                                )
                                , parent_node = default_parent_node
                                , child_nodes = []
                            )
                            , child_nodes = []
                        )
                        , Node(
                            State(
                                Board(
                                    rows = default_rows
                                    , columns = default_columns
                                    , num_consecutive_for_win = default_num_consecutive_for_win
                                    , board_positions = np.array([
                                        [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                        , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                        , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE]]
                                    ])
                                    , player_to_act = default_player_to_act
                                    , win_combos = default_win_combos
                                )
                                , num_wins = 1000
                                , num_visits = 1000
                            )
                            , parent_node = Node(
                                State(
                                    Board(
                                        rows = default_rows
                                        , columns = default_columns
                                        , num_consecutive_for_win = default_num_consecutive_for_win
                                        , board_positions = np.array([
                                            [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                            , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                            , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                                        ])
                                        , player_to_act = default_player_to_act
                                        , win_combos = default_win_combos
                                    )
                                    , num_wins = 1150
                                    , num_visits = 1300
                                )
                                , parent_node = default_parent_node
                                , child_nodes = []
                            )
                            , child_nodes = []
                        )
                    ]
                )
                , mcts_decision_time = default_mcts_decision_time
            )
            , Node(
                State(
                    Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array([
                            [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                            , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                            , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE]]
                        ])
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                    , num_wins = 1000
                    , num_visits = 1000
                )
                , parent_node = Node(
                    State(
                        Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([
                                [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                            ])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 1150
                        , num_visits = 1300
                    )
                    , parent_node = []
                    , child_nodes = []
                )
                , child_nodes = []
            )
        )
    ]
    @pytest.mark.parametrize('inp, expected', select_best_child_test_cases)
    def test_select_best_child(self, inp: Mcts, expected: Node):
        assert inp.select_best_child().__str__() == expected.__str__()
    
    
    convert_best_child_to_move_test_cases = [
        pytest.param(
            Mcts(
                Node(
                    State(
                        Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([
                                [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                            ])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = default_num_wins
                        , num_visits = default_num_visits
                    )
                    , parent_node = default_parent_node
                    , child_nodes = [
                        Node(
                            State(
                                Board(
                                    rows = default_rows
                                    , columns = default_columns
                                    , num_consecutive_for_win = default_num_consecutive_for_win
                                    , board_positions = np.array([
                                        [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE]]
                                        , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                        , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                                    ])
                                    , player_to_act = default_player_to_act
                                    , win_combos = default_win_combos
                                )
                                , num_wins = default_num_wins
                                , num_visits = default_num_visits
                            )
                            , parent_node = Node(
                                State(
                                    Board(
                                        rows = default_rows
                                        , columns = default_columns
                                        , num_consecutive_for_win = default_num_consecutive_for_win
                                        , board_positions = np.array([
                                            [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                            , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                            , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                                        ])
                                        , player_to_act = default_player_to_act
                                        , win_combos = default_win_combos
                                    )
                                    , num_wins = default_num_wins
                                    , num_visits = default_num_visits
                                )
                                , parent_node = default_parent_node
                                , child_nodes = []
                            )
                            , child_nodes = []
                        )
                        , Node(
                            State(
                                Board(
                                    rows = default_rows
                                    , columns = default_columns
                                    , num_consecutive_for_win = default_num_consecutive_for_win
                                    , board_positions = np.array([
                                        [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                        , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE]]
                                        , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                                    ])
                                    , player_to_act = default_player_to_act
                                    , win_combos = default_win_combos
                                )
                                , num_wins = default_num_wins
                                , num_visits = default_num_visits
                            )
                            , parent_node = Node(
                                State(
                                    Board(
                                        rows = default_rows
                                        , columns = default_columns
                                        , num_consecutive_for_win = default_num_consecutive_for_win
                                        , board_positions = np.array([
                                            [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                            , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                            , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                                        ])
                                        , player_to_act = default_player_to_act
                                        , win_combos = default_win_combos
                                    )
                                    , num_wins = default_num_wins
                                    , num_visits = default_num_visits
                                )
                                , parent_node = default_parent_node
                                , child_nodes = []
                            )
                            , child_nodes = []
                        )
                        , Node(
                            State(
                                Board(
                                    rows = default_rows
                                    , columns = default_columns
                                    , num_consecutive_for_win = default_num_consecutive_for_win
                                    , board_positions = np.array([
                                        [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                        , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                        , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE]]
                                    ])
                                    , player_to_act = default_player_to_act
                                    , win_combos = default_win_combos
                                )
                                , num_wins = default_num_wins
                                , num_visits = default_num_visits
                            )
                            , parent_node = Node(
                                State(
                                    Board(
                                        rows = default_rows
                                        , columns = default_columns
                                        , num_consecutive_for_win = default_num_consecutive_for_win
                                        , board_positions = np.array([
                                            [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                            , [PLAYERS[default_opponent][BOARD_VALUE], PLAYERS[default_opponent][BOARD_VALUE], 0]
                                            , [PLAYERS[default_player_to_act][BOARD_VALUE], PLAYERS[default_player_to_act][BOARD_VALUE], 0]
                                        ])
                                        , player_to_act = default_player_to_act
                                        , win_combos = default_win_combos
                                    )
                                    , num_wins = default_num_wins
                                    , num_visits = default_num_visits
                                )
                                , parent_node = default_parent_node
                                , child_nodes = []
                            )
                            , child_nodes = []
                        )
                    ]
                )
                , mcts_decision_time = default_mcts_decision_time
            )
            , '2,2'
        )
    ]
    @pytest.mark.parametrize('inp, expected', convert_best_child_to_move_test_cases)
    def test_convert_best_child_to_move(self, inp, expected):
        assert inp.convert_best_child_to_move(inp.root_node.child_nodes[2]) == expected






