from state import State
from Minimax import minimax
from Player import Player

n_bots = int(input("Enter number of bots:"))


def print_bot_move_details(state: 'State'):
    print("bot moved piece " +
          chr(state.last_piece_moved + 65) + " to ", end="")
    if state.last_move == (-1, -1):
        print("top left")
    elif state.last_move == (-1, 1):
        print("top right")
    elif state.last_move == (1, -1):
        print("bottom right")
    elif state.last_move == (1, 1):
        print("bottom left")
    print()
    state.print()


if n_bots == 0:
    red_state = State()
    want_to_exit = False
    while (True):
        print()
        red_state.print()
        print("It's red's turn" if red_state.turn ==
              Player.RED else "It's blue's turn")
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
                for successor in red_state.successor():
                    if successor.last_piece_moved == selected_piece_id and successor.last_move == selected_move:
                        red_state = successor
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

        if red_state.blue_pieces == 0 or red_state.red_pieces == 0:
            red_state.print()
            if red_state.turn == Player.RED:
                print("player red won the game!")
            else:
                print("player red won the game!")
            break

if n_bots == 1:
    red_state = State()
    want_to_exit = False
    red_bot_strength = int(input("input bot strength:"))
    while True:
        try:
            if red_state.turn == Player.RED:
                print()
                red_state.print()
                print("It's your turn - you are red!")
                print("input a piece id and move in form of 'id' 'q|r|z|c'")
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
                for successor in red_state.successor():
                    if successor.last_piece_moved == selected_piece_id and successor.last_move == selected_move:
                        red_state = successor
                        is_valid_move = True
                        break
                if not is_valid_move:
                    print("here")
                    print("\033[31minvalid move! please try again.\033[0m")
            else:
                print()
                red_state.print()
                MAX, MIN = 1000, -1000
                red_state, new_v2 = minimax(
                    red_state, 0, True, MIN, MAX, red_bot_strength)
                print_bot_move_details(red_state)
        except:
            if want_to_exit:
                exit(0)
            else:
                print("\033[31minvalid move! please try again.\033[0m")
        if red_state.blue_pieces == 0 or red_state.red_pieces == 0:
            red_state.print()
            if red_state.turn == Player.RED:
                print("congratulations! You won the game!")
            else:
                print("you lost to our strong AI!")
            break


if n_bots == 2:
    MAX, MIN = 1000, -1000
    red_bot_strength = int(input("input red bot strength:"))
    blue_bot_strength = int(input("input blue bot strength:"))
    red_state = State()
    red_state.print()
    while (True):
        blue_state, new_v2 = minimax(
            red_state, 0, True, MIN, MAX, red_bot_strength)
        print_bot_move_details(blue_state)
        if blue_state.blue_pieces == 0 or blue_state.red_pieces == 0:
            if red_state.turn == Player.RED:
                print("bot red won the game!")
            else:
                print("bot blue won the game!")
            break
        red_state, new_v1 = minimax(
            blue_state, 0, True, MIN, MAX, blue_bot_strength)
        print_bot_move_details(red_state)
        if red_state.blue_pieces == 0 or red_state.red_pieces == 0:
            if red_state.turn == Player.RED:
                print("bot red won the game!")
            else:
                print("bot blue won the game!")
            break
