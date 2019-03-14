"""Contains all search algorithms"""
import copy
import heapq as hq
import pancake as pc


def dfs(cake):
    """Depth First Search approach to finding a acceptable order of flips"""
    fringe = []
    visited = []
    fringe.append(cake)
    while fringe:
        cur_cakes = fringe.pop()
        if cur_cakes.goal():
            cur_cakes.print_path(None)
            print(str(cur_cakes) + " g=" + str(cur_cakes.a_cost))
            return cur_cakes
        if cur_cakes not in visited:
            visited.append(cur_cakes)
            fringe.extend(cur_cakes.next_states())


def ucs(cake):
    """Uniform Cost Search approach to finding an optimal order of flips"""
    fringe = []
    visited = []
    fringe_push(fringe, cake.a_cost, cake)
    while fringe:
        cur_cakes = fringe_pop(fringe)
        if cur_cakes.goal():
            cur_cakes.print_path(None)
            print(str(cur_cakes) + " g=" + str(cur_cakes.a_cost))
            return cur_cakes
        if cur_cakes not in visited:
            visited.append(cur_cakes)
            for c in cur_cakes.next_states():
                fringe_push(fringe, c.a_cost, c)


def greedy(cake):
    """Greed search, using number of out of place pancakes as a heuristic"""
    sorted_list = copy.deepcopy(cake.cakes)
    sorted_list.sort(reverse=True)
    fringe = []
    visited = []
    fringe_push(fringe, cake.heuristic(sorted_list), cake)
    while fringe:
        cur_cakes = fringe_pop(fringe)
        if cur_cakes.goal():
            cur_cakes.print_path(sorted_list)
            print(
                str(cur_cakes)
                + " g="
                + str(cur_cakes.a_cost)
                + " h="
                + str(cur_cakes.heuristic(sorted_list))
            )
            return cur_cakes
        if cur_cakes not in visited:
            visited.append(cur_cakes)
            for c in cur_cakes.next_states():
                fringe_push(fringe, cur_cakes.heuristic(sorted_list), c)


def a_star(cake):
    """A star search, using number of pancakes out of place as heuristic"""
    sorted_list = copy.deepcopy(cake.cakes)
    sorted_list.sort(reverse=True)
    fringe = []
    visited = []
    fringe_push(fringe, cake.a_cost + cake.heuristic(sorted_list), cake)
    while fringe:
        cur_cakes = fringe_pop(fringe)
        if cur_cakes.goal():
            cur_cakes.print_path(sorted_list)
            print(
                str(cur_cakes)
                + " g="
                + str(cur_cakes.a_cost)
                + " h="
                + str(cur_cakes.heuristic(sorted_list))
            )
            return cur_cakes
        if cur_cakes not in visited:
            visited.append(cur_cakes)
            for c in cur_cakes.next_states():
                fringe_push(
                    fringe, cur_cakes.a_cost +
                    cur_cakes.heuristic(sorted_list), c
                )


def fringe_push(fringe, priority, cake):
    """
    Push PancakeState to the fringe, sorted by lowest priority num, then
    highest number
    """
    hq.heappush(fringe, (priority, -int(cake), cake))


def fringe_pop(fringe):
    """Get state with lowest priority num, if tie, highest number"""
    return hq.heappop(fringe)[2]
