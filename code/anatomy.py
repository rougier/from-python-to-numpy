# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# More information at https://github.com/rougier/numpy-book
# -----------------------------------------------------------------------------
import numpy as np
from tools import print_info

if __name__ == '__main__':
    Z = np.arange(5*5).reshape(5,5)
    print_info(Z)
    # Z = np.array(Z,order='F')
    # info(Z)
