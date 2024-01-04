# Python3 program to demonstrate
# working of Alpha-Beta Pruning

# Initial values of Alpha and Beta
from state import State
import random
MAX, MIN = 1000, -1000

# Returns optimal value for current player
# (Initially called for root and maximizer)


def minimax(state: 'State', depth, maximizingPlayer, alpha, beta, strength):
    successors = state.successor()
    player = state.turn
    if not maximizingPlayer:
        if state.turn == player.BLACK:
            player = player.WHITE
        else:
            player = player.BLACK
    if depth == strength:
        return state, state.heuristic(player)

    if maximizingPlayer:
        if len(successors) == 0:
            return state, state.heuristic(player)
        best = MIN
        best_state = successors[random.randint(0, len(successors) - 1)]
        # Recur for left and right children
        for successor in successors:
            s, val = minimax(successor, depth + 1,
                             False, alpha, beta, strength)
            best = max(best, val)
            if val > best:
                best = val
                best_state = s
            alpha = max(alpha, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best_state, best

    else:
        if len(successors) == 0:
            return state, state.heuristic(player)
        best = MAX
        best_state = successors[random.randint(0, len(successors) - 1)]
        # Recur for left and
        # right children
        for successor in successors:
            s, val = minimax(successor, depth + 1,
                             True, alpha, beta, strength)
            best = min(best, val)
            if val < best:
                best = val
                best_state = s
            beta = min(beta, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best_state, best
