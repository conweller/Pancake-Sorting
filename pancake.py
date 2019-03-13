"""This module contains the PancakeState class and methods"""
import copy


class PancakeState:
    """The current state of the stack of cakes

    Attributes:
        cakes:  list of integers representing pancakes, the larger the
                    integer, the larger the pancake, the bottom is the first
                    integer.
        a_cost: Actual Cost
        heur:   Heuristic value
        flip_i: Index at which pancakes were flipped to get to this state
        parent: Previous PancakeState
    """

    def __init__(self, cakes, actual_cost, heuristic):
        """Creates a PancakeState"""
        self.cakes = cakes
        self.a_cost = actual_cost
        self.heur = heuristic
        self.flip_i = None
        self.parent = None

    def __int__(self):
        """Returns the integer representation of self's pancakes"""
        return int("".join(list(map(str, self.cakes))))

    def __str__(self):
        """Returns object string"""
        return str(str(int(self)))

    def __lt__(self, other):
        """Self less than other"""
        return int(self) < int(other)

    def __eq__(self, other):
        """True if lists are equal"""
        return self.cakes == other.cakes

    def next_states(self):
        """Returns sorted list of all possible CakeStackStaes after 1 flip"""
        states = []
        for i in range(len(self.cakes) - 1):
            new_state = copy.deepcopy(self)
            new_state.a_cost += new_state.flip(i)
            new_state.parent = self
            new_state.flip_i = i
            states.append(new_state)
        states.sort()
        return states

    def flip(self, index):
        """
        Flips cakes whose indexes are greater than or equal the inputted
        index, returns the cost of the flip
        """
        flipped = self.cakes[index:]
        flipped.reverse()
        self.cakes = self.cakes[:index] + flipped
        return len(flipped)

    def print_flip(self):
        """The string representation of the pancake stack's last flip"""
        if self.parent:
            parent_string = str(self.parent)
            flipped = parent_string[self.flip_i :]
            print(
                parent_string[: self.flip_i] + "|" + flipped + " g=" + str(self.a_cost)
            )

    def goal(self):
        """Returns true, if we have reach the goal state"""
        return all(
            self.cakes[i] >= self.cakes[i + 1] for i in range(len(self.cakes) - 1)
        )
