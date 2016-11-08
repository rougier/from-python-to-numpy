# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright 2017 Nicolas P. Rougier - BSD License
# -----------------------------------------------------------------------------
import random
import numpy as np


def random_walk_1(n=1000):
    """ Pure python version """

    position=0
    walk = [position]
    for i in range(n):
        step = 2*random.randint(0, 1)-1
        position += step
        walk.append(position)


def random_walk_2(n=1000):
    """ Pure python version, faster """

    from itertools import accumulate
    steps = random.sample([1,-1]*n, n)
    return list(accumulate(steps))


def random_walk_3(n=1000):
    """ Numpy version, fastest """
    steps = 2*np.random.randint(0, 2, size=n) - 1
    return np.cumsum(steps)


if __name__ == "__main__":
    from tools import timeit
    
    timeit("random_walk_1(n=10000)", globals())
    timeit("random_walk_2(n=10000)", globals())
    timeit("random_walk_3(n=10000)", globals())


