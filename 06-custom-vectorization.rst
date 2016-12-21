

Custom vectorization
===============================================================================

.. contents:: **Contents**
   :local:
      

Introduction
------------

One of the strength of Numpy is that it allows you to `subclass the ndarray
<https://docs.scipy.org/doc/numpy/user/basics.subclassing.html>`_ object.  The
process is a bit tedious but it is worth the effort because it allows you to
create new objects that suit perfectly your problem. We'll examine in the
following section two real-word cases (typed list and memory aware) that are
extensively used in the `glumpy <http://glumpy.github.io>`_ project while the
last one (double precision array) is a more academic case.


Typed list
----------

Typed list (also known as ragged array) is a list of items that all have the
same data type (in the sense of numpy). They offer both the list and ndarray
API (with some restriction of course). Since respective API may be not
compatible in some cases, we have to make some choices:

.. code:: python

   >>> l = TypedList(int)
   >>> l.append([1,2])
   >>> l.append([3])
   >>> print(l)
   [1, 2], [3]
   >>> print(l+1)
   [2, 3], [4]

For the `+` operator, we'll choose to use Numpy API where the value is added to
each individual item instead of expanding the list by appending a new item
(`1`).
   

..
   We would like to define a typed list object such that if offers both the Python
   list API and the Numpy array API (with some restriction of course). We would
   like for example to be able to write:


   We first need to subclass the ndarray object and define a new init method.


   .. code::
      :class: output

      ╌╌╌╌┬───┬───┬───┐┌───┬───┬───┬───┬───┐┌───┬───┬╌╌╌╌╌
          │ 0 │ 1 │ 6 ││ 3 │ 2 │ 0 │ 0 │ 5 ││ 3 │ 4 │
       ╌╌╌┴───┴───┴───┘└───┴───┴───┴───┴───┘└───┴───┴╌╌╌╌╌╌
             item 1           item 2          item 3


Memory aware array
------------------


Double precision array
----------------------


Conclusion
----------

