"""Contains all search algorithms"""
import pancake as pc
import heapq as hq

# TODO: keep track of cost


def dfs(cake):
    """Depth First Search approach to finding a acceptable order of flips"""
    fringe = []
    visited = []
    fringe.append(cake)
    while fringe:
        cur_cakes = fringe.pop()
        if cur_cakes.goal():
            cur_cakes.print_path()
            print(str(cur_cakes) + " g=" + str(cur_cakes.a_cost))
            return cur_cakes
        if cur_cakes not in visited:
            visited.append(cur_cakes)
            fringe.extend(cur_cakes.next_states())


def ufs(cake):
    """Uniform Cost Search approach to findin an optimal order of flips"""
    fringe = []
    visited = []
    fringe_push(fringe, cake.a_cost, cake)
    while fringe:
        cur_cakes = fringe_pop(fringe)
        if cur_cakes.goal():
            cur_cakes.print_path()
            print(str(cur_cakes) + " g=" + str(cur_cakes.a_cost))
            return cur_cakes
        if cur_cakes not in visited:
            for c in cur_cakes.next_states():
                fringe_push(fringe, c.a_cost, c)


def greedy(cake):
    return None


def a_star(cake):
    return None


def fringe_push(fringe, priority, cake):
    """
    Push PancakeState to the fringe, sorted by lowest priority num, then highest 
    number
    """
    hq.heappush(fringe, (priority, -int(cake), cake))


def fringe_pop(fringe):
    """Get state with lowest priority num, if tie, highest number"""
    return hq.heappop(fringe)[2]
