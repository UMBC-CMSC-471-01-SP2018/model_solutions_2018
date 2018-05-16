import random
import sys
from math import sqrt, ceil
from collections import defaultdict
import search

class FlipIt(search.Problem):
    """
    STATE: string of size**2 bits
    GOAL: a state with all bits = 0
    PROBLEM:  """

    name = "null"

    def __init__(self, size=3, initial=None, goal=None, steps=None):
        self.size = size
        self.goal = goal or ''.join('0' for _ in range(size**2))
        if initial:
            self.initial = initial
        elif steps:
            self.initial = random_walk_state(self.goal, steps, self.map)
        else:
            self.initial = ''.join(random.choice(['0','1']) for _ in range(size**2))
        self.map = make_map(size)

    def __repr__(self):
        """ Returns a string representing the object """
        return "FlipIt({},{},{})".format(self.size, self.initial, self.goal)

    def goal_test(self, state):
        """ Returns true if state is a goal state """
        return state == self.goal

    def h(self, node):
        """ Estimate of cost of shortest path from node to a goal """
        return 1
    
    def actions(self, state):
        """ generates legal actions for state """
        return range(self.size**2)

    def result(self, state, action):
        """ Returns the successor of state after doing action """
        return flipper(state, action, self.map)
    
    def path_cost(self, c, state1, action, state2):
        """ Cost of path from start node to state1 assuming cost c to
        get to state1 and doing action to get to state2 """
        return c + 1
        

class FlipIt_optimal(FlipIt):

    name = "optimal"
    
    def h(self, node):
        """ An admissable stimate of cost of shortest path from node to a goal """
        return ceil(node.state.count('1') / 5.0)    


class FlipIt_aggressive(FlipIt):

    name = "aggressive"
    
    def h(self, node):
        """ a more aggressive, non-admissable estimate of cost of
        shortest path from node to a goal """
        return node.state.count('1')

def flipper(state, cell, map):
    inverse = {'0':'1', '1':'0'}
    state = list(state)
    state[cell] = inverse[state[cell]]
    for i in map[cell]:
        state[i] = inverse[state[i]]
    return ''.join(state)


def random_walk_state(s, n, map):
    """returns a state after n random flips"""
    cells = list(range(len(s)))
    size = len(cells)
    path = [s]
    for _ in range(n):
        # do random flips until you find a state not on already on the path
        new_s = flipper(s, random.choice(cells), map)
        tries = 1
        while tries <= size and new_s in path:
            tries += 1
            new_s = flipper(s, random.choice(cells), map)
        if tries <= size:
            s = new_s
            path.append(s)
        else:
            # bail if we exausted our tries
            print("Stopping after {} steps".format(len(path) - 1))
            break
    return s

def random_tests(size, steps):
    """ returns a list flipit problems of a given size that are a
        certain number of steps away from the goal.  Call like
        random_tests(3, [2,4,6,6]."""
    # goal state is a string on size 0's
    goal_state = ''.join('0' for _ in range(size*size))
    map = make_map(size)
    results = []
    for step in steps:
        results.append(random_walk_state(goal_state, step, map))
    return results

def show_solution(goal):
    if goal:
        path = goal.path()
        print("Solution with {} steps found".format(len(path) - 1))
        actions = [None] + goal.solution()
        for action, node in zip(actions, path):
            state = node.state
            print('flip {}'.format(action) if action else 'initial')
            print_state(state)
    else:
        print("No solution found")

def print_state(state):
    out = sys.stdout
    size = sqrt(len(state))
    out.write('  ')
    for i, char in enumerate(state):
        if i % size == 0 and i:
            out.write('\n  ')
        out.write(char)
    out.write('\n\n')

def make_map(size):
    def top(n): return n < size
    def bottom(n): return n >= (size*size - size)
    def left(n): return n % size == 0
    def right(n): return n % size == size - 1
    map = defaultdict(list)
    for i in range(size*size):
        if not top(i): map[i].append(i-size)
        if not bottom(i): map[i].append(i+size)
        if not left(i): map[i].append(i-1)
        if not right(i): map[i].append(i+1)
    return map
