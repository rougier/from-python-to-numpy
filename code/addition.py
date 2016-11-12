# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# -----------------------------------------------------------------------------
import random
import numpy as np


def solution_1(Z1,Z2):
    return [z1+z2 for (z1,z2) in zip(Z1,Z2)]


def solution_2(Z1,Z2):
    return np.add(Z1,Z2)


if __name__ == '__main__':
    from tools import print_timeit

    Z1 = random.sample(range(10000), 1000)
    Z2 = random.sample(range(10000), 1000)
    print_timeit("solution_1(Z1, Z2)", globals())
    print_timeit("solution_2(Z1, Z2)", globals())

    Z1 = [[1,2],[3,4]]
    Z2 = [[5,6],[7,8]]
    print(solution_1(Z1, Z2))
    print(solution_2(Z1, Z2))

