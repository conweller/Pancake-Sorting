"""Contains all search algorithms"""
import pancake as pc

# TODO Need print statements and docstrings


def dfs(cake):
    """Depth First Search approach to finding a acceptable order of flips"""
    stack = []
    visited = []
    stack.append(cake)
    while stack:
        cur_cakes = stack.pop()
        if cur_cakes.goal():
            return cur_cakes
        if cur_cakes not in visited:
            print(cur_cakes)
            visited.append(cur_cakes)
            stack.extend(cur_cakes.next_states())
