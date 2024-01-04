from state import State

state = State()

# for s in state.successor()[1].successor()[0].successor()[0].successor():
#     s.print()


while (True):
    successors = state.successor()
    for index, s in enumerate(successors):
        print(str(index) + "")
        s.print()
    choice = int(input())
    state = successors[choice]
