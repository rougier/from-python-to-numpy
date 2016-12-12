# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# More information at https://github.com/rougier/numpy-book
# -----------------------------------------------------------------------------

def compute_neighbours(Z):
    shape = len(Z), len(Z[0])
    N = [[0, ]*(shape[0]) for i in range(shape[1])]
    for x in range(1, shape[0]-1):
        for y in range(1, shape[1]-1):
            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
                    + Z[x-1][y]            +Z[x+1][y]   \
                    + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N


def iterate(Z):
    shape = len(Z), len(Z[0])

    N = compute_neighbours(Z)
    for x in range(1, shape[0]-1):
        for y in range(1, shape[1]-1):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
    return Z

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle

    Z = [[0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 1, 0, 1, 0, 0],
         [0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]

    figure = plt.figure(figsize=(12, 3))

    labels = ("Initial state",
              "iteration 1", "iteration 2",
              "iteration 3", "iteration 4")

    for i in range(5):
        ax = plt.subplot(1, 5, i+1, aspect=1, frameon=False)

        for x in range(1, 5):
            for y in range(1, 5):
                if Z[x][y] == 1:
                    facecolor = 'black'
                else:
                    facecolor = 'white'
                rect = Rectangle((x, 5-y), width=0.9, height=0.9,
                                 linewidth=1.0, edgecolor='black',
                                 facecolor=facecolor)
                ax.add_patch(rect)
        ax.set_xlim(.9, 5.1)
        ax.set_ylim(.9, 5.1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlabel(labels[i])

        for tick in ax.xaxis.get_major_ticks():
            tick.tick1On = tick.tick2On = False
        for tick in ax.yaxis.get_major_ticks():
            tick.tick1On = tick.tick2On = False

        iterate(Z)

    plt.tight_layout()
    plt.savefig("glider.png")
    plt.show()
