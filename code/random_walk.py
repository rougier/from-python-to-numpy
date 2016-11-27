# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# More information at https://github.com/rougier/numpy-book
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
    steps = random.sample([1, -1]*n, n)
    return list(accumulate(steps))


def random_walk_3(n=1000):
    """ Numpy version, fastest """
    steps = 2*np.random.randint(0, 2, size=n) - 1
    return np.cumsum(steps)


def find_crossing_1(seq, subseq):
    """ Readable but slow """
    return [i for i in range(len(seq) - len(subseq))
                    if seq[i:i+len(subseq)] == subseq]


def find_crossing_2(seq, subseq):
    """ Fast but hardly readable """
    # See http://stackoverflow.com/questions/7100242/python-numpy-first-occurrence-of-subarray
    target = np.dot(subseq, subseq)
    candidates = np.where(np.correlate(seq, subseq, mode='valid') == target)[0]
    # some of the candidates entries may be false positives, double check
    check = candidates[:, np.newaxis] + np.arange(len(subseq))
    mask = np.all((np.take(seq, check) == subseq), axis=-1)
    return candidates[mask]


if __name__ == "__main__":
    from tools import print_timeit

    print_timeit("random_walk_1(n=10000)", globals())
    print_timeit("random_walk_2(n=10000)", globals())
    print_timeit("random_walk_3(n=10000)", globals())
    print()
    W = random_walk_3(n=1000)
    print_timeit("find_crossing_1(list(W), [+1,0,-1])", globals())
    print_timeit("find_crossing_2(W, [+1,0,-1])", globals())
