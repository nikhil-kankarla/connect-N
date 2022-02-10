from math import sqrt
from project.win_combos import get_win_combos

# Game size
ROWS = 3
COLUMNS = 3
NUM_CONSECUTIVE_FOR_WIN = 3

# Player settings
PLAYER_1 = 'player_1'
PLAYER_2 = 'player_2'
PLAYER_NUM = 'player_num'
BOARD_VALUE = 'board_value'
BOARD_STR = 'board_string'
OPPONENT = 'opponent'
PLAYERS = {
    PLAYER_1: {
        PLAYER_NUM: 1
        , BOARD_VALUE: 1
        , BOARD_STR: 'X'
        , OPPONENT: PLAYER_2
    }
    , PLAYER_2: {
        PLAYER_NUM: 2
        , BOARD_VALUE: -1
        , BOARD_STR: 'O'
        , OPPONENT: PLAYER_1
    }
}
MCTS_PLAYER = PLAYER_2

# Gameplay input settings
MAX_INPUT_ATTEMPTS = 3

# Game status settings
PLAYER_1_WIN_STATUS = PLAYERS[PLAYER_1][BOARD_VALUE]
PLAYER_2_WIN_STATUS = PLAYERS[PLAYER_2][BOARD_VALUE]
DRAW_STATUS = 0
ONGOING_GAME_STATUS = 9

# Monte-Carlo Tree Search settings
EXPLORATION_CONSTANT = sqrt(2)

# Winning combinations of board positions
WIN_COMBOS = get_win_combos(rows = ROWS, columns = COLUMNS, num_consecutive_for_win = NUM_CONSECUTIVE_FOR_WIN)
