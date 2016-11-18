# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# More information at https://github.com/rougier/numpy-book
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt


def display(Z, filename=None, vmin=0, vmax=8):
    resolution = 24 # pixels
    dpi = 72
    rows, cols = Z.shape
    border = 2
    height = (rows*resolution + 2*border)
    width = (cols*resolution + 2*border)

    fig = plt.figure(figsize=(width/dpi, height/dpi), dpi=dpi)
    x = border / width
    w = 1 - 2*x
    y = border / height
    h = 1 - 2*y
    ax = fig.add_axes([x, y, w, h], frameon=True, aspect=1)

    # ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=True) # aspect=1)
    ax.imshow(Z, interpolation="nearest", cmap=plt.cm.gray,
              extent=[0, Z.shape[1], 0, Z.shape[0]], vmin=vmin, vmax=vmax)

    plt.xticks([]), plt.yticks([])
    if filename:
        plt.savefig(filename, dpi=dpi, transparent=True)
    else:
        plt.show()

display(np.zeros((1, 9)), "../pics/creation-1.png", 0, 1)
display(np.ones((1, 9)), "../pics/creation-2.png", 0, 1)
display(np.arange(9).reshape(1, 9), "../pics/creation-3.png", 0, 8)
display(np.random.randint(0, 9, (1, 9)), "../pics/creation-4.png", 0, 8)
display(np.zeros((3, 9)), "../pics/creation-5.png", 0, 1)
display(np.ones((3, 9)), "../pics/creation-6.png", 0, 1)
display(np.arange(3*9).reshape(3, 9), "../pics/creation-7.png", 0, 3*9-1)
display(np.random.randint(0, 9, (3, 9)), "../pics/creation-8.png", 0, 8)

