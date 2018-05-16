from math import sqrt
import sys
import time
import search


from functools import wraps
import errno
import os
import signal

class TimeoutError(Exception):
    pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator


import flipit

tests2 = [ '0011', '0111', '0001', '0100']
tests3 = ['011100010', '000100010', '001111000']
tests4 = ['0111100010101001', '0000011110110100']
tests5 = ['1000000110100110101000000']

def run_tests():
    """run all of the tests"""
    print("Testing 2x2 problem", flush=True)
    for test in tests2:
        flipit_solve(2, initial=test)
    print("Testing 3x3 problem", flush=True)
    for test in tests3:
        flipit_solve(3, initial=test)
    print("Testing 4x4 problem", flush=True)
    for test in tests4:
        flipit_solve(4, initial=test)
    print("Testing 5x5 problem", flush=True)
    for test in tests5:
        flipit_solve(5, initial=test)        

def flipit_solve(size, initial):
    return flipit_solve1(size, initial)
    try:
        return flipit_solve1(size, initial)
    except:
        print('error', size, initial)
        return None

@timeout(300)
def flipit_solve1(size, initial):
    """ Solve a flip problem and print the result """
    problem =  search.InstrumentedProblem(flipit.FlipIt_optimal(size=size, initial=initial))
    print("{} Solving {} => {} optimal".format(size, problem.initial, problem.goal), flush=True)
    time0 = time.time()
    solution = search.astar_search(problem)
    elapsed = time.time() - time0
    show_solution(solution, problem, elapsed)

    problem =  search.InstrumentedProblem(flipit.FlipIt_aggressive(size=size, initial=initial))
    print("{} Solving {} => {} aggressive".format(size, problem.initial, problem.goal), flush=True)
    time0 = time.time()
    solution = search.astar_search(problem)
    elapsed = time.time() - time0
    show_solution(solution, problem, elapsed)
    

def show_solution(solution_node, ip, time=0):
    """ Print a flipit solution """
    if solution_node:
        path = solution_node.path()
        print("Solution of length {} found".format(len(path) - 1, time, ip.states, ip.succs, flush=True))
        #actions = [None] + solution_node.solution()
        #for action, node in zip(actions, path):
        #print("flip {} =>".format(action) if action != None else 'initial', flush=True)
        #print_state(node.state)
    else:
        print("No solution found", flush=True)
    print(" ", flush=True)

    
def print_state(state):
    """ print a flipit state """
    out = sys.stdout
    size = sqrt(len(state))
    out.write('  ')
    for i, char in enumerate(state):
        if i % size == 0 and i:
            out.write('\n  ')
        out.write(char)
    out.write('\n')

# if called from the command line, call run_tests
if __name__ == "__main__":
    run_tests()
        
