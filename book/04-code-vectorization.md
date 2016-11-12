## Chapter 4 - Code vectorization

**Content**

* [Introduction](#introduction)
* [Fractals](#fractals)
* [Cellular automata](#automata)
* [Reaction diffusion](#reaction-diffusion)
* [Earthquake visualization](#earthquake)
* [Conclusion](#conclusion)

### Introduction <a name="introduction"></a>

Code vectorization means that the problem you're trying to solve is inherently
vectorizable and only requires a few numpy tricks to make it faster. Of course
it does not mean it is easy nor straighforward, but at least it does not
necessitate to totally rethink your problem. Still, it may require some
experience to see where code can be vectorized. Let's illustrate this through
the most simple example I can think of where we want to sum up two lists of
integers. One straightforwardway  using pure Python is:

    import random

    def solution_1(Z1,Z2):
        return [z1+z2 for (z1,z2) in zip(Z1,Z2)]

This first naive solution can be vectorize very easily using numpy:

    import numpy as np
    
    def solution_2(Z1,Z2):
        return np.add(Z1,Z2)

Without nay surprise, benchmarkming the two approaches shows the second method is
the fastest with one order of magnitude.

    >>> Z1 = random.sample(range(1000), 100)
    >>> Z2 = random.sample(range(1000), 100)
    >>> print_timeit("solution_1(Z1, Z2)", globals())
    1000 loops, best of 3: 68 usec per loop
    >>> print_timeit("solution_2(Z1, Z2)", globals())
    10000 loops, best of 3: 1.14 usec per loop
    
Not only the second approach is faster, but it also naturally adapts to the
shape of `Z1` and `Z2`, which is not the case for the first method because the
`+` will be interpreted differently depending on the nature of the
object. For example, if we now consider two nested lists:

    >>> Z1 = [[1,2],[3,4]]
    >>> Z2 = [[5,6],[7,8]]
    >>> solution_1(Z1, Z2)
    [[1, 2, 5, 6], [3, 4, 7, 8]]
    >>> solution_2(Z1, Z2)
    [[ 6  8]
     [10 12]]

The first method concatenates the internal lists together while the second one
does what is (numerically) expected. Let's move now move to more complex
problems.


### Fractals <a name="fractals"></a>

**From Wikipedia**: The Mandelbrot set is the set of complex numbers c for
  which the function fc(z) = z²+ c does not diverge when iterated from z=0,
  i.e., for which the sequence fc(0), fc(fc(0)), etc., remains bounded in
  absolute value.

### Cellular automata <a name="automata"></a>
### Reaction diffusion <a name="reaction-diffusion"></a>
### Earthquake visualization <a name="earthquake"></a>
### Conclusion <a name="conclusion"></a>
