# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# More information at https://github.com/rougier/numpy-book
# -----------------------------------------------------------------------------
import numpy as np
from tools import info

if __name__ == '__main__':
    Z = np.arange(4*4).reshape(4,4)

    Z = np.array(Z, order='C')
    info(Z)

    Z = np.array(Z, order='F')
    info(Z)

