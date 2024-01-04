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
        print("  " + ((12*4+1)*"-"))
        for i in range(8):
            print(f"  ", end='')
            for j in range(8):
                if (self.board.matrix[i][j]):
                    print("| ", end='')
                    if (self.board.matrix[i][j].isKing):
                        print('\033[32m', end='')
                    if (self.board.matrix[i][j].color == Player.WHITE):
                        print("w", end='')
                        print(str(self.board.matrix[i][j].id) + " ", end='')
                        if self.board.matrix[i][j].id < 10:
                            print(" ", end="")
                    if (self.board.matrix[i][j].color == Player.BLACK):
                        print("b", end='')
                        print(str(self.board.matrix[i][j].id) + " ", end='')
                        if self.board.matrix[i][j].id < 10:
                            print(" ", end="")
                    print('\033[m', end='')
                else:
                    print(f"| {'   '} ", end='')
            print("| ")
            print("  " + ((12*4+1)*"-"))

    def legal_moves(self, piece: 'Piece'):
        legal_moves = list()
        for attr, move in vars(moves).items():
            if self.is_move_in_board(piece, move):
                if not piece.isKing:
                    if self.turn == Player.BLACK and piece.color == Player.BLACK:
                        if move == moves.TL or move == moves.TR:
                            next_coordinates_y, next_coordinates_x = self.next_coordinates(
                                piece, move)
                            if self.is_empty_cell(next_coordinates_y, next_coordinates_x):
                                legal_moves.append(move)
                    if self.turn == Player.WHITE and piece.color == Player.WHITE:
                        if move == moves.BL or move == moves.BR:
                            next_coordinates_y, next_coordinates_x = self.next_coordinates(
                                piece, move)
                            if self.is_empty_cell(next_coordinates_y, next_coordinates_x):
                                legal_moves.append(move)
                else:
                    if self.turn == Player.BLACK and piece.color == Player.BLACK:
                        next_coordinates_y, next_coordinates_x = self.next_coordinates(
                            piece, move)
                        if self.is_empty_cell(next_coordinates_y, next_coordinates_x):
                            legal_moves.append(move)
                    if self.turn == Player.WHITE and piece.color == Player.WHITE:
                        next_coordinates_y, next_coordinates_x = self.next_coordinates(
                            piece, move)
                        if self.is_empty_cell(next_coordinates_y, next_coordinates_x):
                            legal_moves.append(move)
        return legal_moves

    def legal_attacks(self, piece: 'Piece'):
        legal_attacks = list()
        for attr, attack in vars(moves).items():
            if self.is_move_in_board(piece, attack):
                if not piece.isKing:
                    if self.turn == Player.BLACK and piece.color == Player.BLACK:
                        if attack == moves.TL or attack == moves.TR:
                            next_coordinates_y, next_coordinates_x = self.next_coordinates(
                                piece, attack)
                            if self.is_opponent(next_coordinates_y, next_coordinates_x, piece.color):
                                next_next_y = next_coordinates_y + attack[0]
                                next_next_x = next_coordinates_x + attack[1]
                                if self.is_in_board(next_next_y, next_next_x) and self.is_empty_cell(next_next_y, next_next_x):
                                    legal_attacks.append(attack)
                    if self.turn == Player.WHITE and piece.color == Player.WHITE:
                        if attack == moves.BL or attack == moves.BR:
                            next_coordinates_y, next_coordinates_x = self.next_coordinates(
                                piece, attack)
                            if self.is_opponent(next_coordinates_y, next_coordinates_x, piece.color):
                                next_next_y = next_coordinates_y + attack[0]
                                next_next_x = next_coordinates_x + attack[1]
                                if self.is_in_board(next_next_y, next_next_x) and self.is_empty_cell(next_next_y, next_next_x):
                                    legal_attacks.append(attack)
                else:
                    if self.turn == Player.BLACK and piece.color == Player.BLACK:
                        next_coordinates_y, next_coordinates_x = self.next_coordinates(
                            piece, attack)
                        if self.is_opponent(next_coordinates_y, next_coordinates_x, piece.color):
                            next_next_y = next_coordinates_y + attack[0]
                            next_next_x = next_coordinates_x + attack[1]
                            if self.is_in_board(next_next_y, next_next_x) and self.is_empty_cell(next_next_y, next_next_x):
                                legal_attacks.append(attack)
                    if self.turn == Player.WHITE and piece.color == Player.WHITE:
                        next_coordinates_y, next_coordinates_x = self.next_coordinates(
                            piece, attack)
                        if self.is_opponent(next_coordinates_y, next_coordinates_x, piece.color):
                            next_next_y = next_coordinates_y + attack[0]
                            next_next_x = next_coordinates_x + attack[1]
                            if self.is_in_board(next_next_y, next_next_x) and self.is_empty_cell(next_next_y, next_next_x):
                                legal_attacks.append(attack)
        return legal_attacks

    def move(self, piece: 'Piece', move: 'Moves'):
        self.board.matrix[piece.y][piece.x] = None
        piece.y, piece.x = self.next_coordinates(piece, move)
        self.board.matrix[piece.y][piece.x] = piece
        if (piece.color == Player.BLACK and piece.y == 0) or (piece.color == Player.WHITE and piece.y == 7):
            piece.crown()

    def attack(self, piece: 'Piece', move: 'Moves'):
        new_y = piece.y + 2 * move[0]
        new_x = piece.x + 2 * move[1]
        opponent = self.board.matrix[piece.y + move[0]][piece.x + move[1]]
        for p in self.board.pieces:
            if p.id == opponent.id and p.color == opponent.color:
                self.board.pieces.remove(p)
        self.board.matrix[piece.y][piece.x] = None
        self.board.matrix[piece.y + move[0]][piece.x + move[1]] = None
        self.board.matrix[new_y][new_x] = piece
        piece.y = new_y
        piece.x = new_x
        if (piece.color == Player.BLACK and piece.y == 0) or (piece.color == Player.WHITE and piece.y == 7):
            piece.crown()

    def is_empty_cell(self, y, x):
        if self.board.matrix[y][x] == None:
            return True
        return False

    def is_opponent(self, y, x, color):
        if not self.board.matrix[y][x] == None and self.board.matrix[y][x].color != color:
            return True
        return False

    def is_in_board(self, y, x):
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return True
        return False

    def is_move_in_board(self, piece: 'Piece', move: 'Moves'):
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
            for legal_attack in self.legal_attacks(piece):
                newState = copy.deepcopy(self)
                for new_piece in newState.board.pieces:
                    if new_piece.color == piece.color and new_piece.id == piece.id:
                        newState.attack(new_piece, legal_attack)
                if self.turn == Player.BLACK:
                    newState.turn = Player.WHITE
                else:
                    newState.turn = Player.BLACK
                next_states.append(newState)
        if len(next_states) == 0:
            for piece in self.board.pieces:
                for legal_attack in self.legal_moves(piece):
                    newState = copy.deepcopy(self)
                    for new_piece in newState.board.pieces:
                        if new_piece.color == piece.color and new_piece.id == piece.id:
                            newState.move(new_piece, legal_attack)
                    if self.turn == Player.BLACK:
                        newState.turn = Player.WHITE
                    else:
                        newState.turn = Player.BLACK
                    next_states.append(newState)
        return next_states

    def heuristic(self, player: 'Player'):
        utility = 0
        for piece in self.board.pieces:
            if piece.color == player:
                if piece.isKing:
                    utility += 1
                utility += 1
            else:
                if piece.isKing:
                    utility -= 1
                utility -= 1
