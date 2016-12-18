Beyond Numpy
===============================================================================

.. contents:: **Contents**
   :local:

Back to Python
--------------

Cython vs Python
----------------

OpenGL made easy
----------------

Scikits
-------

Here is a very short list of packages that are well-maintained, well tested and
may simplify your scientific life (depending on your domain). There are of
course many more and depending on your specific needs, chances are you do not
have to program everything by yourself. But it is a good exercise if you have
some spare time. For an extensive list, have a look at the `Awesome python list
<https://awesome-python.com>`_.

* `scikit-image <http://scikit-image.org>`_ is a Python package dedicated to
  image processing, and using natively NumPy arrays as image objects. This
  chapter describes how to use scikit-image on various image processing tasks,
  and insists on the link with other scientific Python modules such as NumPy
  and SciPy.

* `scikit-learn <http://scikit-learn.org/stable/>`_ is a free software machine
  learning library for the Python programming language. It features various
  classification, regression and clustering algorithms including support vector
  machines, random forests, gradient boosting, k-means and DBSCAN, and is
  designed to interoperate with the Python numerical and scientific libraries
  NumPy and SciPy.
  
* The `Astropy <http://www.astropy.org>`_ project is a community effort to
  develop a single core package for astronomy in Python and foster
  interoperability between Python astronomy packages.

* `Cartopy <http://scitools.org.uk/cartopy/>`_ is a Python package designed to
  make drawing maps for data analysis and visualisation as easy as
  possible. Cartopy makes use of the powerful PROJ.4, numpy and shapely
  libraries and has a simple and intuitive drawing interface to matplotlib for
  creating publication quality maps.

* `Brian <http://www.briansimulator.org>`_ is a free, open source simulator for
  spiking neural networks. It is written in the Python programming language and
  is available on almost all platforms. We believe that a simulator should not
  only save the time of processors, but also the time of scientists. Brian is
  therefore designed to be easy to learn and use, highly flexible and easily
  extensible.


Conclusion
----------

If numpy is a very versatile library, it does not mean you have to use in every
situation. In this chapter, we've seen some alternatives (including Python
itself) that are worth a look. As always, the choice belongs to you and you
have to consider what is the best solution for you in term of development time,
computation time and effort in maintenance. If you design you own solution,
you'll have to test it and to maintain it but in exchange, you're free to
design it the way you want. On the other side, if you decide to rely on a
third-party package, you'll save time in development and benefit from
community-support even though you might have to adapt the package to your
specific needs. The choice is up to you.
