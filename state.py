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
        print(end="\n\n")

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
        # Index 0: Number of pawns
        # Index 1: Number of kings
        # Index 2: Number in back row
        # Index 3: Number in middle box
        # Index 4: Number in middle 2 rows, not box
        # Index 5: Number that can be taken this turn
        # Index 6: Number that are protected
        # Weights: [4, 8, 1, 2, 1.5, -3, 3]
        utility_red = [0 for i in range(7)]
        utility_blue = [0 for i in range(7)]
        for i in range(8):
            for j in range(8):
                current_cell = self.board.matrix[i][j]
                if current_cell != None:
                    if current_cell.color == Color.RED:
                        if current_cell.is_king:
                            # king
                            utility_red[1] += 1
                        else:
                            # pawn
                            utility_red[0] += 1

                        if i == 7:
                            # back row
                            utility_red[2] += 1
                            utility_red[6] += 1
                        elif i == 3 or i == 4:
                            # mid box
                            if j >= 2 and j <= 5:
                                utility_red[3] += 1
                            # non box
                            else:
                                utility_red[4] += 1
                        elif i > 0:
                            if j > 0 and j < 7:
                                if self.board.matrix[i - 1][j - 1] != None and self.board.matrix[i - 1][j - 1].color == Color.BLUE and self.board.matrix[i + 1][j + 1] == None:
                                    utility_red[5] += 1
                                if self.board.matrix[i - 1][j + 1] != None and self.board.matrix[i - 1][j + 1].color == Color.BLUE and self.board.matrix[i + 1][j - 1] == None:
                                    utility_red[5] += 1
                        elif i < 7:
                            if j == 0 or j == 7:
                                utility_red[6] += 1
                            elif (self.board.matrix[i + 1][j - 1] != None and (self.board.matrix[i + 1][j - 1].color == Color.RED or not self.board.matrix[i + 1][j - 1].is_king)) and self.board.matrix[i + 1][j + 1] != None and (self.board.matrix[i + 1][j + 1].color == Color.RED or not self.board.matrix[i + 1][j + 1].is_king):
                                utility_red[6] += 1

                    if current_cell.color == Color.BLUE:
                        if current_cell.is_king:
                            # king
                            utility_blue[1] += 1
                        else:
                            # pawn
                            utility_blue[0] += 1

                        if i == 0:
                            # back row
                            utility_blue[2] += 1
                            utility_blue[6] += 1
                        else:
                            if i == 3 or i == 4:
                                # mid box
                                if j >= 2 and j <= 5:
                                    utility_blue[3] += 1
                                # non box
                                else:
                                    utility_blue[4] += 1
                            if i < 7:
                                if j > 0 and j < 7:
                                    if self.board.matrix[i + 1][j - 1] != None and self.board.matrix[i + 1][j - 1].color == Color.RED and self.board.matrix[i - 1][j + 1] == None:
                                        utility_blue[5] += 1
                                    if self.board.matrix[i + 1][j + 1] != None and self.board.matrix[i + 1][j + 1].color == Color.RED and self.board.matrix[i - 1][j - 1] == None:
                                        utility_blue[5] += 1
                            if i > 0:
                                if j == 0 or j == 7:
                                    utility_blue[6] += 1
                                elif (self.board.matrix[i - 1][j - 1] != None and (self.board.matrix[i - 1][j - 1].color == Color.RED or not self.board.matrix[i - 1][j - 1].is_king)) and self.board.matrix[i - 1][j + 1] != None and (self.board.matrix[i - 1][j + 1].color == Color.RED or not self.board.matrix[i - 1][j + 1].is_king):
                                    utility_red[6] += 1

        weight = [4, 8, 1, 2, 1.5, -3, 3]
        sum = 0
        for i in range(7):
            if color == Color.RED:
                utility_red[i] -= utility_blue[i]
                sum += utility_red[i] * weight[i]
            else:
                utility_blue[i] -= utility_red[i]
                sum += utility_blue[i] * weight[i]
        return sum
