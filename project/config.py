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
WIN_STATUS = 'win_status'
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
MAX_INPUT_ATTEMPTS = 3 # number of times human is allowed to specify an invalid move before the game is shut down

# Monte-Carlo Tree Search settings
EXPLORATION_CONSTANT = 2

# Game status settings
# ! Do not change
PLAYER_1_WIN_STATUS = PLAYERS[PLAYER_1][BOARD_VALUE] # shouldn't be equal to player_2_win_status, draw_status nor ongoing_game_status
PLAYER_2_WIN_STATUS = PLAYERS[PLAYER_2][BOARD_VALUE] # # shouldn't be equal to player_1_win_status, draw_status nor ongoing_game_status
DRAW_STATUS = 0 # shouldn't be equal to player_1_win_status, player_2_win_status nor ongoing_game_status
ONGOING_GAME_STATUS = 9 # shouldn't be equal to player_1_win_status, player_2_win_status nor draw_status

# Winning combinations of board positions
WIN_COMBOS = get_win_combos(rows = ROWS, columns = COLUMNS, num_consecutive_for_win = NUM_CONSECUTIVE_FOR_WIN)

# derived inputs
PLAYERS[PLAYER_1][WIN_STATUS] = PLAYER_1_WIN_STATUS
PLAYERS[PLAYER_2][WIN_STATUS] = PLAYER_2_WIN_STATUS