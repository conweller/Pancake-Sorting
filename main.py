"""
This module reads system input and executes the corresponding search
algorithm
"""
import sys
import pancake as pc
import search

# Argument should be 4 ints and a char concatenated
assert len(sys.argv) == 2
assert len(sys.argv[1]) == 5
assert sys.argv[1][:-1].isdigit()
assert sys.argv[1][-1] in ["d", "u", "g", "a"]


SEARCH_TYPE = {"d": search.dfs, "u": search.ucs,
               "g": search.greedy, "a": search.a_star}

SEARCH_TYPE[sys.argv[1][-1]](
        pc.PancakeState(list(map(int, sys.argv[1][:-1])))
        )
