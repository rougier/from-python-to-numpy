# From Python to NumPy
  Nicolas P. Rougier, 2017

## Introduction
### About the author

  Nicolas P. Rougier is a full-time research scientist at Inria which is the
  French national institute for research in computer science and control. This
  is a public scientific and technological establishment (EPST) under the
  double supervision of the Research & Education Ministry, and the Ministry of
  Economy Finance and Industry. Nicolas P. Rougier is working within the
  Mnemosyne project which lies at the frontier between integrative and
  computational neuroscience in association with the Institute of
  Neurodegenerative Diseases, the Bordeaux laboratory for research in computer
  science (LaBRI), the University of Bordeaux and the National Center for
  scientific research (CNRS).
  
  He has been using Python for more than 15 years and Numpy for more than 10
  years (approximately) for modeling in Neuroscience, machine learning and for
  advanced visualization (OpenGL). He's the author of several online resources
  and tutorials (matplotlib, numpy, openGL) that have became references in the
  scientific community. He's also teaching Python, Numpy and scientific
  visualization at the University of Bordeaux as well as in various conferences
  worldwide (SciPy, EuroScipy). He's also the author of the very popular
  article "Ten Simple Rules for Better Figures".

### Why another book on Numpy ?

  There is already a fair number of book about Numpy (see bibliography) and a
  legitimate question is to wonder if another book is really necessary. As you
  may have guessed while reading these lines, my personal answer is yes, mostly
  because I think there's room for a different approach, concentrating on the
  migration from Python to Numpy through vectorization. There is actually a lot
  of techniques that you don't find in books and such techniques are mostly
  learned through experience. The goal of this book is to explain some of them.

### Pre-requisites

  This is not a beginner guide.
  You should have an intermediate level in both Python and Numpy.
  
### Conventions

We'll use usual naming conventions. If not stated explicitely, each script
should import numpy, scipy and matplotlib as:
  
    import numpy as np
    import scipy as sp
    import matplotlib.pyplot as plt
    
Furthermore, we'll measuring time performances quite a lot of time and we'll be
using an elapsed timer context manager:
    
    from timeit import default_timer
    from contextlib import contextmanager

    @contextmanager
    def elapsed_timer():
        start = default_timer()
        elapser = lambda: default_timer() - start
        yield lambda: elapser()
        end = default_timer()
        elapser = lambda: end-start


## Theory
### Introduction

    → History & timeline
    
### Numpy architecture

    → What is numpy useful for
    → Universal functions
    → Mixing C, Fortran and Python
    
### Anatomy of an array
    → Memory layout
    → Strides
    → Copy and view
    → Exercises
    
### Broadcasting principles

    → Intuitive broadcasting
    → Weird broadcasting
    → Strides madness
    → Exercises
    
### Vectorization philosophy

    → Theoretical vectorization
    → Practical vectoration 
    → Memory vs speed
    → Exercises
    
  Let's consider a simple problem where, given two vectors `X` and `Y`, you
  have to compute the sum of `X[i]*Y[j]` for all pairs of indices `i`, `j`. One
  simple obvious solution might be written as:
            
  ```
  # Right, but slow
  def compute_1(x, y):
      result = 0
      for i in range(len(x)):
          for j in range(len(y)):
              result += x[i] * y[j]
      return result
  ```
    
  However, this first (very) naive implementation requires two loops and you
  already know it will be slow.
  
  ```
  import timeit
  
  X = np.arange(1000)
  timeit.timeit("compute(X,X)", globals=globals(), number=1000000)
  ```
  
  The question is "how to vectorize the problem?"
  
  If you remember your linear algebra course, you may have identified the
  expression `X[i] * Y[j]` to be very similar to a matrix product
  expression. So maybe we could benefit from some numpy speedup. One wrong
  solution would be to write:
  
  ```
  # Wrong
  def compute(X, Y):
      Z = X * Y
      return Z.sum()
  ```
  
  This is wrong because the `X*Y` epxression will actually compute a new vector
  Z such that `Z[i] = X[i] * Y[i]` and this is not what we want. Instead, we
  have to exploit numpy broadcasting by first reshaping the two vectors and
  then multiply them:
  
  ```
  # Right & fast
  def compute(X, Y):
      Z = X.reshape(len(X),1) * Y.reshape(1,len(Y))
      return Z.sum()
  ```
  
  Here we have `Z[i,j] == X[i]*Y[j]` and if we make the sum over Z, we have the
  expected result. Let's see how much speedup we gain in the process:
  
  
  
  
  
  Looking at the above code, there is no obvious way to do that. But, if you
  look more closely, you can realize that the inner loop is using `x[i]` that
  does not depend on the `j` index, meaning it can be removed from the inner
  loop. Code can be rewritten as:

  ```
  def compute(x, y):
      result = 0
      for i in range(len(x)):
          ysum = 0
          for j in range(len(y)):
               ysum += y[j]
          result += x[i]*ysum
      return result
  ```

  But then, instead of using a loop to compute the sum over y, we can now use
  the `numpy.sum` method:

  ```
  def compute(x, y):
      result = 0
      for i in range(len(x)):
          result += x[i]*np.sum(y)
      return result
  ```
    
  Not so bad, we have removed one loop. What about the other? Using the same
  approach, we can also realize that there's no need to compute the sum over y
  at each iteration. It would be better to compute it once and save it in a
  variable:

  ```
  def compute(x, y):
      result = 0
      ysum = np.sum(y)
      for i in range(len(x)):
          result += x[i]*ysum
      return result
  ```
    
  Finally, it's now obvious that the loop is computing the sum over x and we
  can factorize the ysum outside the loop. Our final code is then:
    
  ```
  def compute(x, y):
      return np.sum(y) * np.sum(x)
  ```
    
  It is shorter, clearear and much, much faster !
    
    
    
### Readability vs optimization

    → Einsum notation
    → NumExpr
    → Unit-tests
    
### Numpy resources

    → Command-line documentation
    → Online documentation
    → Online tutorials
    → Mailing lists
    → Stack overflow
    → Conferences (SciPy, EuroSciPy, SciPy India)
    → Books / Tutorial / Articles
    → Contributing to Numpy

### Other resources

    → Scikits (learn, images, etc.)
    → Pandas
    → PyTables


## Practice
### Introduction
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


## Beyond Numpy
### Introduction
### Python
    See http://yasermartinez.com/blog/posts/numpy-programming-challenge.html
### Cython
    See http://cython.org
     and https://github.com/ianozsvald/Mandelbrot_pyCUDA_Cython_Numpy/
### OpenGL
    See http://glumpy.github.io
### CUDA / OpenCL


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
