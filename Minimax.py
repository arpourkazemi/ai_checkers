from state import State
from Color import Color
import random
MAX, MIN = 1000, -1000
BRANCHING_FACTOR = 4


def get_heuristic(element):
    return element.heuristic(element.turn)


def minimax(state: 'State', depth, maximizing_player, alpha, beta, strength):
    successors = state.successor()
    if len(successors) > BRANCHING_FACTOR:
        successors.sort(key=get_heuristic, reverse=True)
        successors = successors[:BRANCHING_FACTOR]
    color: 'Color' = state.turn
    if not maximizing_player:
        if state.turn == color.BLUE:
            color = color.RED
        else:
            color = color.BLUE
    if depth == strength:
        return state, state.heuristic(color)

    if maximizing_player:
        if len(successors) == 0:
            return state, state.heuristic(color)
        best = MIN
        best_state = successors[random.randint(0, len(successors) - 1)]
        for successor in successors:
            s, val = minimax(successor, depth + 1,
                             False, alpha, beta, strength)
            best = max(best, val)
            if val > best:
                best = val
                best_state = s
            alpha = max(alpha, best)
            if beta <= alpha:
                break

        return best_state, best

    else:
        if len(successors) == 0:
            return state, state.heuristic(color)
        best = MAX
        best_state = successors[random.randint(0, len(successors) - 1)]
        for successor in successors:
            s, val = minimax(successor, depth + 1,
                             True, alpha, beta, strength)
            best = min(best, val)
            if val < best:
                best = val
                best_state = s
            beta = min(beta, best)
            if beta <= alpha:
                break

        return best_state, best
