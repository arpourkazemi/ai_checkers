from Piece import Piece
from Color import Color
from typing import List


class Board:
    def __init__(self):
        self.pieces: List['Piece'] = list()
        self.matrix = self.new_board()

    def new_board(self):
        matrix = [[None] * 8 for i in range(8)]
        id = 0
        for y in range(3):
            for x in range(8):
                if (((x % 2 == 0) and (y % 2 != 0)) or ((x % 2 != 0) and (y % 2 == 0))):
                    new_piece = Piece(id, Color.RED, y, x)
                    id += 1
                    self.pieces.append(new_piece)
                    matrix[y][x] = new_piece
        id = 0
        for y in range(5, 8):
            for x in range(8):
                if (((x % 2 == 0) and (y % 2 != 0)) or ((x % 2 != 0) and (y % 2 == 0))):
                    new_piece = Piece(id, Color.BLUE, y, x)
                    id += 1
                    self.pieces.append(new_piece)
                    matrix[y][x] = new_piece
        return matrix
