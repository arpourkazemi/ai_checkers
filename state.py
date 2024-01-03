from Player import Player
from Board import Board


class State:
    def __init__(self):
        self.board = Board()
        self.turn = Player.WHITE

    def print(self):
        print("  " + ((8*4+1)*"-"))
        for i in range(8):
            print(f"  ", end='')
            for j in range(8):
                if (self.board.matrix[i][j]):
                    if (self.board.matrix[i][j].color == Player.WHITE):
                        print(f"| {'w'} ", end='')
                    if (self.board.matrix[i][j].color == Player.BLACK):
                        print(f"| {'b'} ", end='')
                else:
                    print(f"| {' '} ", end='')
            print("| ")
            print("  " + ((8*4+1)*"-"))
