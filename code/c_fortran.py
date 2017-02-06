# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# More information at https://github.com/rougier/numpy-book
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from display import display_2D_array



if __name__ == '__main__':

    Z1 = np.arange(9).reshape(3,3)
    Z2 = np.arange(9).reshape(3, 3, order='F')

    print(Z1.ravel())
    print(Z2.ravel())
