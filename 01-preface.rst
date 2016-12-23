Preface
===============================================================================

.. contents:: **Contents**
   :local:


About the author
----------------

`Nicolas P. Rougier`_ is a full-time research scientist at Inria_ which is the
French national institute for research in computer science and control. This is
a public scientific and technological establishment (EPST) under the double
supervision of the Research & Education Ministry, and the Ministry of Economy
Finance and Industry. Nicolas P. Rougier is working within the Mnemosyne_
project which lies at the frontier between integrative and computational
neuroscience in association with the `Institute of Neurodegenerative
Diseases`_, the Bordeaux laboratory for research in computer science
(LaBRI_), the `University of Bordeaux`_ and the national center for scientific
research (CNRS_).

He has been using Python for more than 15 years and numpy for more than 10
years for modeling in neuroscience, machine learning and for advanced
visualization (OpenGL). Nicolas P. Rougier is the author of several online
resources and tutorials (Matplotlib, numpy, OpenGL) and he's teaching Python,
numpy and scientific visualization at the University of Bordeaux and in various
conferences and schools worldwide (SciPy, EuroScipy, etc). He's also the author
of the popular article `Ten Simple Rules for Better Figures`_ and a popular
'matplotlib tutorial
<http://www.labri.fr/perso/nrougier/teaching/matplotlib/matplotlib.html>`_.


About this book
---------------

This book has been written in |ReST|_ format and generated using the
`rst2html.py` command line available from the docutils_ python package.

If you want to rebuild the html output, from the top directory, type:

.. code-block::

   $ rst2html.py --link-stylesheet --cloak-email-addresses \
                 --toc-top-backlinks --stylesheet=book.css \
                 book.rst book.html

The sources are available from https://github.com/rougier/from-python-to-numpy.
                   
.. |ReST| replace:: restructured text
.. _ReST: http://docutils.sourceforge.net/rst.html
.. _docutils: http://docutils.sourceforge.net/


Prerequisites
+++++++++++++

This is not a Python beginner guide and you should have an intermediate level in
Python and ideally a beginner level in numpy. If this is not the case, have
a look at the bibliography_ for a curated list of resources.


Conventions
+++++++++++

We will use usual naming conventions. If not stated explicitly, each script
should import numpy, scipy and matplotlib as:

.. code-block:: python
   
   import numpy as np
   import scipy as sp
   import matplotlib.pyplot as plt


We'll use up-to-date versions (at the date of writing, i.e. January, 2017) of the
different packages:

=========== =========
Packages    Version
=========== =========
Python      3.5.2
----------- ---------
Numpy       1.11.2
----------- ---------
Scipy       0.18.1
----------- ---------
Matplotlib  1.5.3
=========== =========

How to contribute
+++++++++++++++++

If you want to contribute to this book, you can:

* Review chapters (please contact me)
* Report issues (https://github.com/rougier/from-python-to-numpy/issues)
* Suggest improvements (https://github.com/rougier/from-python-to-numpy/pulls)
* Correct English (https://github.com/rougier/from-python-to-numpy/issues)
* Design a better and more responsive html template for the book.
* Star the project (https://github.com/rougier/from-python-to-numpy)

Publishing
++++++++++

If you're an editor interested in publishing this book, you can `contact me
<mailto:Nicolas.Rougier@inria.fr>`_ if you agree to have this version and all
subsequent versions open access (i.e. online at `this address
<http://www.labri.fr/perso/nrougier/from-python-to-numpy>`_), you know how to
deal with `restructured text <http://docutils.sourceforge.net/rst.html>`_ (Word
is not an option), you provide a real added-value as well as supporting
services, and more importantly, you have a truly amazing latex book template
(and be warned that I'm a bit picky about typography & design: `Edward Tufte
<https://www.edwardtufte.com/tufte/>`_ is my hero). Still here?


License
--------

**Book**

This work is licensed under a `Creative Commons Attribution-Non Commercial-Share
Alike 4.0 International License <https://creativecommons.org/licenses/by-nc-sa/4.0/>`_. You are free to:

* **Share** — copy and redistribute the material in any medium or format
* **Adapt** — remix, transform, and build upon the material

The licensor cannot revoke these freedoms as long as you follow the license terms.

**Code**

The code is licensed under the `OSI-approved BSD 2-Clause License
<LICENSE-code.txt>`_.


.. --- Links ------------------------------------------------------------------
.. _Nicolas P. Rougier:     http://www.labri.fr/perso/nrougier/
.. _Inria:                  http://www.inria.fr/en
.. _Mnemosyne:              http://www.inria.fr/en/teams/mnemosyne
.. _LaBRI:                  https://www.labri.fr/
.. _CNRS:                   http://www.cnrs.fr/index.php
.. _University of Bordeaux: http://www.u-bordeaux.com/
.. _Institute of Neurodegenerative Diseases:
      http://www.imn-bordeaux.org/en/
.. _Ten Simple Rules for Better Figures:
      http://dx.doi.org/10.1371/journal.pcbi.1003833
.. ----------------------------------------------------------------------------

