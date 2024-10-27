
from helpers import is_goal, get_possible_moves

def iddfs_copy(state, depth):
    def dfs(current_state, depth, current_depth=0):
        print(f"Explorando estado (cópia) na profundidade {current_depth}:")
        for row in current_state:
            print(row)
        print("")

        if depth == 0:
            return is_goal(current_state)
        if is_goal(current_state):
            return True
        for next_state in get_possible_moves(current_state):
            if dfs(next_state, depth - 1, current_depth + 1):
                return True
        return False

    for d in range(depth + 1):
        print(f"Iniciando nova profundidade máxima: {d}")
        if dfs(state, d):
            return True
    return False
