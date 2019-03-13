"""Contains all search algorithms"""
import pancake as pc

# TODO: keep track of cost


def dfs(cake):
    """Depth First Search approach to finding a acceptable order of flips"""
    stack = []
    visited = []
    stack.append(cake)
    while stack:
        cur_cakes = stack.pop()
        if cur_cakes.goal():
            cur_cakes.print_flip()
            print(cur_cakes)
            return cur_cakes
        if cur_cakes not in visited:
            cur_cakes.print_flip()
            visited.append(cur_cakes)
            stack.extend(cur_cakes.next_states())
