from copy import deepcopy
import numpy as np
from project.classes.board import Board
from project.classes.state import State
from project.classes.node import Node
from project.classes.mcts import Mcts
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


def human_vs_simple_ai_game():
    
    player_to_act = PLAYER_1
    simple_ai_player = PLAYER_2
    starting_board = Board(player_to_act = player_to_act)
    board = deepcopy(starting_board)
    game_status = ONGOING_GAME_STATUS
    games = {}
    
    while game_status == ONGOING_GAME_STATUS:

        if games != {}:
            print('')
        
        if board.new_game_bool():
            game_num = board.new_game_message(games)
            print(board)
        
        if player_to_act == simple_ai_player:
            print('\nSimple AI to act...')
        else:
            print(f'What move would {player_to_act} ({PLAYERS[player_to_act][BOARD_STR]}) like to play?')
            if (games == {}) and (board.new_game_bool()):
                print('Please provide an input of the form "X,Y", where X represents the row index, and Y represents the column index')
        
        input_attempt = 0
        
        if player_to_act == simple_ai_player: # simple AI's move

            state = State(board, num_wins = 0, num_visits = 0)
            node = Node(state, parent_node = None, child_nodes = [])
            mcts = Mcts(node)

            move = mcts.select_best_move()
            print(f'Simple AI chooses to play move: {move}')
        
        else: # human move
            while input_attempt < MAX_INPUT_ATTEMPTS:
                print(f'You have {MAX_INPUT_ATTEMPTS - input_attempt} attempt(s) remaining to make a valid move\n')
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
                print(f'{PLAYER_1} ({PLAYERS[PLAYER_1][BOARD_STR]}) wins\n')
                games[game_num] = game_status
                board.print_match_outcome(games)
                print('Do you want to keep playing? Hit "Enter" or answer "y" to keep playing, or answer "n" to stop playing')
                continue_playing = input()
                if (continue_playing.lower() in ['y', 'yes', '']) | (not continue_playing):
                    board = deepcopy(starting_board)
                    board.player_to_act = player_to_act
                    game_status = ONGOING_GAME_STATUS
                else:
                    board.print_match_outcome(games)
                    break
            elif game_status == PLAYER_2_WIN_STATUS:
                print(f'{PLAYER_2} ({PLAYERS[PLAYER_2][BOARD_STR]}) wins\n')
                games[game_num] = game_status
                board.print_match_outcome(games)
                print('Do you want to keep playing? Hit "Enter" or answer "y" to keep playing, or answer "n" to stop playing')
                continue_playing = input()
                if (continue_playing.lower() in ['y', 'yes', '']) | (not continue_playing):
                    board = deepcopy(starting_board)
                    board.player_to_act = player_to_act
                    game_status = ONGOING_GAME_STATUS
                else:
                    board.print_match_outcome(games)
                    break
            elif game_status == DRAW_STATUS:
                print('Game is DRAWN...\n')
                games[game_num] = game_status
                board.print_match_outcome(games)
                print('Do you want to keep playing? Hit "Enter" or answer "y" to keep playing, or answer "n" to stop playing')
                continue_playing = input()
                if (continue_playing.lower() in ['y', 'yes', '']) | (not continue_playing):
                    board = deepcopy(starting_board)
                    board.player_to_act = player_to_act
                    game_status = ONGOING_GAME_STATUS
                else:
                    board.print_match_outcome(games)
                    break


if __name__ == '__main__':
    human_vs_simple_ai_game()
