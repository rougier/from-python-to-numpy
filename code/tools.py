# -----------------------------------------------------------------------------
# From Numpy to Python
# Copyright (2017) Nicolas P. Rougier - BSD license
# -----------------------------------------------------------------------------

def timeit(stmt, globals):
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
