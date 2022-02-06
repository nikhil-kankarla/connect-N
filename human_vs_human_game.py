###### Play game:
# start_board = Board()
# start_state = State(start_board)
# start_node = Node(start_state)
# start_tree = Tree(start_node)
# start_mcts = MCTS(start_tree)

import numpy as np
from classes.board import Board
from config import (
    DRAW_STATUS
    , PLAYER_1_WIN_STATUS
    , PLAYER_2_WIN_STATUS
    , ONGOING_GAME_STATUS
    , MCTS_PLAYER
    , PLAYERS
    , PLAYER_1
    , PLAYER_2
    , BOARD_STR
    , OPPONENT
    , MAX_INPUT_ATTEMPTS
)


def human_vs_human_game():
    
    player_to_act = PLAYER_1
    board = Board(player_to_act = player_to_act)
    game_status = ONGOING_GAME_STATUS
    games = {}
    
    while game_status == ONGOING_GAME_STATUS:
        
        if board.new_game_bool():
            game_num = board.new_game_message(games)
            print(board)
        
        print(f'What move would {player_to_act} ({PLAYERS[player_to_act][BOARD_STR]}) like to play?')

        if (games == {}) and (board.new_game_bool()):
            print('Please provide an input of the form "X,Y"')
            print('Note: X represents the row index, and Y represents the column index')
        
        input_attempt = 0
        while input_attempt < MAX_INPUT_ATTEMPTS:
            print(f'You have {MAX_INPUT_ATTEMPTS - input_attempt} attempt(s) remaining to make a valid move')
            move: str = input()
            input_is_valid = board.check_input_is_valid_format(move)
            if input_is_valid:
                move_is_valid = board.check_move_is_valid(move)
                if move_is_valid:
                    break
                else:
                    input_attempt += 1
            else:
                input_attempt += 1
        
        if input_attempt >= MAX_INPUT_ATTEMPTS:
            print('Too many invalid inputs')
            game_status = None
            board.print_match_outcome(games)
            return
        else:
            board.play_move(move)
            print(board)
            player_to_act = PLAYERS[player_to_act][OPPONENT]
            board.player_to_act = player_to_act
            game_status = board.check_game_status()
            if game_status == PLAYER_1_WIN_STATUS:
                print(f'{PLAYER_1} ({PLAYERS[PLAYER_1][BOARD_STR]}) wins')
                games[game_num] = game_status
                board.print_match_outcome(games)
                print('Do you want to keep playing? Answer "y" or "n"')
                continue_playing = input()
                if continue_playing.lower() in ['y', 'yes']:
                    board = Board(player_to_act = player_to_act)
                    game_status = ONGOING_GAME_STATUS
                else:
                    board.print_match_outcome(games)
                    break
            elif game_status == PLAYER_2_WIN_STATUS:
                print(f'{PLAYER_2} ({PLAYERS[PLAYER_2][BOARD_STR]}) wins')
                games[game_num] = game_status
                board.print_match_outcome(games)
                print('Do you want to keep playing? Answer "y" or "n"')
                continue_playing = input()
                if continue_playing.lower() in ['y', 'yes']:
                    board = Board(player_to_act = player_to_act)
                    game_status = ONGOING_GAME_STATUS
                else:
                    board.print_match_outcome(games)
                    break
            elif game_status == DRAW_STATUS:
                print('Game is DRAWN...')
                games[game_num] = game_status
                board.print_match_outcome(games)
                print('Do you want to keep playing? Answer "y" or "n"')
                continue_playing = input()
                if continue_playing.lower() in ['y', 'yes']:
                    board = Board(player_to_act = player_to_act)
                    game_status == ONGOING_GAME_STATUS
                else:
                    board.print_match_outcome(games)
                    break


if __name__ == '__main__':
    human_vs_human_game()
