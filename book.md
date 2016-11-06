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
  migration from Python to Numpy through vectorization.

### Pre-requisites

  This is not a beginner guide.
  You should have an intermediate level in both Python and Numpy.

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
