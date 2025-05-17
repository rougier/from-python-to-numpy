.. ----------------------------------------------------------------------------
.. Title:   From Python to Numpy
.. Author:  Nicolas P. Rougier
.. Date:    January 2017
.. License: Creative Commons Share-Alike Non-Commercial International 4.0
.. ----------------------------------------------------------------------------

.. meta::
   :description: An open-source book about numpy vectorization techniques, based on experience, practice and descriptive examples
   :viewport: width=device-width, initial-scale=1, maximum-scale=1

.. |date| date::  %B %Y
   
===============================================================================
                             From Python to Numpy                              
===============================================================================

Copyright (c) 2021 - Nicolas P. Rougier <Nicolas.Rougier@inria.fr>  & Loïc Houpert <loic@lhoupert.fr>

.. default-role:: code

.. container:: title-logos

   .. image:: data/cc.large.png
      :width: 40px
   .. image:: data/by.large.png
      :width: 40px
   .. image:: data/sa.large.png
      :width: 40px
   .. image:: data/nc.large.png
      :width: 40px

   |
   | Latest version - |date|
   | DOI: `10.5281/zenodo.225783 <http://doi.org/10.5281/zenodo.225783>`_

.. ----------------------------------------------------------------------------
.. container:: title-logos

   .. image:: data/cubes.png
      :width: 100%

.. ----------------------------------------------------------------------------

There are already a fair number of books about Numpy (see Bibliography_) and a
legitimate question is to wonder if another book is really necessary. As you
may have guessed by reading these lines, my personal answer is yes, mostly
because I think there is room for a different approach concentrating on the
migration from Python to Numpy through vectorization. There are a lot of
techniques that you don't find in books and such techniques are mostly learned
through experience. The goal of this book is to explain some of these
techniques and to provide an opportunity for making this experience in the
process.

**Website:** http://www.labri.fr/perso/nrougier/from-python-to-numpy


.. ----------------------------------------------------------------------------
.. contents:: **Table of Contents**
   :class: main-content
   :depth: 2

|
|

**Disclaimer:** All external pictures should have associated credits. If there
are missing credits, please tell me, I will correct it. Similarly, all excerpts
should be sourced (wikipedia mostly). If not, this is an error and I will
correct it as soon as you tell me.


The book is open-access (you're reading it) but **if you insist on buying it**,
my advice would be to read it first and then decide if you still want to buy it
(!?). If this is the case, you can do it via `Paypal
<https://www.paypal.me/NicolasPRougier/>`_, price is free (`5 euros
<https://www.paypal.me/NicolasPRougier/5>`_, `10 euros
<https://www.paypal.me/NicolasPRougier/10>`_, `25 euros
<https://www.paypal.me/NicolasPRougier/25>`_). You won't get anything extra but
it might help me with the writing of the upcoming **Python and OpenGL for
Scientific Visualization** (May 2018).


.. ----------------------------------------------------------------------------
.. |WIP| image:: https://img.shields.io/badge/status-WIP-orange.svg?style=flat-square

.. ----------------------------------------------------------------------------
.. include:: 01-preface-with-jupyter-book.rst
.. include:: 02-introduction.rst
.. include:: 03-anatomy.rst
.. include:: 04-code-vectorization.rst
.. include:: 05-problem-vectorization.rst
.. include:: 06-custom-vectorization.rst
.. include:: 07-beyond-numpy.rst
.. include:: 08-conclusion.rst
.. include:: 09-quick-reference.rst
.. include:: 10-bibliography.rst


.. --- Compilation ------------------------------------------------------------
.. rst2html.py --link-stylesheet --stylesheet=markdown.css book.rst book.html
