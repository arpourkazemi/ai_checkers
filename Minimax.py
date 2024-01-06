from state import State
import random
MAX, MIN = 1000, -1000


def minimax(state: 'State', depth, maximizingPlayer, alpha, beta, strength):
    successors = state.successor()
    player = state.turn
    if not maximizingPlayer:
        if state.turn == player.BLUE:
            player = player.RED
        else:
            player = player.BLUE
    if depth == strength:
        return state, state.heuristic(player)

    if maximizingPlayer:
        if len(successors) == 0:
            return state, state.heuristic(player)
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
            return state, state.heuristic(player)
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
