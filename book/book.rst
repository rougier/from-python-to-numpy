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

   .. image:: ../data/cc.large.png
      :width: 40px
   .. image:: ../data/by.large.png
      :width: 40px
   .. image:: ../data/sa.large.png
      :width: 40px
   .. image:: ../data/nc.large.png
      :width: 40px


.. ----------------------------------------------------------------------------

There is already a fair number of book about Numpy (see Bibliography_) and a
legitimate question is to wonder if another book is really necessary. As you
may have guessed by reading these lines, my personal answer is yes, mostly
because I think there's room for a different approach concentrating on the
migration from Python to Numpy through vectorization. There is a lot of
techniques that you don't find in books and such techniques are mostly learned
through experience. The goal of this book is to explain some of them and to
make you acquire experience in the process.

.. ----------------------------------------------------------------------------
.. contents:: **Table of Contents**
   :class: main-content
   :depth: 2

.. ----------------------------------------------------------------------------
.. |WIP| image:: https://img.shields.io/badge/status-WIP-orange.svg?style=flat-square

.. ----------------------------------------------------------------------------
.. include:: preface.rst
.. include:: introduction.rst
.. include:: anatomy.rst
.. include:: code-vectorization.rst
.. include:: problem-vectorization.rst
.. include:: custom-vectorization.rst
.. include:: beyond-numpy.rst
.. include:: conclusion.rst
.. include:: quick-reference.rst
.. include:: bibliography.rst


.. --- Compilation ------------------------------------------------------------
.. rst2html.py --link-stylesheet --stylesheet=markdown.css book.rst book.html
