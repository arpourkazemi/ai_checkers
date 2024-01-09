from Color import Color
from Board import Board
from Piece import Piece
from Moves import moves, Moves
from typing import List
import copy


class State:
    def __init__(self):
        self.board = Board()
        self.turn = Color.RED
        self.red_pieces = 12
        self.blue_pieces = 12
        self.last_move = ''
        self.last_piece_moved = ''

    def print(self):
        circled = ["🅐", "🅑", "🅒", "🅓", "🅔", "🅕", "🅖", "🅗", "🅘", "🅙", "🅚", "🅛"]
        negative = ["Ⓐ", "Ⓑ", "Ⓒ", "Ⓓ", "Ⓔ", "Ⓕ", "Ⓖ", "Ⓗ", "Ⓘ", "Ⓙ", "Ⓚ", "Ⓛ"]
        for i in range(8):
            for p in range(3):
                print("  ", end='')
                for j in range(8):
                    if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                        print("\033[47m", end="")
                    else:
                        print("\033[40m", end="")
                    if (self.board.matrix[i][j] and p == 1):
                        if (self.board.matrix[i][j].color == Color.RED):
                            if (self.board.matrix[i][j].is_king):
                                print(
                                    "\033[31m  " + circled[self.board.matrix[i][j].id] + "  \033[0m", end="")
                            else:
                                print(
                                    "\033[31m  " + negative[self.board.matrix[i][j].id] + "  \033[0m", end="")
                        if (self.board.matrix[i][j].color == Color.BLUE):
                            if (self.board.matrix[i][j].is_king):
                                print(
                                    "\033[34m  " + circled[self.board.matrix[i][j].id] + "  \033[0m", end="")
                            else:
                                print(
                                    "\033[34m  " + negative[self.board.matrix[i][j].id] + "  \033[0m", end="")
                    else:
                        print("     \033[0m", end="")
                print("")
        print(end="\n")

    def legal_moves(self, piece: 'Piece'):
        legal_moves = list()
        for attr, move in vars(moves).items():
            if self.is_move_in_board(piece, move):
                if not piece.is_king:
                    if self.turn == Color.BLUE and piece.color == Color.BLUE:
                        if move == moves.TL or move == moves.TR:
                            next_coordinates_y, next_coordinates_x = self.next_coordinates(
                                piece, move)
                            if self.is_empty_cell(next_coordinates_y, next_coordinates_x):
                                legal_moves.append(move)
                    if self.turn == Color.RED and piece.color == Color.RED:
                        if move == moves.BL or move == moves.BR:
                            next_coordinates_y, next_coordinates_x = self.next_coordinates(
                                piece, move)
                            if self.is_empty_cell(next_coordinates_y, next_coordinates_x):
                                legal_moves.append(move)
                else:
                    if self.turn == Color.BLUE and piece.color == Color.BLUE:
                        next_coordinates_y, next_coordinates_x = self.next_coordinates(
                            piece, move)
                        if self.is_empty_cell(next_coordinates_y, next_coordinates_x):
                            legal_moves.append(move)
                    if self.turn == Color.RED and piece.color == Color.RED:
                        next_coordinates_y, next_coordinates_x = self.next_coordinates(
                            piece, move)
                        if self.is_empty_cell(next_coordinates_y, next_coordinates_x):
                            legal_moves.append(move)
        return legal_moves

    def legal_attacks(self, piece: 'Piece'):
        legal_attacks = list()
        for attr, attack in vars(moves).items():
            if self.is_move_in_board(piece, attack):
                if not piece.is_king:
                    if self.turn == Color.BLUE and piece.color == Color.BLUE:
                        if attack == moves.TL or attack == moves.TR:
                            next_coordinates_y, next_coordinates_x = self.next_coordinates(
                                piece, attack)
                            if self.is_opponent(next_coordinates_y, next_coordinates_x, piece.color):
                                next_next_y = next_coordinates_y + attack[0]
                                next_next_x = next_coordinates_x + attack[1]
                                if self.is_in_board(next_next_y, next_next_x) and self.is_empty_cell(next_next_y, next_next_x):
                                    legal_attacks.append(attack)
                    if self.turn == Color.RED and piece.color == Color.RED:
                        if attack == moves.BL or attack == moves.BR:
                            next_coordinates_y, next_coordinates_x = self.next_coordinates(
                                piece, attack)
                            if self.is_opponent(next_coordinates_y, next_coordinates_x, piece.color):
                                next_next_y = next_coordinates_y + attack[0]
                                next_next_x = next_coordinates_x + attack[1]
                                if self.is_in_board(next_next_y, next_next_x) and self.is_empty_cell(next_next_y, next_next_x):
                                    legal_attacks.append(attack)
                else:
                    if self.turn == Color.BLUE and piece.color == Color.BLUE:
                        next_coordinates_y, next_coordinates_x = self.next_coordinates(
                            piece, attack)
                        if self.is_opponent(next_coordinates_y, next_coordinates_x, piece.color):
                            next_next_y = next_coordinates_y + attack[0]
                            next_next_x = next_coordinates_x + attack[1]
                            if self.is_in_board(next_next_y, next_next_x) and self.is_empty_cell(next_next_y, next_next_x):
                                legal_attacks.append(attack)
                    if self.turn == Color.RED and piece.color == Color.RED:
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
        self.last_piece_moved = piece.id
        self.last_move = move
        if (piece.color == Color.BLUE and piece.y == 0) or (piece.color == Color.RED and piece.y == 7):
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
        if piece.color == Color.BLUE:
            self.red_pieces -= 1
        else:
            self.blue_pieces -= 1
        self.last_piece_moved = piece.id
        self.last_move = move
        if (piece.color == Color.BLUE and piece.y == 0) or (piece.color == Color.RED and piece.y == 7):
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
                new_state = copy.deepcopy(self)
                change_turn = True
                for new_piece in new_state.board.pieces:
                    if new_piece.color == piece.color and new_piece.id == piece.id:
                        new_state.attack(new_piece, legal_attack)
                        if len(new_state.legal_attacks(new_piece)) != 0:
                            change_turn = False
                if change_turn:
                    if self.turn == Color.BLUE:
                        new_state.turn = Color.RED
                    else:
                        new_state.turn = Color.BLUE
                next_states.append(new_state)
        if len(next_states) == 0:
            for piece in self.board.pieces:
                for legal_move in self.legal_moves(piece):
                    new_state = copy.deepcopy(self)
                    for new_piece in new_state.board.pieces:
                        if new_piece.color == piece.color and new_piece.id == piece.id:
                            new_state.move(new_piece, legal_move)
                    if self.turn == Color.BLUE:
                        new_state.turn = Color.RED
                    else:
                        new_state.turn = Color.BLUE
                    next_states.append(new_state)
        return next_states

    def heuristic(self, color: 'Color'):
        utility_red = 0
        utility_blue = 0
        for piece in self.board.pieces:
            if piece.color == Color.RED:
                utility_red += 1
                if piece.is_king:
                    utility_red += 1
                if self.turn == Color.RED and len(self.legal_attacks(piece)) != 0:
                    utility_red += 2

            if piece.color == Color.BLUE:
                utility_blue += 1
                if piece.is_king:
                    utility_blue += 1
                if self.turn == Color.BLUE and len(self.legal_attacks(piece)) != 0:
                    utility_blue += 2

        if color == Color.BLUE:
            return utility_blue - utility_red
        else:
            return utility_red - utility_blue
