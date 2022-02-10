import pytest
from project.classes.position import Position

def get_win_combos(rows = 3, columns = 3, num_consecutive_for_win = 3):

    RIGHT = 'right'
    DOWN = 'down'
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


square_board_and_num_consecutive_test_cases = [
    pytest.param(
        3
        , [
            [(0, 0), (0, 1), (0, 2)]
            , [(0, 0), (1, 0), (2, 0)]
            , [(0, 0), (1, 1), (2, 2)]
            , [(0, 1), (1, 1), (2, 1)]
            , [(0, 2), (1, 2), (2, 2)]
            , [(0, 2), (1, 1), (2, 0)]
            , [(1, 0), (1, 1), (1, 2)]
            , [(2, 0), (2, 1), (2, 2)]
        ]
    )
    , pytest.param(
        4
        , [
            [(0, 0), (0, 1), (0, 2), (0, 3)]
            , [(0, 0), (1, 0), (2, 0), (3, 0)]
            , [(0, 0), (1, 1), (2, 2), (3, 3)]
            , [(0, 1), (1, 1), (2, 1), (3, 1)]
            , [(0, 2), (1, 2), (2, 2), (3, 2)]
            , [(0, 3), (1, 3), (2, 3), (3, 3)]
            , [(0, 3), (1, 2), (2, 1), (3, 0)]
            , [(1, 0), (1, 1), (1, 2), (1, 3)]
            , [(2, 0), (2, 1), (2, 2), (2, 3)]
            , [(3, 0), (3, 1), (3, 2), (3, 3)]
        ]
    )
]
@pytest.mark.parametrize('inp, expected', square_board_and_num_consecutive_test_cases)
def test_square_board_and_num_consecutive_win_combos(inp, expected):
    assert get_win_combos(rows=inp, columns=inp, num_consecutive_for_win=inp) == expected


general_board_size_and_num_consecutive_test_cases = [
    pytest.param(
        3
        , 2
        , 2
        , [
            [(0, 0), (0, 1)]
            , [(0, 0), (1, 0)]
            , [(0, 0), (1, 1)]
            , [(0, 1), (1, 1)]
            , [(0, 1), (1, 0)]
            , [(1, 0), (1, 1)]
            , [(1, 0), (2, 0)]
            , [(1, 0), (2, 1)]
            , [(1, 1), (2, 1)]
            , [(1, 1), (2, 0)]
            , [(2, 0), (2, 1)]
        ]
    )
    , pytest.param(
        4
        , 5
        , 4
        , [
            [(0, 0), (0, 1), (0, 2), (0, 3)]
            , [(0, 0), (1, 0), (2, 0), (3, 0)]
            , [(0, 0), (1, 1), (2, 2), (3, 3)]
            , [(0, 1), (0, 2), (0, 3), (0, 4)]
            , [(0, 1), (1, 1), (2, 1), (3, 1)]
            , [(0, 1), (1, 2), (2, 3), (3, 4)]
            , [(0, 2), (1, 2), (2, 2), (3, 2)]
            , [(0, 3), (1, 3), (2, 3), (3, 3)]
            , [(0, 3), (1, 2), (2, 1), (3, 0)]
            , [(0, 4), (1, 4), (2, 4), (3, 4)]
            , [(0, 4), (1, 3), (2, 2), (3, 1)]
            , [(1, 0), (1, 1), (1, 2), (1, 3)]
            , [(2, 0), (2, 1), (2, 2), (2, 3)]
            , [(3, 0), (3, 1), (3, 2), (3, 3)]
            , [(3, 1), (3, 2), (3, 3), (3, 4)]
        ]
    )
]
@pytest.mark.parametrize('r, c, n, expected', general_board_size_and_num_consecutive_test_cases)
def test_general_board_size_and_num_consecutive_win_combos(r, c, n, expected):
    assert get_win_combos(rows=r, columns=c, num_consecutive_for_win=n) == expected
