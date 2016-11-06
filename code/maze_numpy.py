# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier
# -----------------------------------------------------------------------------
"""
Maze solving using the Bellman-Ford algorithm
"""

import numpy as np
from collections import deque
import matplotlib.pyplot as plt
from scipy.ndimage import generic_filter


# -------------------------------------------------------------- build_maze ---
def build_maze(shape=(65,65), complexity=0.75, density = 0.50):
    """
    Build a maze using given complexity and density

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
def BellmanFord(Z, start, goal):

    # We reserve Z such that walls have value 0
    Z = 1 - Z
    
    # Build gradient array
    G = np.zeros(Z.shape)

    # Initialize gradient at the entrance with value 1
    G[start] = 1

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
    while G[goal] == 0.0:
        G = Z * generic_filter(G, diffuse, footprint= [[0, 1, 0],
                                                       [1, 1, 1],
                                                       [0, 1, 0]])
    
    # Descent gradient to find shortest path from entrance to exit
    y, x = goal
    P = []
    dirs = [(0,-1), (0,+1), (-1,0), (+1,0)]
    while (x, y) != start:
        P.append((x, y))
        neighbours = [-1, -1, -1, -1]
        if x > 0:
            neighbours[0] = G[y, x-1]
        if x < G.shape[1]-1:
            neighbours[1] = G[y, x+1]
        if y > 0:
            neighbours[2] = G[y-1, x]
        if y < G.shape[0]-1:
            neighbours[3] = G[y+1, x]
        a = np.argmax(neighbours)
        x, y  = x + dirs[a][1], y + dirs[a][0]
    P.append((x, y))
    return G, np.array(P)

def build_graph(maze):
    height, width = maze.shape
    graph = {(i, j): [] for j in range(width) for i in range(height) if not maze[i][j]}
    for row, col in graph.keys():
        if row < height - 1 and not maze[row + 1][col]:
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width - 1 and not maze[row][col + 1]:
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph

def BreadthFirst(maze):
    start, goal = (1, 1), (len(maze) - 2, len(maze[0]) - 2)
    queue = deque([([start], start)])
    visited = set()
    graph = build_graph(maze)
    while queue:
        path, current = queue.popleft()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            p = list(path)
            p.append(neighbour)
            queue.append((p, neighbour))
    return "NO WAY!"


# -------------------------------------------------------------------- main ---
if __name__ == '__main__':

    n = 51
    start, goal = (1,1), (n-2,n-2)
    Z = build_maze((n,n))
    
    G, P = BellmanFord(Z, start, goal)
    X, Y = P[:,0], P[:,1]

    # P = np.array(BreadthFirst(Z))
    # X, Y = P[:,1], P[:,0]
    
    # Visualization maze, gradient and shortest path
    plt.figure(figsize=(9,9))
    ax = plt.subplot(1, 1, 1, frameon=False)
    ax.imshow(Z, interpolation='nearest', cmap=plt.cm.gray_r, vmin=0.0, vmax=1.0)
    cmap = plt.cm.hot
    cmap.set_under(color='k', alpha=0.0)
    ax.imshow(G, interpolation='nearest', cmap=cmap, vmin=0.01, vmax=G[start])
    ax.scatter(X[1:-1], Y[1:-1], s=60,
               lw=1, marker='o', edgecolors='k', facecolors='w')
    ax.scatter(X[[0,-1]], Y[[0,-1]], s=60,
               lw=3, marker='x', color=['w','k'])
    ax.set_xticks([])
    ax.set_yticks([])
    plt.tight_layout()
    plt.show()

