from state import State

class Node:
    
    def __init__(self, state: State, parent_state: State):
        self.state = state
        self.parent_state = parent_state

class Tree:
    
    def __init__(self, root: Node):
        self.root = root

class MCTS:

    def __init__(self, root_state: Tree):
        self.root_state = root_state