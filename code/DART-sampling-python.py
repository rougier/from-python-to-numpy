# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# More information at https://github.com/rougier/numpy-book
# -----------------------------------------------------------------------------
import math
import random
import matplotlib.pyplot as plt


def DART_sampling_python(width=1.0, height=1.0, radius=0.025, k=100):
    def squared_distance(p0, p1):
        dx, dy = p0[0]-p1[0], p0[1]-p1[1]
        return dx*dx+dy*dy

    points = []
    i = 0
    last_success = 0
    while True:
        x = random.uniform(0, width)
        y = random.uniform(0, height)
        accept = True
        for p in points:
            if squared_distance(p, (x, y)) < radius*radius:
                accept = False
                break
        if accept is True:
            points.append((x, y))
            if i-last_success > k:
                break
            last_success = i
        i += 1
    return points

if __name__ == '__main__':

    plt.figure()
    plt.subplot(1, 1, 1, aspect=1)

    points = DART_sampling_python()
    X = [x for (x, y) in points]
    Y = [y for (x, y) in points]
    plt.scatter(X, Y, s=10)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()
