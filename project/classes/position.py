class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column
    
    def __repr__(self):
        return f'Position({self.row}, {self.column})'

    def __str__(self):
        return str([self.row, self.column])