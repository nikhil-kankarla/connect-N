from math import sqrt
from project.classes.position import Position

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
def get_win_combos(rows = ROWS, columns = COLUMNS, num_consecutive_for_win = NUM_CONSECUTIVE_FOR_WIN):

    # LEFT = 'left'
    RIGHT = 'right'
    # UP = 'up'
    DOWN = 'down'
    # UP_LEFT = 'up_left'
    # UP_RIGHT = 'up_right'
    DOWN_LEFT = 'down_left'
    DOWN_RIGHT = 'down_right'

    TOP_ROW_INDX = 'top_row_indx'
    BOTTOM_ROW_INDX = 'bottom_row_indx'
    LEFT_COLUMN_INDX = 'left_column_indx'
    RIGHT_COLUMN_INDX = 'right_column_indx'

    def is_in_outer_perimeter(outer_perimeter_indices, row, column):
        return (
            (row in [outer_perimeter_indices[TOP_ROW_INDX], outer_perimeter_indices[BOTTOM_ROW_INDX]]) or 
            (column in [outer_perimeter_indices[LEFT_COLUMN_INDX], outer_perimeter_indices[RIGHT_COLUMN_INDX]])
        )
    
    def get_directions_to_check_for_position(position: Position, rows = rows, columns = columns, num_consecutive_for_win = num_consecutive_for_win):
        position_row = position.row
        position_column = position.column

        directions_to_check_for_position = []
        # Add directions based on position
        # - for positions that are num_consecutive_for_win away from right of board, you can check to the right
        # - for positions that are num_consecutive_for_win away from bottom of board, you can check downwards
        # - for positions that are num_consecutive_for_win away from bottom AND right of board, you can check downw-right diagonal
        # - for positions that are num_consecutive_for_win away from bottomm AND left of board, you can down-left diagonal
        if (columns - position_column) >= num_consecutive_for_win:
            directions_to_check_for_position.append(RIGHT)
        if (rows - position_row) >= num_consecutive_for_win:
            directions_to_check_for_position.append(DOWN)
        if (RIGHT in directions_to_check_for_position) and (DOWN in directions_to_check_for_position):
            directions_to_check_for_position.append(DOWN_RIGHT)
        if (DOWN in directions_to_check_for_position) and ((position_column + 1) >= num_consecutive_for_win):
            directions_to_check_for_position.append(DOWN_LEFT)

        return directions_to_check_for_position
    
    def get_win_combo(position: Position, direction, num_consecutive_for_win = num_consecutive_for_win):
        
        win_combo = []
        for n in range(num_consecutive_for_win):
            if direction == RIGHT:
                win_combo.append(Position(position.row, position.column + n))
            if direction == DOWN:
                win_combo.append(Position(position.row + n, position.column))
            if direction == DOWN_RIGHT:
                win_combo.append(Position(position.row + n, position.column + n))
            if direction == DOWN_LEFT:
                win_combo.append(Position(position.row + n, position.column - n))
        
        return win_combo

    win_combos = []
    outer_perimeter_indices = {
        TOP_ROW_INDX: 0
        , BOTTOM_ROW_INDX: rows - 1
        , LEFT_COLUMN_INDX: 0
        , RIGHT_COLUMN_INDX: columns - 1
    }

    while (
        ((outer_perimeter_indices[BOTTOM_ROW_INDX] - outer_perimeter_indices[TOP_ROW_INDX]) > 1) and
        ((outer_perimeter_indices[RIGHT_COLUMN_INDX] - outer_perimeter_indices[LEFT_COLUMN_INDX]))
    ):

        outer_perimeter_positions = []
        for row in range(outer_perimeter_indices[TOP_ROW_INDX], outer_perimeter_indices[BOTTOM_ROW_INDX] + 1):
            for column in range(outer_perimeter_indices[LEFT_COLUMN_INDX], outer_perimeter_indices[RIGHT_COLUMN_INDX] + 1):
                if is_in_outer_perimeter(outer_perimeter_indices, row, column):
                    outer_perimeter_positions.append(Position(row, column))

        for position in outer_perimeter_positions:
            directions_to_check_for_position = get_directions_to_check_for_position(position, rows, columns)
            for direction in directions_to_check_for_position:
                win_combo = get_win_combo(position, direction, num_consecutive_for_win) # list of tuples
                win_combos.append(win_combo)

        # change outer perimeter to largest inner loop
        outer_perimeter_indices[TOP_ROW_INDX] += 1
        outer_perimeter_indices[BOTTOM_ROW_INDX] -= 1
        outer_perimeter_indices[LEFT_COLUMN_INDX] += 1
        outer_perimeter_indices[RIGHT_COLUMN_INDX] -= 1

    win_combos_declassed = []
    # Convert from list of list of Positions to list of list of tuples
    for win_combo in win_combos:
        win_combos_declassed.append([(win_position.row, win_position.column) for win_position in win_combo])

    return win_combos_declassed

WIN_COMBOS = get_win_combos()
