

import numpy as np
import pytest
from project.classes.board import Board
from project.classes.node import Node
from project.classes.state import State
from project.config import OPPONENT, PLAYER_1, PLAYERS
from project.win_combos import get_win_combos


class TestNode:

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
    
    
    test_add_child_nodes_test_cases = [
        pytest.param(
            default_node
            , [
                Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([[1,0,0],[0,0,0],[0,0,0]])
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
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([[0,1,0],[0,0,0],[0,0,0]])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 0
                    )
                    , parent_node = default_node
                    , child_nodes = []
                ), Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([[0,0,1],[0,0,0],[0,0,0]])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 0
                    )
                    , parent_node = default_node
                    , child_nodes = []
                ), Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([[0,0,0],[1,0,0],[0,0,0]])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 0
                    )
                    , parent_node = default_node
                    , child_nodes = []
                ), Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([[0,0,0],[0,1,0],[0,0,0]])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 0
                    )
                    , parent_node = default_node
                    , child_nodes = []
                ), Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([[0,0,0],[0,0,1],[0,0,0]])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 0
                    )
                    , parent_node = default_node
                    , child_nodes = []
                ), Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([[0,0,0],[0,0,0],[1,0,0]])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 0
                    )
                    , parent_node = default_node
                    , child_nodes = []
                ), Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([[0,0,0],[0,0,0],[0,1,0]])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 0
                    )
                    , parent_node = default_node
                    , child_nodes = []
                ), Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([[0,0,0],[0,0,0],[0,0,1]])
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
        , pytest.param(
            Node(
                state = State(
                    board = Board(
                        rows = default_rows
                        , columns = default_columns
                        , num_consecutive_for_win = default_num_consecutive_for_win
                        , board_positions = np.array([[1,-1,-1],[-1,-1,1],[1,0,0]])
                        , player_to_act = default_player_to_act
                        , win_combos = default_win_combos
                    )
                    , num_wins = 0
                    , num_visits = 0
                )
                , parent_node = Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([[1,0,-1],[-1,-1,1],[1,0,0]])
                            , player_to_act = default_opponent
                            , win_combos = default_win_combos
                        )
                        , num_wins = default_num_visits
                        , num_visits = 0
                    )
                )
                , child_nodes = []
            )
            , [
                Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([[1,-1,-1],[-1,-1,1],[1,1,0]])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 0
                    )
                    , parent_node = Node(
                        state = State(
                            board = Board(
                                rows = default_rows
                                , columns = default_columns
                                , num_consecutive_for_win = default_num_consecutive_for_win
                                , board_positions = np.array([[1,-1,-1],[-1,-1,1],[1,0,0]])
                                , player_to_act = default_player_to_act
                                , win_combos = default_win_combos
                            )
                            , num_wins = 0
                            , num_visits = 0
                        )
                        , parent_node = Node(
                            state = State(
                                board = Board(
                                    rows = default_rows
                                    , columns = default_columns
                                    , num_consecutive_for_win = default_num_consecutive_for_win
                                    , board_positions = np.array([[1,0,-1],[-1,-1,1],[1,0,0]])
                                    , player_to_act = default_opponent
                                    , win_combos = default_win_combos
                                )
                                , num_wins = default_num_visits
                                , num_visits = 0
                            )
                        )
                        , child_nodes = []
                    )
                    , child_nodes = []
                )
                , Node(
                    state = State(
                        board = Board(
                            rows = default_rows
                            , columns = default_columns
                            , num_consecutive_for_win = default_num_consecutive_for_win
                            , board_positions = np.array([[1,-1,-1],[-1,-1,1],[1,0,1]])
                            , player_to_act = default_player_to_act
                            , win_combos = default_win_combos
                        )
                        , num_wins = 0
                        , num_visits = 0
                    )
                    , parent_node = Node(
                        state = State(
                            board = Board(
                                rows = default_rows
                                , columns = default_columns
                                , num_consecutive_for_win = default_num_consecutive_for_win
                                , board_positions = np.array([[1,-1,-1],[-1,-1,1],[1,0,0]])
                                , player_to_act = default_player_to_act
                                , win_combos = default_win_combos
                            )
                            , num_wins = 0
                            , num_visits = 0
                        )
                        , parent_node = Node(
                            state = State(
                                board = Board(
                                    rows = default_rows
                                    , columns = default_columns
                                    , num_consecutive_for_win = default_num_consecutive_for_win
                                    , board_positions = np.array([[1,0,-1],[-1,-1,1],[1,0,0]])
                                    , player_to_act = default_opponent
                                    , win_combos = default_win_combos
                                )
                                , num_wins = default_num_visits
                                , num_visits = 0
                            )
                        )
                        , child_nodes = []
                    )
                    , child_nodes = []
                )
            ]
        )
    ]
    @pytest.mark.parametrize('inp, expected', test_add_child_nodes_test_cases)
    def test_add_child_nodes(self, inp: Node, expected):
        inp.add_child_nodes()
        assert [n.__str__() for n in inp.child_nodes] == [n.__str__() for n in expected]




