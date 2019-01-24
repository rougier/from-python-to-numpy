
Bibliography
===============================================================================

This is a curated list of some NumPy related resources (articles, books &
tutorials) addressing different aspects of NumPy. Some are very specific to
NumPy/Scipy while some others offer a broader view on numerical computing.

.. contents:: **Contents**
   :local:
      

Tutorials
---------

.. |tutorial-1| replace:: 100 Numpy exercises
.. _tutorial-1: http://www.labri.fr/perso/nrougier/teaching/numpy.100/index.html

.. |tutorial-2| replace:: Numpy tutorial
.. _tutorial-2: http://www.labri.fr/perso/nrougier/teaching/numpy/numpy.html

.. |tutorial-3| replace:: Python course
.. _tutorial-3: http://www.python-course.eu/numpy.php

.. |tutorial-4| replace:: An introduction to Numpy and Scipy
.. _tutorial-4: https://engineering.ucsb.edu/~shell/che210d/numpy.pdf

.. |tutorial-5| replace:: Python Numpy tutorial
.. _tutorial-5: http://cs231n.github.io/python-numpy-tutorial/

.. |tutorial-6| replace:: Quickstart tutorial
.. _tutorial-6: https://docs.scipy.org/doc/numpy/user/quickstart.html

.. |tutorial-7| replace:: Numpy medkits
.. _tutorial-7: http://mentat.za.net/numpy/numpy_advanced_slides/

* |tutorial-1|_, Nicolas P. Rougier, 2016.
* |tutorial-2|_, Nicolas P. Rougier, 2015.
* |tutorial-3|_, Bernd Klein, 2015.
* |tutorial-4|_, M. Scott Shell, 2014.
* |tutorial-5|_, Justin Johnson, 2014.
* |tutorial-6|_, Numpy developers, 2009.
* |tutorial-7|_, Stéfan van der Walt, 2008.

  
Articles
--------

.. |article-1|
   replace:: Python for Scientific Computing
.. _article-1: http://dl.acm.org/citation.cfm?id=1251830

.. |article-2|
   replace:: The NumPy array: a structure for efficient numerical computation
.. _article-2: https://hal.inria.fr/inria-00564007/document

.. |article-3|
   replace:: Vectorised algorithms for spiking neural network simulation
.. _article-3: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.397.6097


* | |article-2|_
  | Stéfan van der Walt, Chris Colbert & Gael Varoquaux,
    Computing in Science and Engineering, 13(2), 2011.

  .. container:: abstract

     In the Python world, NumPy arrays are the standard representation for
     numerical data and enable efficient implementation of numerical
     computations in a high-level language. As this effort shows, NumPy
     performance can be improved through three techniques: vectorizing
     calculations, avoiding copying data in memory, and minimizing operation
     counts.

* | |article-3|_
  | Romain Brette & Dan F. M. Goodman,
    Neural Computation, 23(6), 2010.

  .. container:: abstract

     High-level languages (Matlab, Python) are popular in neuroscience because
     they are flexible and accelerate development. However, for simulating
     spiking neural networks, the cost of interpretation is a bottleneck. We
     describe a set of algorithms to simulate large spiking neural networks
     efficiently with high-level languages using vector-based operations. These
     algorithms constitute the core of Brian, a spiking neural network
     simulator written in the Python language. Vectorized simulation makes it
     possible to combine the flexibility of high-level languages with the
     computational efficiency usually associated with compiled languages.

* | |article-1|_
  | Travis E. Oliphant,
    Computing in Science & Engineering, 9(3), 2007.

  .. container:: abstract

     By itself, Python is an excellent "steering" language for scientific codes
     written in other languages. However, with additional basic tools, Python
     transforms into a high-level language suited for scientific and
     engineering code that's often fast enough to be immediately useful but
     also flexible enough to be sped up with additional extensions.
  

Books
-----

.. |book-1| replace:: Python Data Science Handbook
.. _book-1: http://shop.oreilly.com/product/0636920034919.do

.. |book-2| replace:: Elegant SciPy: The Art of Scientific Python
.. _book-2: http://shop.oreilly.com/product/0636920038481.do

.. |book-3| replace:: Guide to NumPy
.. _book-3: http://csc.ucdavis.edu/~chaos/courses/nlp/Software/NumPyBook.pdf

.. |book-4| replace:: Learning IPython for Interactive Computing and Data Visualization
.. _book-4: https://www.packtpub.com/big-data-and-business-intelligence/learning-ipython-interactive-computing-and-data-visualization-sec

.. |book-5| replace:: SciPy and NumPy
.. _book-5: https://www.safaribooksonline.com/library/view/scipy-and-numpy/9781449361600/

.. |book-6| replace:: Python for Data Analysis
.. _book-6: http://shop.oreilly.com/product/0636920023784.do

.. |book-7| replace:: SciPy Lecture Notes
.. _book-7: http://www.scipy-lectures.org


* | |book-7|_,
  | Gaël Varoquaux, Emmanuelle Gouillart, Olav Vahtras et al., 2016.

  .. container:: abstract

     One document to learn numerics, science, and data with Python.  Tutorials
     on the scientific Python ecosystem: a quick introduction to central tools
     and techniques. The different chapters each correspond to a 1 to 2 hours
     course with increasing level of expertise, from beginner to expert.


* | |book-1|_
  | Jake van der Plas, O'Reilly, 2016.

  .. container:: abstract
                   
     The Python Data Science Handbook provides a reference to the breadth of
     computational and statistical methods that are central to data—intensive
     science, research, and discovery. People with a programming background who
     want to use Python effectively for data science tasks will learn how to
     face a variety of problems: for example, how can you read this data format
     into your script? How can you manipulate, transform, and clean this data?
     How can you use this data to gain insight, answer questions, or to build
     statistical or machine learning models?
  
* | |book-2|_
  | Juan Nunez-Iglesias, Stéfan van der Walt, Harriet Dashnow, O'Reilly, 2016.

  .. container:: abstract
                   
     Welcome to Scientific Python and its community! With this practical book,
     you'll learn the fundamental parts of SciPy and related libraries, and get
     a taste of beautiful, easy-to-read code that you can use in practice. More
     and more scientists are programming, and the SciPy library is here to
     help.  Finding useful functions and using them correctly, efficiently, and
     in easily readable code are two very different things. You'll learn by
     example with some of the best code available, selected to cover a wide
     range of SciPy and related libraries—including scikit-learn, scikit-image,
     toolz, and pandas.

* | |book-4|_
  | Cyrille Rossant, Packt Publishing, 2015.

  .. container:: abstract

     This book is a beginner-friendly guide to the Python data analysis
     platform. After an introduction to the Python language, IPython, and the
     Jupyter Notebook, you will learn how to analyze and visualize data on
     real-world examples, how to create graphical user interfaces for image
     processing in the Notebook, and how to perform fast numerical computations
     for scientific simulations with NumPy, Numba, Cython, and ipyparallel. By
     the end of this book, you will be able to perform in-depth analyses of all
     sorts of data.

* | |book-5|_
  | Eli Bressert, O'Reilly Media, Inc., 2012

  .. container:: abstract

     Are you new to SciPy and NumPy? Do you want to learn it quickly and easily
     through examples and concise introduction? Then this is the book for
     you. You’ll cut through the complexity of online documentation and
     discover how easily you can get up to speed with these Python libraries.
 
* | |book-6|_
  | Wes McKinney, O'Reilly Media, Inc., 2012.

  .. container:: abstract

     Looking for complete instructions on manipulating, processing, cleaning,
     and crunching structured data in Python? This hands-on book is packed
     with practical cases studies that show you how to effectively solve a
     broad set of data analysis problems, using several Python libraries.*

* | |book-3|_
  | Travis Oliphant, 2006

  .. container:: abstract

     This book only briefly outlines some of the infrastructure that surrounds
     the basic objects in NumPy to provide the additional functionality
     contained in the older Numeric package (i.e. LinearAlgebra, RandomArray,
     FFT). This infrastructure in NumPy includes basic linear algebra routines,
     Fourier transform capabilities, and random number generators. In addition,
     the f2py module is described in its own documentation, and so is only
     briefly mentioned in the second part of the book.
