# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# More information at https://github.com/rougier/numpy-book
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist


def DART_sampling_numpy(width=1.0, height=1.0, radius=0.025, k=100):

    # Theoretical limit
    n = int((width+radius)*(height+radius) / (2*(radius/2)*(radius/2)*np.sqrt(3))) + 1
    # 5 times the theoretical limit
    n = 5*n

    # Compute n random points
    P = np.zeros((n, 2))
    P[:, 0] = np.random.uniform(0, width, n)
    P[:, 1] = np.random.uniform(0, height, n)

    # Computes respective distances at once
    D = cdist(P, P)

    # Cancel null distances on the diagonal
    D[range(n), range(n)] = 1e10

    points, indices = [P[0]], [0]
    i = 1
    last_success = 0
    while i < n and i - last_success < k:
        if D[i, indices].min() > radius:
            indices.append(i)
            points.append(P[i])
            last_success = i
        i += 1
    return points


if __name__ == '__main__':

    plt.figure()
    plt.subplot(1, 1, 1, aspect=1)

    points = DART_sampling_numpy()
    X = [x for (x, y) in points]
    Y = [y for (x, y) in points]
    plt.scatter(X, Y, s=10)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()
