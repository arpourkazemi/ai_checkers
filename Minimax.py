from state import State
from typing import List
import random
MAX, MIN = 1000, -1000
BRANCHING_FACTOR = 4


def get_heuristic(element: 'State'):
    return element.heuristic(element.turn)


def forward_pruning(successors: List['State']):
    if len(successors) > BRANCHING_FACTOR:
        successors.sort(key=get_heuristic)
        successors = successors[:BRANCHING_FACTOR]
    return successors


def minimax(state: 'State', depth, maximizing_player, alpha, beta, strength, color):
    successors = state.successor()
    # successors = forward_pruning(successors)
    if depth == strength:
        return state, state.heuristic(color)

    if maximizing_player:
        if len(successors) == 0:
            return state, state.heuristic(color)
        best = MIN
        best_state = successors[random.randint(0, len(successors) - 1)]
        for successor in successors:
            s, val = minimax(successor, depth + 1,
                             False, alpha, beta, strength, color)
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
                             True, alpha, beta, strength, color)
            best = min(best, val)
            if val < best:
                best = val
                best_state = s
            beta = min(beta, best)
            if beta <= alpha:
                break

        return best_state, best
