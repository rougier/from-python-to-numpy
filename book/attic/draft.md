# From Python to Numpy
  Copyright 2017 - Nicolas P. Rougier

## Preface

## Introduction
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
Bordeaux and in various conferences and schools worldwide (SciPy, EuroScipy,
etc). He's also the author of the popular article Ten Simple Rules for Better
Figures.


### Why another book on Numpy ?

There is already a fair number of book about Numpy (see bibliography) and a
legitimate question is to wonder if another book is really necessary. As you
may have guessed by reading these lines, my personal answer is yes, mostly
because I think there's room for a different approach concentrating on the
migration from Python to Numpy through vectorization. There is actually a lot
of techniques that you don't find in books and such techniques are mostly
learned through experience. The goal of this book is to explain some of them
and to make you acquire experience.

This book is freely available on the web through github. A paper version can be
generated if you really hate trees but it will be out of date a soon as it is
printed.

### Pre-requisites

This is not a beginner guide and you should have an intermediate level in
Python and (at least) a beginner level in Numpy. If this is not the case, have
a look at the bibliography for a curated list of resources.

### Conventions

We will use usual naming conventions. If not stated explicitely, each script
should import numpy, scipy and matplotlib as:

```Python
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
```
 
We'll use up-to-date versions of the different packages at the date of
writing (December, 2016):

| Packages   | Version |
|------------|---------|
| Python     | 3.5.2   |
| Numpy      | 1.11.2  |
| Scipy      | 0.18.1  |
| Matplotlib | 1.5.3   |




## Anatomy of an array
### Introduction
### Numpy architecture
### Broadcasting principles
### Vectorization philosophy
    Simple addition
    Code vs problem vectorization
### Conclusion

## Code vectorization
### Introduction
    Random walk
### Uniform vectorization
    Cellular automata
### Differential vectorization (temporal)
    Mandelbrot example
### Differential vectorization (spatial)
    Boids simulation
### Conclusion
  
## Problem vectorization
### Introduction
### Path finding
    Tree vs Markov
### Smoke simulation
    Particle vs grid
### Poisson disk sampling
    Very slow or very fast
### Conclusion

## Custom vectorization
### Introduction
### Typed list
### Memory aware
### Double precision
### Conclusion

## Beyond Numpy
### Introduction
### Back to Python
    Allocation
### Cython vs Python
    Game of life made faster
### OpenGL made easy
    Glumpy
### Scikits

## Conclusion
## Bibliography
### Tutorials
### Articles
### Books

## Appendix
### A - Quick references
### B - Cheat sheet

