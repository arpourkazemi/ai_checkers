from state import State
from Minimax import minimax

# state = State(0)

# while (True):
#     successors = state.successor()
#     for index, s in enumerate(successors):
#         print(str(index) + "")
#         s.print()
#     choice = int(input())
#     state = successors[choice]
MAX, MIN = 1000, -1000

w_d = int(input("input white playes depth:"))
b_d = int(input("input black playes depth:"))

first_player_state = State()

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
