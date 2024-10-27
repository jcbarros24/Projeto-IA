
from helpers import is_goal, get_possible_moves_inplace, find_empty_tile

def iddfs_inplace(state, depth):
    def dfs(current_state, depth, row, col, current_depth=0):
        print(f"Explorando estado (in-place) na profundidade {current_depth}:")
        for row_content in current_state:
            print(row_content)
        print("")

        if depth == 0:
            return is_goal(current_state)
        if is_goal(current_state):
            return True
        for next_state in get_possible_moves_inplace(current_state, row, col):
            new_row, new_col = find_empty_tile(next_state)
            if dfs(next_state, depth - 1, new_row, new_col, current_depth + 1):
                return True
        return False

    empty_row, empty_col = find_empty_tile(state)
    for d in range(depth + 1):
        print(f"Iniciando nova profundidade máxima: {d}")
        if dfs(state, d, empty_row, empty_col):
            return True
    return False
