###### Play game:
# start_board = Board()
# start_state = State(start_board)
# start_node = Node(start_state)
# start_tree = Tree(start_node)
# start_mcts = MCTS(start_tree)

from lib2to3.pgen2.literals import simple_escapes
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


def human_vs_simple_ai_game():
    
    player_to_act = PLAYER_1
    simple_ai_player = PLAYER_2
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
        

        if player_to_act == simple_ai_player: # simple AI's move
            # move = select_move_via_mcts(board, player_to_act, simple_ai_player)

            # 0. while time and computational resources are available, and total simulations of root node < threshold:
                # 1. Take current state as root node
                # 2. [selection] If root node has any child nodes
                    # 2.1. [selection] go down the tree by repeatedly (1) selecting a legal move, and (2) advancing to the corresponding child node,
                    #      until a node without any further children is reached. This will be called the selected node
                    # 2.2. [selection] if the selected node is a terminal node:
                        # 2.2.1. [back propogation] Update the statistics of the selected node (wins, simulations, UCB)
                        # 2.2.2. [back propogation] Update the statistics of ALL parent nodes of the selected node (wins, simulations, UCB)
                    # 2.3. [selection] If not:
                        # 2.3.1. [expansion] get list of available moves, and add these as children of the selected node 
                        # 2.3.2. [expansion] ensure each of these children are initialised with a "w" of 0, "n" of 0 and UCB of ???
                        # 2.3.3. [expansion] select a child at random
                        # 2.3.4. [simulation] continuing from the selected child node, play moves at random and repeatedly advance the game state.
                        #        until the game is finished and (a winner emerges or the game ends in a draw). No new nodes are created in this phase.
                        #        No part of this process is stored
                        # 2.3.5. [back propogation] Update the statistics of this node that was selected during expansion (wins, simulations, UCB)
                        # 2.3.6. [back propogation] Update the statistics of ALL parent nodes of the node selected during expansion

                # 3. [selection] If not:
                    # 3.1. if the root node is a terminal node (i.e. game has ended):
                        # ! 3.1.1. the game should've already ended # check this !!!!
                    # 3.2. if not:
                        # 3.2.1. [expansion] get list of available moves, and add these as children of the root
                        # 3.2.2. [expansion] ensure each of these children are initialised with a "w" of 0, "n" of 0 and UCB of ???
                        # 3.2.3. [expansion] select a child at random
                        # 3.2.4. [simulation] continuing from the selected child node, play moves at random and repeatedly advance the game state.
                        #        until the game is finished and (a winner emerges or the game ends in a draw). No new nodes are created in this phase.
                        #        No part of this process is stored
                        # 3.2.5. [back propogation] Update the statistics of this node that was selected during expansion (wins, simulations, UCB)
                        # 3.2.6. [back propogation] Update the statistics of ALL parent nodes of the node selected during expansion





                # Find available moves that can be played by the AI, and store these as child nodes of the root node
                # Determine the best leaf node to simulate
                # For each child node, simulate a random rollout, determine the outcome of the rollout, and update two properties of the child node:
                    # number of trials run for the child node
                    # number of accumulated wins for the AI, for the child node (across the number of trials that have been run for the child node)
                # Update the root node's properties:
                    # number of trials run for the root node
                    # number of accumulated wins for the AI, for the root node (across the number of trials that have been run for the root node)
                # 

            pass
        
        else: # human move
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
    human_vs_simple_ai_game()
