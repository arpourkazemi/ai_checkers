from state import State

state = State()

while (True):
    successors = state.successor()
    for index, s in enumerate(successors):
        print(str(index) + "")
        s.print()
    choice = int(input())
    state = successors[choice]
