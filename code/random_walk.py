# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# More information at https://github.com/rougier/numpy-book
# -----------------------------------------------------------------------------
import random
import numpy as np


# --- Object-oriented approach ------------------------------------------------
class RandomWalker:
    def __init__(self):
        self.position = 0

    def walk(self, n):
        self.position = 0
        for i in range(n):
            yield self.position
            self.position += 2*random.randint(0, 1) - 1


# --- Procedural approach -----------------------------------------------------
def random_walk(n):
    position = 0
    walk = [position]
    for i in range(n):
        step = 2*random.randint(0, 1)-1
        position += step
        walk.append(position)
    return walk


def random_walk_faster(n=1000):
    from itertools import accumulate
    # Only available from Python 3.6
    steps = random.choices([-1,+1], k=n)
    return [0]+list(accumulate(steps))


# --- Vectorized approach -----------------------------------------------------
def random_walk_fastest(n=1000):
    steps = np.random.choice([-1,+1], 1000)
    return np.cumsum(steps)


# -----------------------------------------------------------------------------
# Readable but slow
def find_crossing_1(seq, sub):
    return [i for i in range(len(seq) - len(sub)) if seq[i:i+len(sub)] == sub]

# Fast but hardly readable
def find_crossing_2(seq, sub):
    # See stackoverflow.com / "python-numpy-first-occurrence-of-subarray"
    target = np.dot(sub, sub)
    candidates = np.where(np.correlate(seq, sub, mode='valid') == target)[0]
    # some of the candidates entries may be false positives, double check
    check = candidates[:, np.newaxis] + np.arange(len(sub))
    mask = np.all((np.take(seq, check) == sub), axis=-1)
    return candidates[mask]


if __name__ == "__main__":
    from tools import timeit

    walker = RandomWalker()

    timeit("[position for position in walker.walk(n=10000)]", globals())
    timeit("random_walk(n=10000)", globals())
    timeit("random_walk_faster(n=10000)", globals())
    timeit("random_walk_fastest(n=10000)", globals())
    print()
    W = random_walk_fastest(n=1000)
    timeit("find_crossing_1(list(W), [+1,0,-1])", globals())
    timeit("find_crossing_2(W, [+1,0,-1])", globals())
