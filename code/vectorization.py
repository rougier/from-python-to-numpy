# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# More information at https://github.com/rougier/numpy-book
# -----------------------------------------------------------------------------
import numpy as np


def compute_1(x, y):
    """ Pure python version """

    result = 0
    for i in range(len(x)):
        for j in range(len(y)):
            result += x[i] * y[j]
    return result


def compute_2(X, Y):
    """ Numpy version, faster """

    return (X.reshape(len(X), 1) * Y.reshape(1, len(Y))).sum()


def compute_3(X, Y):
    """ Numpy version, fastest """

    return X.sum()*Y.sum()


def compute_4(X, Y):
    """ Pure python version, fastesr """

    return sum(X)*sum(Y)


if __name__ == '__main__':
    from tools import print_timeit

    X = np.arange(1000)
    print_timeit("compute_1(X,X)", globals())
    print_timeit("compute_2(X,X)", globals())
    print_timeit("compute_3(X,X)", globals())
    print_timeit("compute_4(X,X)", globals())
