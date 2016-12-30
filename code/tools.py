# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# More information at https://github.com/rougier/numpy-book
# -----------------------------------------------------------------------------
def sysinfo():
    import sys
    import time
    import numpy as np
    import scipy as sp
    import matplotlib

    print("Date:       %s" % (time.strftime("%D")))
    version = sys.version_info
    major, minor, micro = version.major, version.minor, version.micro
    print("Python:     %d.%d.%d" % (major, minor, micro))
    print("Numpy:     ", np.__version__)
    print("Scipy:     ", sp.__version__)
    print("Matplotlib:", matplotlib.__version__)

    

def timeit(stmt, globals):
    import timeit as _timeit
    import numpy as np
    
    # Rough approximation of a single run
    trial = _timeit.timeit(stmt, globals=globals, number=1)
    
    # Maximum duration
    duration = 1.0
    
    # Number of repeat
    repeat = 3
    
    # Compute rounded number of trials
    number = max(1,int(10**np.floor(np.log(duration/trial/repeat)/np.log(10))))
    
    # Only report best run
    best = min(_timeit.repeat(stmt, globals=globals, number=number, repeat=repeat))

    units = {"usec": 1, "msec": 1e3, "sec": 1e6}
    precision = 3
    usec = best * 1e6 / number
    if usec < 1000:
        print("%d loops, best of %d: %.*g usec per loop" % (number, repeat,
                                                            precision, usec))
    else:
        msec = usec / 1000
        if msec < 1000:
            print("%d loops, best of %d: %.*g msec per loop" % (number, repeat,
                                                                precision, msec))
        else:
            sec = msec / 1000
            print("%d loops, best of %d: %.*g sec per loop" % (number, repeat,
                                                               precision, sec))
   
    # Display results
    # print("%d loops, best of %d: %g sec per loop" % (number, repeat, best/number))

    
def info(Z):
    import numpy as np
        
    print("------------------------------")
    print("Interface (item)")
    print("  shape:      ", Z.shape)
    print("  dtype:      ", Z.dtype)
    print("  size:       ", Z.size)
    if np.isfortran(Z):
        print("  order:       ☐ C  ☑ Fortran")
    else:
        print("  order:       ☑ C  ☐ Fortran")
    print("")
    print("Memory (byte)")
    print("  item size:  ", Z.itemsize)
    print("  array size: ", Z.size*Z.itemsize)
    print("  strides:    ", Z.strides)
    print("")
    print("Properties")
    if Z.flags["OWNDATA"]:
        print("  own data:    ☑ Yes  ☐ No")
    else:
        print("  own data:    ☐ Yes  ☑ No")
    if Z.flags["WRITEABLE"]:
        print("  writeable:   ☑ Yes  ☐ No")
    else:
        print("  writeable:   ☐ Yes  ☑ No")
    if np.isfortran(Z) and Z.flags["F_CONTIGUOUS"]:
        print("  contiguous:  ☑ Yes  ☐ No")
    elif not np.isfortran(Z) and Z.flags["C_CONTIGUOUS"]:
        print("  contiguous:  ☑ Yes  ☐ No")
    else:
        print("  contiguous:  ☐ Yes  ☑ No")
    if Z.flags["ALIGNED"]:
        print("  aligned:     ☑ Yes  ☐ No")
    else:
        print("  aligned:     ☐ Yes  ☑ No")
    print("------------------------------")
    print()
