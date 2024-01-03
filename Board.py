from Piece import Piece
from Player import Player


class Board:
    def __init__(self):
        self.matrix = self.new_board()

    def new_board(self):
        matrix = [[None] * 8 for i in range(8)]

        for x in range(8):
            for y in range(3):
                if (((x % 2 == 0) and (y % 2 != 0)) or ((x % 2 != 0) and (y % 2 == 0))):
                    matrix[y][x] = Piece(Player.WHITE)
            for y in range(5, 8):
                if (((x % 2 == 0) and (y % 2 != 0)) or ((x % 2 != 0) and (y % 2 == 0))):
                    matrix[y][x] = Piece(Player.BLACK)
        return matrix
