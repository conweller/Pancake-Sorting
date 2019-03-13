"""This module contains the StackState class and methods"""
import copy



class StackState:
    """The current state of the stack of cakes

    Attributes:
        cakes:   list of integers representing pancakes, the larger the
                    integer, the larger the pancake, the bottom is the first
                    integer.
    """

    def __init__(self, cakes):
        """Creates a StackState"""
        self.cakes = cakes

    def __str__(self):
        """Returns object string"""
        return str(self.cakes)

    def __repr__(self):
        """Returns object string"""
        return str(self)

    def next_states(self):
        """Returns list of all possible StackStaes after 1 flip"""
        states = []
        for i in range(len(self.cakes)-1):
            new_state = copy.deepcopy(self)
            new_state.flip(i)
            states.append(new_state)
        return states

    def flip(self, index):
        """
        Flips cakes whose indexes are greater than or equal the inputted
        index, returns the cost of the flip
        """
        flipped = self.cakes[index:]
        flipped.reverse()
        self.cakes = self.cakes[:index]+(flipped)
        return len(flipped)

    def goal(self):
        """Returns true, if we have reach the goal state"""
        return all(self.cakes[i] > self.cakes[i+1] for i in
                   range(len(self.cakes)-1))
