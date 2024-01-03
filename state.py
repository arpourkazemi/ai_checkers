from Player import Player
from Board import Board
from Piece import Piece
from Moves import moves, Moves
from typing import List
import copy


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

    def legal_moves(self, piece: 'Piece'):
        legal_moves = list()
        for attr, move in vars(moves).items():
            if self.is_in_board(piece, move):
                if not piece.isKing:
                    if self.turn == Player.BLACK:
                        if move == moves.TL or move == moves.TR:
                            if self.is_empty_cell(self.next_coordinates(piece, move)[0], self.next_coordinates(piece, move)[1]):
                                legal_moves.append(move)
                    if self.turn == Player.WHITE:
                        if move == moves.BL or move == moves.BR:
                            if self.is_empty_cell(self.next_coordinates(piece, move)[0], self.next_coordinates(piece, move)[1]):
                                legal_moves.append(move)
        return legal_moves

    def move(self, piece: 'Piece', move: 'Moves'):
        piece.y, piece.x = self.next_coordinates(piece, move)

    def is_empty_cell(self, y, x):
        if self.board.matrix[y][x] == None:
            return True
        return False

    def is_in_board(self, piece: 'Piece', move: 'Moves'):
        next_x, next_y = self.next_coordinates(piece, move)
        if next_x >= 0 and next_x < 8 and next_y >= 0 and next_y < 8:
            return True
        return False

    def next_coordinates(self, piece: 'Piece', move: 'Moves'):
        ydiff, xdiff = move
        return piece.y + ydiff, piece.x + xdiff

    def current_coordinates(self, piece: 'Piece'):
        return piece.y, piece.x

    def successor(self) -> List['State']:
        next_states = list()
        for piece in self.board.pieces:
            if piece.color == self.turn:
                for legal_move in self.legal_moves(piece):
                    newState = copy.deepcopy(self)
                    newState.move(piece, legal_move)
                    if newState.turn is Player.BLACK:
                        newState.turn = Player.WHITE
                    else:
                        newState.turn = Player.BLACK
                    next_states.append(newState)
        return next_states
