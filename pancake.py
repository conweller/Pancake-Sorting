"""This module contains the PancakeState class and methods"""
import copy
import functools


@functools.total_ordering
class PancakeState:
    """The current state of the stack of cakes

    Attributes:
        cakes:  list of integers representing pancakes, the larger the
                    integer, the larger the pancake, the bottom is the first
                    integer.
        a_cost: Actual Cost
        flip_i: Index at which pancakes were flipped to get to this state
        parent: Previous PancakeState
    """

    def __init__(self, cakes):
        """Creates a PancakeState"""
        self.cakes = cakes
        self.a_cost = 0
        self.flip_i = len(cakes) - 1
        self.parent = None

    def __int__(self):
        """Returns the integer representation of self's pancakes"""
        return int("".join(list(map(str, self.cakes))))

    def __str__(self):
        """Returns object string"""
        return str(int(self))

    def __repr__(self):
        """Returns object string"""
        return str(int(self))

    def __lt__(self, other):
        """Self less than other"""
        return int(self) < int(other)

    def __eq__(self, other):
        """True if lists are equal"""
        return self.cakes == other.cakes

    def heuristic(self, sorted_list):
        """
        Returns the heuristic value for the pancakes state, the number of
        pancakes out of place
        """
        h = 0
        for i in range(len(self.cakes)):
            h += self.cakes[i] != sorted_list[i]
        return h

    def next_states(self):
        """
        Returns sorted list of all possible CakeStackStaes after 1 flip
        """
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

    def print_path(self):
        """
        Prints the sequence in which the pancakes are flipped according to
        the algorithm used
        """
        path = []
        path.append(self)
        cur_cakes = self
        while cur_cakes.parent:
            path.append(cur_cakes.parent)
            cur_cakes = cur_cakes.parent
            # print(cur_cakes)
        for c in reversed(path):
            c.print_flip()

    def print_path(self, sorted_list):
        """
        Prints the sequence in which the pancakes are flipped according to
        the algorithm used
        """
        path = []
        path.append(self)
        cur_cakes = self
        while cur_cakes.parent:
            path.append(cur_cakes.parent)
            cur_cakes = cur_cakes.parent
            # print(cur_cakes)
        for c in reversed(path):
            c.print_flip(sorted_list)

    def print_flip(self, sorted_list):
        """The string representation of the pancake stack's last flip"""
        if self.parent:
            parent_string = str(self.parent)
            flipped = parent_string[self.flip_i:]
            print(
                parent_string[: self.flip_i] + "|" +
                flipped + " g=" + str(self.a_cost) +
                " h=" + str(self.parent.heuristic(sorted_list))
            )


    def goal(self):
        """Returns true, if we have reach the goal state"""
        return all(
            self.cakes[i] >= self.cakes[i + 1] for i in range(len(self.cakes) - 1)
        )
