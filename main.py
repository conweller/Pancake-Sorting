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

# Read in Pancakes
pancakes = pc.PancakeState(list(map(int, sys.argv[1][:-1])))

search_type = {"d": search.dfs, "u": search.ucs, "g": search.greedy, "a": search.a_star}

search_type[sys.argv[1][-1]](pancakes)
