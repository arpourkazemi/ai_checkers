from state import State
from Minimax import minimax
from Player import Player

n_bots = int(input("Enter number of bots:"))


if n_bots == 0:
    first_player_state = State()
    want_to_exit = False
    while (True):
        print()
        first_player_state.print()
        print("It's red's turn" if first_player_state.turn ==
              Player.WHITE else "It's blue's turn")
        print("input a piece id and move in form of 'id' 'q|r|z|c'")
        while True:
            try:
                inp = input()
                if inp == "exit":
                    want_to_exit = True
                    exit(0)
                selected_piece_char, selected_move = inp.lower().split()
                selected_piece_id = ord(selected_piece_char) - 97
                if selected_move == "q":
                    selected_move = (-1, -1)
                elif selected_move == "e":
                    selected_move = (-1, 1)
                elif selected_move == "z":
                    selected_move = (1, -1)
                elif selected_move == "c":
                    selected_move = (1, 1)
                is_valid_move = False
                for successor in first_player_state.successor():
                    if successor.last_piece_moved == selected_piece_id and successor.last_move == selected_move:
                        first_player_state = successor
                        is_valid_move = True
                        break
                if not is_valid_move:
                    print("\033[31minvalid move! please try again.\033[0m")
                else:
                    break
            except:
                if want_to_exit:
                    exit(0)
                else:
                    print("\033[31minvalid move! please try again.\033[0m")
        if first_player_state.white_pieces == 0 or first_player_state.black_pieces == 0:
            break


if n_bots == 2:
    MAX, MIN = 1000, -1000
    w_d = int(input("input white playes depth:"))
    b_d = int(input("input black playes depth:"))
    first_player_state = State()
    first_player_state.print()
    while (True):
        second_player_state, new_v2 = minimax(
            first_player_state, 0, True, MIN, MAX, w_d)
        second_player_state.print()
        if second_player_state.white_pieces == 0 or second_player_state.black_pieces == 0:
            break
        first_player_state, new_v1 = minimax(
            second_player_state, 0, True, MIN, MAX, b_d)
        first_player_state.print()
        if first_player_state.white_pieces == 0 or first_player_state.black_pieces == 0:
            break
