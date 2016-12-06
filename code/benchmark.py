import numpy as np
from scipy.spatial import cKDTree
from scipy.spatial.distance import cdist


P = np.random.uniform(0,1,(1000,2))

def benchmark_3(P):
    xs, ys = P[:, 0], P[:, 1]
    xdiff = np.add.outer(xs, -xs)
    ydiff = np.add.outer(ys, -ys)
    # D = np.sqrt(xdiff ** 2 + ydiff ** 2)
    D = cdist(P,P)
    P1 = (D < 0.01)
    P2 = (D < 0.02)
    P3 = (D < 0.03)

def benchmark_1(P):
    D = cdist(P,P)
    P1 = (D < 0.01)
    P2 = (D < 0.02)
    P3 = (D < 0.03)

    
def benchmark_2(P):
    T = cKDTree(P)
    P1 = T.query_ball_point(P, 0.01)
    P2 = T.query_ball_point(P, 0.02)
    P3 = T.query_ball_point(P, 0.03)
