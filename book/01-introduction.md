## Introduction

* [About the author](#about)
* [Why another book on Numpy ?](#why)
* [Pre-requisites](#pre-requisites)
* [Conventions](#conventions)
* [Contribute](#contribute)

### About the author <a name="about"></a>

[Nicolas P. Rougier](http://www.labri.fr/perso/nrougier/) is a full-time
research scientist at Inria which is the French national institute for research
in computer science and control. This is a public scientific and technological
establishment (EPST) under the double supervision of the Research & Education
Ministry, and the Ministry of Economy Finance and Industry. Nicolas P. Rougier
is working within the Mnemosyne project which lies at the frontier between
integrative and computational neuroscience in association with the Institute of
Neurodegenerative Diseases, the Bordeaux laboratory for research in computer
science (LaBRI), the University of Bordeaux and the national center for
scientific research (CNRS).
  
He has been using Python for more than 15 years and Numpy for more than 10
years (approximately) for modeling in Neuroscience, machine learning and for
advanced visualization (OpenGL). Of course, you can have 10 or 15 years
experience in something and still have no clue on how things work. However,
Nicolas is the author of several online resources and tutorials (Matplotlib,
Numpy, OpenGL) that have became references in the scientific community. He's
also teaching Python, Numpy and scientific visualization at the University of
Bordeaux and in various conferences and schools worldwide (SciPy, EuroScipy,
etc). He's also the author of the popular article [Ten Simple Rules for Better
Figures](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833).

### Why another book on Numpy ? <a name="why"></a>

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

### Pre-requisites <a name="pre-requisites"></a>

This is not a beginner guide and you should have an intermediate level in
Python and (at least) a beginner level in Numpy. If this is not the case, have
a look at the [bibliography][bibliography.md] chapter for a curated list of
resources.

### Conventions <a name="conventions"></a>

We'll use usual naming conventions. If not stated explicitely, each script
should import numpy, scipy and matplotlib as:
  
    import numpy as np
    import scipy as sp
    import matplotlib.pyplot as plt
 
We'll use up-to-date versions of the different packages at the date of
writing (November 11, 2016):

| Packages   | Version |
|------------|---------|
| Python     | 3.5.2   |
| Numpy      | 1.11.2  |
| Scipy      | 0.18.1  |
| Matplotlib | 1.5.3   |

### Contribute <a name="contribute"></a>

If you want to contribute to this book, you can send pull requests to improve
the book, correct my English or fix the code. Of course, if you have
better/faster implementation for some of the exercises, you're also welcome.
