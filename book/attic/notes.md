### Resources <a name="resources"></a>

Numpy comes with a large set of resources that are accesible from the
command-line or online.

#### Command-line documentation

The command-line documentation is the first source of information that is
easily accessible using the `numpy.info` command. Don't use the built-in `help`
(or `pydoc` from the shell) because it will mess-up with the C API:

    >>> import numpy
    >>> numpy.info(numpy.sin)
    sin(x[, out])

    Trigonometric sine, element-wise.

    Parameters
    ----------
    x : array_like
        Angle, in radians (:math:`2 \pi` rad equals 360 degrees).
    ...

#### Online documentation

The numpy documentation is quite extensive and is made of several different
guides. The most useful one is probably the [Numpy Reference Guide].

[Numpy Reference Guide]: https://docs.scipy.org/doc/numpy/reference/

#### Stack overflow

[Stack overflow] is a great resource for answering basic to very advanced and
tricky questions. But it can be intimidating since people are not always nice
with new users. My advice is to really search the site with the `numpy` tag
before asking your question to make sure it has not been alreayd asked. But in
the meantime, you'll realize that properly asking a question may help you to
solve the question.

[Stack overflow]: http://stackoverflow.com/questions/tagged/numpy

#### Mailing lists





## Chapter 1 - Introduction
### About the author

Nicolas P. Rougier is a full-time research scientist at Inria which is the
French national institute for research in computer science and control. This is
a public scientific and technological establishment (EPST) under the double
supervision of the Research & Education Ministry, and the Ministry of Economy
Finance and Industry. Nicolas P. Rougier is working within the Mnemosyne
project which lies at the frontier between integrative and computational
neuroscience in association with the Institute of Neurodegenerative Diseases,
the Bordeaux laboratory for research in computer science (LaBRI), the
University of Bordeaux and the national center for scientific research (CNRS).
  
He has been using Python for more than 15 years and Numpy for more than 10
years (approximately) for modeling in Neuroscience, machine learning and for
advanced visualization (OpenGL). Of course, you can have 10 or 15 years
experience in something and still have no clue on how things work. However,
Nicolas is the author of several online resources and tutorials (Matplotlib,
Numpy, OpenGL) that have became references in the scientific community. He's
also teaching Python, Numpy and scientific visualization at the University of
Bordeaux and in various conferences worldwide (SciPy, EuroScipy, etc). He's
also the author of the popular article "Ten Simple Rules for Better Figures".

### Why another book on Numpy ?

There is already a fair number of book about Numpy (see bibliography) and a
legitimate question is to wonder if another book is really necessary. As you
may have guessed by reading these lines, my personal answer is yes, mostly
because I think there's room for a different approach concentrating on the
migration from Python to Numpy through vectorization. There is actually a lot
of techniques that you don't find in books and such techniques are mostly
learned through experience. The goal of this book is to explain some of them
and to make you acquire experience.

This book is freely available on the web via github as well as through my
homepage. A paper version can be bought if you really hate trees but if you
really insist on giving me some money, consider buying an electronic version
instead. Or buy a paper book but plant a tree and/or eat a beaver...

### Pre-requisites

This is not a beginner guide.  
You should have an intermediate level in both Python and Numpy.  
If you're an advanced user, you'll be bored to death.

### Resources

* Command-line documentation
* Online documentation
* Online tutorials
* Mailing lists
* Stack overflow
* Conferences (SciPy, EuroSciPy, SciPy India)
* Books / Tutorial / Articles
* Contributing to Numpy

### Conventions

We'll use usual naming conventions. If not stated explicitely, each script
should import numpy, scipy and matplotlib as:
  
    import numpy as np
    import scipy as sp
    import matplotlib.pyplot as plt



## Chapter 2 - Anatomy of an array
### Introduction

Let's consider a simple 2D array and check what kind of information we can get
from it:

    Z = np.arange(5*5).reshape(5,5)
    
You're probably familiar with the most common properties such as shape, dtype, size or
length:

    >>> print(Z.shape)
    (5,5)
    >>> print(Z.dtype)
    dtype('64')
    >>> print(Z.size)
    25
    >>> print(len(Z))
    5

However, some other properties are lesser known or utilized:

    >>> print(Z.itemsize)
    8
    >>> print(Z.flags)
      C_CONTIGUOUS : True
      F_CONTIGUOUS : False
      OWNDATA : False
      WRITEABLE : True
      ALIGNED : True
      UPDATEIFCOPY : False
    >>> print(Z.strides)
    (40,8)


Let's write a `print_info` function that print most of the relevant information:

    >>> print_info(Z)
    ------------------------------
    Interface (item)
      shape:       (5, 5)
      dtype:       int64
      size:        25
      order:       ☑ C  ☐ Fortran

    Memory (byte)
      item size:   8
      array size:  200
      strides:     (40, 8)

    Property
      own data:    ☐ Yes  ☑︎ No
      writeable:   ☑ Yes  ☐︎ No
      contiguous:  ☑ Yes  ☐︎ No
      aligned:     ☑ Yes  ☐︎ No
    ------------------------------

### Numpy architecture

    → What is numpy useful for
    → Universal functions
    → Mixing C, Fortran and Python

### Broadcasting principles

From the numpy documentation, we can read that there are 4 broadcasting rules:

1. All input arrays with ndim smaller than the input array of largest ndim,
   have 1's prepended to their shapes.
2. The size in each dimension of the output shape is the maximum of all the
   input sizes in that dimension.
3. An input can be used in the calculation if its size in a particular
   dimension either matches the output size in that dimension, or has value
   exactly 1.
4. If an input has a dimension size of 1 in its shape, the first data entry in
   that dimension will be used for all calculations along that dimension. In
   other words, the stepping machinery of the ufunc will simply not step along
   that dimension (the stride will be 0 for that dimension).

 → Intuitive broadcasting  
 → Weird broadcasting  
 → Strides madness  
 → Exercises  
    
### Vectorization philosophy

Let's consider a simple problem. Given two vectors `X` and `Y`, you have to
compute the sum of `X[i]*Y[j]` for all pairs of indices `i`, `j`. One simple
and obvious solution might to write:

    def compute_1(X, Y):
        result = 0
        for i in range(len(X)):
            for j in range(len(Y)):
                result += X[i] * Y[j]
        return result
    
However, this first and naive implementation requires two loops and you already
know it will be slow.

    >>> X = np.arange(1000)
    >>> timeit("compute_1(X,X)")
    1 loops, best of 3: 0.274481 sec per loop

The question is "how to vectorize the problem?" If you remember your linear
algebra course, you may have identified the expression `X[i] * Y[j]` to be very
similar to a matrix product expression. So maybe we could benefit from some
numpy speedup. One wrong solution would be to write:

    def compute_2(X, Y):
        return (X*Y).sum()
  
This is wrong because the `X*Y` expression will actually compute a new vector Z
such that `Z[i] = X[i] * Y[i]` and this is not what we want. Instead, we can
exploit numpy broadcasting by first reshaping the two vectors and then multiply
them:
  
    def compute_2(X, Y):
        Z = X.reshape(len(X),1) * Y.reshape(1,len(Y))
        return Z.sum()
  
Here we have `Z[i,j] == X[i]*Y[j]` and if we take the sum over ech elements of
Z, we get the expected result. Let's see how much speedup we gain in the
process:
  
    >>> X = np.arange(1000)
    >>> timeit("compute_2(X,X)")
    10 loops, best of 3: 0.00157926 sec per loop
  
This is better, we almost gained a factor of 100. But we can do much better. If
you look more closely at the pure Python version, you can see that the inner
loop is using `X[i]` that does not depend on the `j` index, meaning it can be
removed from the inner loop. Code can be rewritten as:

    def compute_3(X, Y):
        result = 0
        for i in range(len(X)):
            Ysum = 0
            for j in range(len(Y)):
                Ysum += Y[j]
            result += X[i]*Ysum
        return result

But since the inner loop does not depend on the `i` index, we might as well
compute it only once:

    def compute_3(X, Y):
        result = 0
        Ysum = 0
        for j in range(len(Y)):
            Ysum += Y[j]
        for i in range(len(X)):
            result += X[i]*Ysum
        return result

Not so bad, we have removed one loop. What about the other? Using the same
approach, we can write:

    def compute_3(x, y):
        Ysum = = 0
        for j in range(len(Y)):
            Ysum += Y[j]
        Xsum = = 0
        for i in range(len(X)):
            Xsum += X[i]
        return Xsum*Ysum

Finally, having realized we only need the product of the sum over X and Y respectively, 
we can benefit from the `np.sum` function and write:

    def compute_3(x, y):
        return np.sum(y) * np.sum(x)
    
It is shorter, clearear and much faster:

    >>> X = np.arange(1000)
    >>> timeit("compute_3(X,X)")
    1000 loops, best of 3: 3.97208e-06 sec per loop

What we've learned from this simple example is that there is two kinds of
vectorization, the vectorization of your problem and the vectorization of your
code. The first is the most difficult but the most important because this is
where you can expect huge gains in speed. But the latter is nonetheless
important because you can speedup your code even more. For example, let's
rewrite the last solution the Python way:

    def compute_4(x, y):
        return sum(x)*sum(y)

    >>> X = np.arange(1000)
    >>> timeit("compute_4(X,X)")
    1000 loops, best of 3: 0.000155677 sec per loop
    
This new Python version is much faster than the previous one, but still, it is
10x slower than the numpy version. 

### Readability vs optimization

    → Einsum notation
    → NumExpr
    → Unit-tests
    


### Conclusion
## Chapter 3 - Crafting new tools
### Introduction
### Benchmark, copy and view
### Typed lists
### Circular arrays
### Memory aware arrays
### Emulating double precision
### Conclusion
## Chapter 4 - Code vectorization
### Introduction
### Fractals
### Cellular automata
### Reaction diffusion
### Earthquake visualization
### Conclusion
## Chapter 5 - Problem vectorization
### Introduction
### Particles
### Maze solving
### Fluid simulation
### Artificial Neural Networks
### Conclusion
## Chapter 6 - Beyon Numpy
### Introduction
### Python made fast
    See http://yasermartinez.com/blog/posts/numpy-programming-challenge.html
### Cython
    See http://cython.org
    and https://github.com/ianozsvald/Mandelbrot_pyCUDA_Cython_Numpy/
### OpenGL
    See http://glumpy.github.io
### Other resources
    Scikits (learn, images, etc.), Pandas, PyTables

### Conclusion
## Bibliography
### Articles

* Python for Scientific Computing
  Travis E. Oliphant
  Computing in Science & Engineering, 9, 2007.

* The NumPy array: a structure for efficient numerical computation
  Stéfan van der Walt, Chris Colbert & Gael Varoquaux
  Computing in Science and Engineering, 13(2), 2011.
  
* Vectorised algorithms for spiking neural network simulation
  Romain Brette	& Dan F. M. Goodman
  Neural Computation, 23(6), 2010.

### Tutorials

* Quickstart tutorial  
  https://docs.scipy.org/doc/numpy-dev/user/quickstart.html

* Numpy medkits  
  http://mentat.za.net/numpy/numpy_advanced_slides/

* Numpy tutorial  
  http://www.labri.fr/perso/nrougier/teaching/numpy/numpy.html

* An introduction to Numpy and Scipy  
  https://engineering.ucsb.edu/~shell/che210d/numpy.pdf

* Python Numpy tutorial  
  http://cs231n.github.io/python-numpy-tutorial/

* 100 Numpy exercices  
  http://www.labri.fr/perso/nrougier/teaching/numpy.100/index.html
  
* DataCamp Numpy  
  https://www.datacamp.com/courses/intro-to-python-for-data-science/chapter-4-numpy-python

* Python course  
  http://www.python-course.eu/numpy.php

### Books

* Elegant SciPy: The Art of Scientific Python  
  Juan Nunez-Iglesias, Stéfan van der Walt, Harriet Dashnow, O'Reilly, 2016  
  http://shop.oreilly.com/product/0636920038481.do

* Guide to NumPy  
  Travis Oliphant, 2006
  http://csc.ucdavis.edu/~chaos/courses/nlp/Software/NumPyBook.pdf
  
* SciPy and NumPy  
  Eli Bressert, O'Reilly Media, Inc., 2012
  https://www.safaribooksonline.com/library/view/scipy-and-numpy/9781449361600/

* Python for Data Analysis  
  Wes McKinney, O'Reilly Media, Inc., 2012
  https://www.safaribooksonline.com/library/view/python-for-data/9781449323592/

* Learning NumPy Array  
  Ivan Idris, Packt Publishing, 2014  
  https://www.packtpub.com/application-development/learning-numpy-array

* NumPy: Beginner's Guide  
  Ivan Idris, Packt Publishing, 2013  
  https://www.packtpub.com/big-data-and-business-intelligence/numpy-beginner’s-guide-second-edition

* NumPy Cookbook
  Ivan Idris, Packt Publishing, 2015  
  https://www.packtpub.com/big-data-and-business-intelligence/numpy-cookbook-second-edition

* NumPy Essentials  
  Leo (Liang-Huan) Chin, Tanmay Dutta, Packt Publishing, 2016  
  https://www.packtpub.com/big-data-and-business-intelligence/numpy-essentials




## Practice
### First steps

    See https://gist.github.com/rougier/e5eafc276a4e54f516ed5559df4242c0
    
    * Naive Mandelbrot (python)
    * Fast Mandelbrot (numpy)
    * Fractal dimension (python)
    * Fractal dimension (numpy)

### Artificial Neural Networks
    See https://github.com/rougier/neural-networks
 
    * Perceptron
    * Multi-Layer Perceptron
    * Self-Organizing Map
    
### Typed lists (ragged arrays)

    * Numpy: array subclass
    * Python lists
    * Numpy typed lists

### Differential equations

    * Numpy: broadcasting
    * Simple equation
    * Differential equation

### Heat diffusion
    See https://github.com/HarrietInc/elegant-scipy-submissions/issues/21
    
    
### Fluid simulation

    * Particle approach
    * Python implementation
    * Grid-based approach
    * Numpy implementation
    
### Particles
    See http://api.vispy.org/en/v0.2.1/examples/demo/boids.html

    * Scipy: KDTree
    * Boids
    * Python implementation
    * Numpy implementation

### Maze solving
    See https://github.com/HarrietInc/elegant-scipy-submissions/issues/20
    and http://bryukh.com/labyrinth-algorithms/
    
    * Numpy: generic filter
    * Building a maze
    * Bellman-Ford algorithm
    * Python implementation
    * Numpy implementation
        
### Cellular automata
    See http://www.labri.fr/perso/nrougier/teaching/numpy/numpy.html
    
    * Numpy: Fast Fourier Transform
    * Game of Life (python / numpy)
    * Reaction diffusion (python / numpy)


### Earthquake visualization
    See http://www.labri.fr/perso/nrougier/teaching/matplotlib/matplotlib.html
    
    * Numpy: Circular arrays
    * It's raining again
    * Earthquakes from the past 7 days



