from state import State
from Minimax import minimax
from Color import Color


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


def check_end_game(state: 'State', blue_win_message="blue wins", red_win_message="red wins"):
    if len(state.successor()) == 0:
        print(blue_win_message if state.turn ==
              Color.RED else red_win_message)
        exit(0)


def player_move(state: 'State'):
    while True:
        try:
            want_to_exit = False
            inp = input()
            if inp == "exit":
                want_to_exit = True
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
            for successor in state.successor():
                if successor.last_piece_moved == selected_piece_id and successor.last_move == selected_move:
                    is_valid_move = True
                    return successor
            if not is_valid_move:
                print("\033[31minvalid move! please try again.\033[0m")
        except:
            if want_to_exit:
                exit(0)
            else:
                print("\033[31minvalid move! please try again.\033[0m")


while (True):
    n_bots = int(input("Enter number of bots:"))
    if n_bots == 0:
        state = State()
        want_to_exit = False
        while (True):
            print()
            state.print()
            check_end_game(state)
            print("It's red's turn" if state.turn ==
                  Color.RED else "It's blue's turn")
            print("input a piece id and move in form of 'id' 'q|e|z|c'")
            state = player_move(state)
            while not state:
                player_move(state)

    elif n_bots == 1:
        state = State()
        want_to_exit = False
        red_bot_strength = int(input("input bot strength:"))
        print()
        state.print()
        while True:
            if state.turn == Color.RED:
                print("It's your turn - you are red!")
                print("input a piece id and move in form of 'id' 'q|e|z|c'")
                state = player_move(state)
                print()
                state.print()
            else:
                print()
                MAX, MIN = 1000, -1000
                state, new_v2 = minimax(
                    state, 0, True, MIN, MAX, red_bot_strength, state.turn)
                print_bot_move_details(state)
            check_end_game(state)

    elif n_bots == 2:
        MAX, MIN = 1000, -1000
        red_bot_strength = int(input("input red bot strength:"))
        blue_bot_strength = int(input("input blue bot strength:"))
        state = State()
        state.print()
        while (True):
            state, new_v2 = minimax(
                state, 0, True, MIN, MAX, red_bot_strength if state.turn == Color.RED else blue_bot_strength, state.turn)
            print_bot_move_details(state)
            check_end_game(state)

    else:
        print("\033[31minvalid input! input number in range 0 and 2.\033[0m")
