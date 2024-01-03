from Piece import Piece
from Player import Player
from typing import List


class Board:
    def __init__(self):
        self.pieces: List['Piece'] = list()
        self.matrix = self.new_board()

    def new_board(self):
        matrix = [[None] * 8 for i in range(8)]

        for y in range(3):
            for x in range(8):
                if (((x % 2 == 0) and (y % 2 != 0)) or ((x % 2 != 0) and (y % 2 == 0))):
                    newPiece = Piece(Player.WHITE, y, x)
                    self.pieces.append(newPiece)
                    matrix[y][x] = newPiece
        for y in range(5, 8):
            for x in range(8):
                if (((x % 2 == 0) and (y % 2 != 0)) or ((x % 2 != 0) and (y % 2 == 0))):
                    newPiece = Piece(Player.BLACK, y, x)
                    self.pieces.append(newPiece)
                    matrix[y][x] = newPiece
        return matrix
