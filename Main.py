from state import State

state = State()
state.print()
# state.is_in_board(state.board.pieces[0], Move.TL)
# print(state.current_coordinates(state.board.pieces[12]))
# print(state.board.pieces[12].color)
# for i in range(24):
#     for legal_move in state.legal_moves(state.board.pieces[i]):
#         print(legal_move)
#         print(i)
#         print(state.board.pieces[i].color)
#         print(state.board.pieces[i].x)
#         print(state.board.pieces[i].y)

print(state.board.pieces[13].color)
print(state.board.pieces[13].y)
print(state.board.pieces[13].x)

for legal_move in state.legal_moves(state.board.pieces[13]):
    print(legal_move)
