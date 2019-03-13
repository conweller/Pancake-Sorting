"""Contains all search algorithms"""
import pancake as pc



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
            cur_cakes.print_flip()
            visited.append(cur_cakes)
            stack = cur_cakes.next_states() + stack
