"""
This module reads system input and executes the corresponding search algorithm
to find an order in which to flip the pancakes. It performs the search
algorithm with the command line arguments if given, otherwise, it prompts the
user to enter input for it to search. Input Should be given in the form of
four digits and 1 character (####X), where the first digit indicates the ID of
the bottom pancake, second indicates the second lowest, etc, and the last
character would be any of "d", "u", "g" and "a", where:
    - "d" refers to Depth-First Search (DFS)
    - "u" refers to Uniform-Cost Search (UCS)
    - "g" refers to Greedy Search
    - "a" refers to A* search
"""
import sys
import pancake as pc
import search


SEARCH_TYPE = {"d": search.dfs, "u": search.ucs,
               "g": search.greedy, "a": search.a_star}


def prompt():
    """
    Prompt the user to enter input, and then performs the corresponding search
    algorith using that input
    """
    user_input = input("Enter four digits an one charcter (####X):\n")
    assert len(user_input) == 5
    assert user_input[:-1].isdigit()
    assert user_input[-1] in ["d", "u", "g", "a"]
    SEARCH_TYPE[user_input[-1]
                ](pc.PancakeState(list(map(int, user_input[:-1]))))


if len(sys.argv) > 1:
    assert len(sys.argv[1]) == 5
    assert sys.argv[1][:-1].isdigit()
    assert sys.argv[1][-1] in ["d", "u", "g", "a"]
    SEARCH_TYPE[sys.argv[1][-1]](
        pc.PancakeState(list(map(int, sys.argv[1][:-1])))
    )

else:
    prompt()
