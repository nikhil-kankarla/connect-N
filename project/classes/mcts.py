from copy import deepcopy
import random
from project.classes.node import Node


class Mcts:
    
    def __init__(self, root_node: Node):
        self.root_node = root_node
    
    
    def select_best_move(self):
        # self.selection()
        # self.expansion()
        # self.simulation()
        # self.back_propogation()

        # 0. while time and computational resources are available, and total simulations of root node < threshold:
        # 1. Take current state as root node
        # 2. [selection] If root node has any possible child nodes
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
        
        NotImplemented
    
    
    def selection(self):
        
        selected_node = self.root_node
        if selected_node.child_nodes == []:
            if selected_node.node_is_terminal():
                # ! The game should've already ended # check this !!!!
                print("Something's gone wrong... Check the code in the selection phase of MCTS")
                return self
            else:
                return self
        else:
            child_nodes = deepcopy(selected_node.child_nodes)
            while child_nodes != []:
                max_ucb = max(child_nodes, key= lambda x: x.state.calculate_ucb())
                max_ucb_nodes = [child_node for child_node in child_nodes if child_node.state.calculate_ucb() == max_ucb]
                selected_node = random.choice(max_ucb_nodes)
            
            return selected_node
    
    
    def expansion(self):
        return
    
    
    def simulation(self):
        return
    
    
    def back_propogation(self):
        return
