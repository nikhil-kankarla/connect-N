class Player:
    def __init__(self, player_num, board_value):
        self.player_num = player_num
        self.board_value = board_value
    
    def __repr__(self):
        return f'Player(player_num: {self.player_num}, board_value: {self.board_value})'

    def __str__(self):
        return f'Player(player_num: {self.player_num}, board_value: {self.board_value})'