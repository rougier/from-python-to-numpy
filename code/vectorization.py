import numpy as np

def compute_1(x, y):
    result = 0
    for i in range(len(x)):
        for j in range(len(y)):
            result += x[i] * y[j]
    return result

def compute_2(X, Y):
    return (X.reshape(len(X),1) * Y.reshape(1,len(Y))).sum()

def compute_3(X, Y):
    return X.sum()*Y.sum()

def timeit(stmt):
    import timeit
    
    # Rough approximation of a single run
    trial = timeit.timeit(stmt, globals=globals(), number=1)

    # Computation of a round number of loops
    time = 1.0
    repeat = 3
    number = max(1,int(10**np.floor(np.log(time/trial/repeat)/np.log(10))))
    best = min(timeit.repeat(stmt, globals=globals(), number=number, repeat=repeat))

    # Display result
    print("%d loops, best of %d: %g sec per loop" % (number, repeat, best/number))


if __name__ == '__main__':

    X = np.arange(100)
    timeit("compute_1(X,X)")
    timeit("compute_2(X,X)")
    timeit("compute_3(X,X)")
