# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier
# -----------------------------------------------------------------------------
"""
Maze solving using the Bellman-Ford algorithm
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import generic_filter

# -------------------------------------------------------------- build_maze ---
def build_maze(shape=(65,65), complexity=0.75, density = 0.50):
    """
    Build a maze with given complexity and density

    Parameters
    ==========

    shape : (rows,cols)
      Size of the maze

    complexity: float
      Mean length of islands (as a ratio of maze size)

    density: float
      Mean numbers of highland (as a ratio of maze surface)

    """
    
    # Only odd shapes
    shape = ((shape[0]//2)*2+1, (shape[1]//2)*2+1)

    # Adjust complexity and density relative to maze size
    n_complexity = int(complexity*(shape[0]+shape[1]))
    n_density    = int(density*(shape[0]*shape[1]))

    # Build actual maze
    Z = np.zeros(shape, dtype=bool)

    # Fill borders
    Z[0,:] = Z[-1,:] = 1
    Z[:,0] = Z[:,-1] = 1

    # Create islands
    for i in range(n_density):

        # This favors islands start away from the center
        x = shape[1]*(0.5-min(max(np.random.normal(0,.5),-.5),.5))
        y = shape[0]*(0.5-min(max(np.random.normal(0,.5),-.5),.5))
        x, y = int((x//2)*2), int((y//2)*2)

        Z[y,x] = 1
        for j in range(n_complexity):
            neighbours = []
            if x > 1:
                neighbours.append([(y,x-1),(y,x-2)])
            if x < shape[1]-2:
                neighbours.append([(y,x+1),(y,x+2)])
            if y > 1:
                neighbours.append([(y-1,x),(y-2,x)])
            if y < shape[0]-2:
                neighbours.append([(y+1,x),(y+2,x)])

            if len(neighbours):
                choice = np.random.randint(len(neighbours))
                next_1, next_2 = neighbours[choice]
                if Z[next_2] == 0:
                    Z[next_1] = Z[next_2] = 1
                    y, x = next_2
            else:
                break
    return Z


# ------------------------------------------------------ find_shortest_path ---
def find_shortest_path(Z, entrance, exit):

    # Build gradient array
    G = np.zeros(Z.shape)

    # Initialize gradient at the entrance with value 1
    G[entrance] = 1

    # Discount factor
    gamma = 0.99
    
    def diffuse(Z):
        # North, West, Center, East, South
        return max(gamma*Z[0], gamma*Z[1], Z[2], gamma*Z[3], gamma*Z[4])

    # Shortest path in best case cannot be less the Manhattan distance
    # from entrance to exit
    length = Z.shape[0]+Z.shape[1]

    # We iterate until value at exit is > 0. This requires the maze
    # to have a solution or it will be stuck in the loop.
    while G[exit] == 0.0:
        for i in range(length):
            G = Z * generic_filter(G, diffuse, footprint= [[0, 1, 0],
                                                           [1, 1, 1],
                                                           [0, 1, 0]])
        
    # Descent gradient to find shortest path from entrance to exit
    y, x = exit
    P = []
    dirs = [(0,-1), (0,+1), (-1,0), (+1,0)]
    # S = Z.astype(float)
    for i in range(5*(n+n)):
        P.append((x,y))
        neighbours = [-1,-1,-1,-1]
        if x > 0:
            neighbours[0] = G[y,x-1]
        if x < G.shape[1]-1:
            neighbours[1] = G[y,x+1]
        if y > 0:
            neighbours[2] = G[y-1,x]
        if y < G.shape[0]-1:
            neighbours[3] = G[y+1,x]
        a = np.argmax(neighbours)
        x, y  = x + dirs[a][1], y + dirs[a][0]
    return G, np.array(P)


# -------------------------------------------------------------------- main ---
if __name__ == '__main__':

    n = 41
    entrance, exit = (-1,-2), (0,1)
    Z = 1 - build_maze((51,51))
    Z[entrance] = 1
    Z[exit] = 1

    G, P = find_shortest_path(Z, entrance, exit)
    X, Y = P[:,0], P[:,1]

    # Visualization
    plt.figure(figsize=(9,9))
    ax = plt.subplot(1, 1, 1, frameon=False)
    ax.imshow(G, interpolation='nearest', cmap=plt.cm.hot, vmin=0, vmax=1)
    ax.scatter(X, Y, s=60, lw=1, color='k', marker='o', edgecolors='k', facecolors='w')
    ax.set_xticks([])
    ax.set_yticks([])

    ax.text(1.0, -1.25, "Exit",
            transform=ax.transData, fontsize=12, ha = 'center', va = 'center')
    ax.text(G.shape[0]-2, G.shape[1]+0.25, "Entrance",
            transform=ax.transData, fontsize=12, ha = 'center', va = 'center')

    plt.tight_layout()
    plt.show()
