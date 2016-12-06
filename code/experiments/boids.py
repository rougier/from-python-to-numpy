# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# More information at https://github.com/rougier/numpy-book
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from matplotlib.animation import FuncAnimation


def update(frame_number):

    P = boids['position']
    Px = boids['position'][:, 0]
    Py = boids['position'][:, 1]

    V = boids['velocity']
    Vx = boids['velocity'][:, 0]
    Vy = boids['velocity'][:, 1]

    # Mask that cancel out diagonal
    # M = (1-np.diag(np.ones(len(P))))

    # Compute all paired distances between boids (D[i,i] = 0)
    D = cdist(P, P)

    # Parameters
    # ----------
    dt = 0.05

    repulsion_radius = 0.05
    repulsion_strength = 1.5
    
    cohesion_radius = 0.1
    cohesion_strength = 1.0
    
    alignment_radius = 0.1
    alignment_strength = 1.0

    
    # Rule 1: repulsion (boids move away from local neihgbours)
    # ---------------------------------------------------------
    M = (D < repulsion_radius)*(D > 0)
    N = M.sum(axis=1)

    
    
    Ax = repulsion_strength*(Px - (M*Px).sum(axis=1) / N)
    Ay = repulsion_strength*(Py - (M*Py).sum(axis=1) / N)

    
    # Rule 2: cohesion (boids move towards local centers)
    # ---------------------------------------------------
    # M = (D < cohesion_radius)
    # N = M.sum(axis=1)
    # Ax += cohesion_strength*((M*Px).sum(axis=1) / N - Px)
    # Ay += cohesion_strength*((M*Py).sum(axis=1) / N - Py)

    # Rule 3: alignment (boids steer likes local boids)
    # -------------------------------------------------
    # M = (D < alignment_radius)
    # N = M.sum(axis=1)
    # Ax += alignment_strength*(Vx - (M*Vx).sum(axis=1) / N)
    # Ay += alignment_strength*(Vy - (M*Vy).sum(axis=1) / N)

    Vx += Ax
    Vy += Ay
    
    V[...] = np.maximum(-0.1, V)
    V[...] = np.minimum(+0.1, V)
    P[...] = np.maximum(-1.0, P)
    P[...] = np.minimum(+1.0, P)
    # V[...] = np.clip(V * 0.8 , -0.1, 0.1)

    P += dt*V
    scatter.set_offsets(boids['position'])

    """
    dt = 0.1
    n = len(boids)

    # Position
    P = boids['position']
    Px = boids['position'][:,0]
    Py = boids['position'][:,1]

    # Velocity
    V = boids['velocity']
    Vx = boids['velocity'][:,0]
    Vy = boids['velocity'][:,1]

    # Boids distance
    T = cKDTree(P)
    # k nearest neighbors
    k = 3
    D, I = T.query(P, k)

    print(D.shape)

    # Cohesion: steer to move toward the average position of local flockmates
    # C = (P.sum(axis=0)/n - P)
    C = (P - P[I].sum(axis=1)/(k-1))

    # Alignment: steer towards the average heading of local flockmates
    # A = (V.sum(axis=0)/n - V)
    A = (V[I].sum(axis=1)/(k-1) - V)

    # Repulsion: steer to avoid crowding local flockmates
    R = P - P[I][:,1:,:].sum(axis=1)/(k-1)

    #M = np.repeat(D < 0.05, 2, axis=1).reshape(n, 7, 2)
    #Z = np.repeat(P, 7, axis=0).reshape(n, 7, 2)
    #R = ((Z-P[I]) * M).sum(axis=1)

    V += .01*R #.1*(.5*C + 1.5*A + 3.5*R )
    P += V*dt

    V[...] = np.maximum(-.1,V)
    V[...] = np.minimum(+.1,V)

    P[...] = np.maximum(-1,P)
    P[...] = np.minimum(+1,P)
    #scatter.set_offsets(boids['position'])
    """


n = 1000
xmin, xmax = -1.0, +1.0
ymin, ymax = -1.0, +1.0


boids = np.zeros(n, [('position', 'f4', 2),
                     ('velocity', 'f4', 2)])
boids['position'] = 0.2*np.random.uniform(-1.00, +1.00, (n, 2))
boids['velocity'] = 0.0*np.random.uniform(-0.10, +0.10, (n, 2))


fig = plt.figure(figsize=(8, 8))
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=True, aspect=1)
scatter = ax.scatter(boids["position"][:, 0], boids["position"][:, 1],
                     s=10, facecolor="red", edgecolor="None", alpha=0.5)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
animation = FuncAnimation(fig, update, interval=10)
plt.show()

