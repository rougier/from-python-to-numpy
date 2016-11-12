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
experience to see where code can be vectorized. We'll illustrate this through a
simple example. Let's consider two lists of integers we want to sum:

    import random

    def solution_1(Z1,Z2):
        return [z1+z2 for (z1,z2) in zip(Z1,Z2)]

This solution is easy to vectorize as:

    import numpy as np
    
    def solution_2(Z1,Z2):
        return Z1+Z2

And if we benchmark the two approaches, the second one is the fastest as expected.

    >>> Z1 = random.sample(range(1000), 100)
    >>> Z2 = random.sample(range(1000), 100)
    >>> print_timeit("solution_1(Z1, Z2)", globals())
    1000 loops, best of 3: 68 usec per loop
    
    >>> Z1 = np.random.randint(0, 10000, 1000)
    >>> Z2 = np.random.randint(0, 10000, 1000)
    >>> print_timeit("solution_2(Z1, Z2)", globals())
    10000 loops, best of 3: 1.14 usec per loop
    
This example was straigthforward, let's head for less obvious ones.

### Fractals <a name="fractals"></a>

**From Wikipedia**: The Mandelbrot set is the set of complex numbers c for
  which the function fc(z) = z²+ c does not diverge when iterated from z=0,
  i.e., for which the sequence fc(0), fc(fc(0)), etc., remains bounded in
  absolute value.

### Cellular automata <a name="automata"></a>
### Reaction diffusion <a name="reaction-diffusion"></a>
### Earthquake visualization <a name="earthquake"></a>
### Conclusion <a name="conclusion"></a>
