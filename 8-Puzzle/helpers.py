
from copy import deepcopy

GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def find_empty_tile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_goal(state):
    return state == GOAL_STATE

def get_possible_moves(state):
    row, col = find_empty_tile(state)
    moves = []
    directions = {
        "up": (row - 1, col),
        "down": (row + 1, col),
        "left": (row, col - 1),
        "right": (row, col + 1)
    }
    for move, (new_row, new_col) in directions.items():
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = deepcopy(state)
            new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
            moves.append(new_state)
    return moves

def get_possible_moves_inplace(state, row, col):
    moves = []
    directions = {
        "up": (row - 1, col),
        "down": (row + 1, col),
        "left": (row, col - 1),
        "right": (row, col + 1)
    }
    for move, (new_row, new_col) in directions.items():
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            state[row][col], state[new_row][new_col] = state[new_row][new_col], state[row][col]
            moves.append(deepcopy(state))
            state[row][col], state[new_row][new_col] = state[new_row][new_col], state[row][col]
    return moves
