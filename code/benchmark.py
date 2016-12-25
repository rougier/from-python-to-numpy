# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# More information at https://github.com/rougier/numpy-book
# -----------------------------------------------------------------------------
import numpy as np
from tools import timeit

Z = np.ones(4*1000000, np.float32)

print(">>> Z.view(np.float16)[...] = 0")
timeit("Z.view(np.float16)[...] = 0", globals())

print(">>> Z.view(np.int16)[...] = 0")
timeit("Z.view(np.int16)[...] = 0", globals())

print(">>> Z.view(np.int32)[...] = 0")
timeit("Z.view(np.int32)[...] = 0", globals())

print(">>> Z.view(np.float32)[...] = 0")
timeit("Z.view(np.float32)[...] = 0", globals())

print(">>> Z.view(np.int64)[...] = 0")
timeit("Z.view(np.int64)[...] = 0", globals())

print(">>> Z.view(np.float64)[...] = 0")
timeit("Z.view(np.float64)[...] = 0", globals())

print(">>> Z.view(np.complex128)[...] = 0")
timeit("Z.view(np.complex128)[...] = 0", globals())

print(">>> Z.view(np.int8)[...] = 0")
timeit("Z.view(np.int8)[...] = 0", globals())
