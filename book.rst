.. ----------------------------------------------------------------------------
.. Title:   From Python to Numpy
.. Author:  Nicolas P. Rougier
.. Date:    January 2017
.. License: Creative Commons Share-Alike Non-Commercial International 4.0
.. ----------------------------------------------------------------------------

===============================================================================
                             From Python to Numpy                              
===============================================================================
-------------------------------------------------------------------------------
       Copyright (c) 2017 - Nicolas P. Rougier <Nicolas.Rougier@inria.fr> 
-------------------------------------------------------------------------------

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

   | Version 1.0 - January 2017


.. ----------------------------------------------------------------------------
.. container:: title-logos

   .. image:: data/cubes.png
      :width: 100%

.. ----------------------------------------------------------------------------

There is already a fair number of book about Numpy (see Bibliography_) and a
legitimate question is to wonder if another book is really necessary. As you
may have guessed by reading these lines, my personal answer is yes, mostly
because I think there's room for a different approach concentrating on the
migration from Python to Numpy through vectorization. There is a lot of
techniques that you don't find in books and such techniques are mostly learned
through experience. The goal of this book is to explain some of them and to
make you acquire experience in the process.

**Website:** http://www.labri.fr/perso/nrougier/from-python-to-numpy


.. ----------------------------------------------------------------------------
.. contents:: **Table of Contents**
   :class: main-content
   :depth: 2

|
|

**Disclaimer** All external pictures should have associated credits. If there
are missing credits, please tell me, I will correct it. Similarly, all excerpts
should be sourced (wikipedia mostly). If not, this is an error and I will
correct it as soon as you tell me.
           
.. ----------------------------------------------------------------------------
.. |WIP| image:: https://img.shields.io/badge/status-WIP-orange.svg?style=flat-square

.. ----------------------------------------------------------------------------
.. include:: 01-preface.rst
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
