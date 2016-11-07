# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright 2017 Nicolas P. Rougier
# BSD License
# -----------------------------------------------------------------------------
import random
import numpy as np
import matplotlib.pyplot as plt

def timeit(stmt):
    import timeit
    trial = timeit.timeit(stmt, globals=globals(), number=1)
    duration = 1.0
    repeat = 3
    number = max(1,int(10**np.floor(np.log(duration/trial/repeat)/np.log(10))))
    best = min(timeit.repeat(stmt, globals=globals(), number=number, repeat=repeat))
    print("%d loops, best of %d: %g sec per loop" % (number, repeat, best/number))

    
def random_walk_1(n=1000):
    position=0
    walk = [position]
    for i in range(n):
        step = 2*random.randint(0, 1)-1
        position += step
        walk.append(position)


def random_walk_2(n=1000):
    from itertools import accumulate
    steps = random.sample([1,-1]*n, n)
    return list(accumulate(steps))


def random_walk_3(n=1000):
    steps = 2*np.random.randint(0, 2, size=n) - 1
    return np.cumsum(steps)


timeit("random_walk_1(n=10000)")
timeit("random_walk_2(n=10000)")
timeit("random_walk_3(n=10000)")


