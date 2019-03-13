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
        flip_i: Index at which pancakes were flipped
    """

    def __init__(self, cakes, actual_cost, heuristic, flip_i):
        """Creates a PancakeState"""
        self.cakes = cakes
        self.a_cost = actual_cost
        self.heur = heuristic
        self.flip_i = flip_i

    def __str__(self):
        """Returns object string"""
        return str(self.cakes)

    def __repr__(self):
        """Returns object string"""
        return str(self)

    def __lt__(self, other):
        """Self less than other"""
        return self.to_int() > other.to_int()

    def __eq__(self, other):
        """True if lists are equal"""
        return self.cakes == other.cakes

    def to_int(self):
        """Returns the integer representation of self's pancakes"""
        return int("".join(list(map(str, self.cakes))))

    def next_states(self):
        """Returns list of all possible CakeStackStaes after 1 flip"""
        states = []
        for i in range(len(self.cakes) - 1):
            new_state = copy.deepcopy(self)
            new_state.a_cost += new_state.flip(i)
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

    def flip_string(self):
        """The string representation of the pancake stack's last flip"""
        int_string = str(self.to_int())
        flipped = int_string[self.flip_i:]
        return int_string[:self.flip_i] + '|' + flipped

    def goal(self):
        """Returns true, if we have reach the goal state"""
        return all(
            self.cakes[i] >= self.cakes[i + 1] for i in range(len(self.cakes) - 1)
        )
