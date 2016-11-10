# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# -----------------------------------------------------------------------------

def print_timeit(stmt, globals):
    import timeit
    import numpy as np
    
    # Rough approximation of a single run
    trial = timeit.timeit(stmt, globals=globals, number=1)
    
    # Maximum duration
    duration = 1.0
    
    # Number of repeat
    repeat = 3
    
    # Compute rounded number of trials
    number = max(1,int(10**np.floor(np.log(duration/trial/repeat)/np.log(10))))
    
    # Only report best run
    best = min(timeit.repeat(stmt, globals=globals, number=number, repeat=repeat))

    # Display results
    print("%d loops, best of %d: %g sec per loop" % (number, repeat, best/number))

    
def print_info(Z):
    import numpy as np
        
    print("------------------------------")
    print("Interface (item)")
    print("  shape:      ", Z.shape)
    print("  dtype:      ", Z.dtype)
    print("  size:       ", Z.size)
    if np.isfortran(Z):
        print("  order:       ☐ C  ☑︎ Fortran")
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
        print("  own data:    ☑ Yes  ☐︎ No")
    else:
        print("  own data:    ☐ Yes  ☑︎ No")
    if Z.flags["WRITEABLE"]:
        print("  writeable:   ☑ Yes  ☐︎ No")
    else:
        print("  writeable:   ☐ Yes  ☑︎ No")
    if np.isfortran(Z) and Z.flags["F_CONTIGUOUS"]:
        print("  contiguous:  ☑ Yes  ☐︎ No")
    elif not np.isfortran(Z) and Z.flags["C_CONTIGUOUS"]:
        print("  contiguous:  ☑ Yes  ☐︎ No")
    else:
        print("  contiguous:  ☐ Yes  ☑︎ No")
    if Z.flags["ALIGNED"]:
        print("  aligned:     ☑ Yes  ☐︎ No")
    else:
        print("  aligned:     ☐ Yes  ☑︎ No")
    print("------------------------------")
    print()
