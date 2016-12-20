Anatomy of an array
===============================================================================

.. contents:: **Contents**
   :local:
      
Data type
---------

Memory layout
-------------

View and copy
-------------

Let's consider two vectors `Z1` and `Z2`. We would like to know if `Z2` is a
view of `Z1` and if yes, what is this view ? Let's consider a simple example:

.. code-block::

   >>> Z1 = np.arange(10)
   >>> Z2 = Z1[1:-1:2]

.. code-block::
   :class: output

      ╌╌╌┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬╌╌
   Z1    │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │
      ╌╌╌┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴╌╌
      ╌╌╌╌╌╌╌┬───┬╌╌╌┬───┬╌╌╌┬───┬╌╌╌┬───┬╌╌╌╌╌╌╌╌╌╌
   Z2        │ 1 │   │ 3 │   │ 5 │   │ 7 │
      ╌╌╌╌╌╌╌┴───┴╌╌╌┴───┴╌╌╌┴───┴╌╌╌┴───┴╌╌╌╌╌╌╌╌╌╌

First test is to check whether `Z1` is the base of `Z2`

.. code-block::

   >>> print(Z2.base is Z1)
   True

At this point, we know `Z2` is a view of `Z1`, meaning `Z2` can be expressed as
`Z1[start:stop:step]`. The difficulty now is to find `start`, `stop` and
`step`.  For the `step`, we can use the `strides` property of any array that
gives the number of bytes to go from one element to the other in each
dimension. In our case, and because both arrays are one-dimensional, we can
directly compare the first stride only:

.. code-block::

   >>> step = Z2.strides[0] // Z1.strides[0]
   >>> print(step)
   2

Next difficulty is to find the `start` and the `stop` indices. To do this, we
can take advantage of the `byte_bounds` method that returns a pointer to the
end-points of an array.

.. code-block::
   :class: output

     byte_bounds(Z1)[0]                  byte_bounds(Z1)[-1]
             ↓                                   ↓ 
      ╌╌╌┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬╌╌
   Z1    │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │
      ╌╌╌┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴╌╌

         byte_bounds(Z2)[0]      byte_bounds(Z2)[-1]
                 ↓                       ↓ 
      ╌╌╌╌╌╌╌┬───┬╌╌╌┬───┬╌╌╌┬───┬╌╌╌┬───┬╌╌╌╌╌╌╌╌╌╌
   Z2        │ 1 │   │ 3 │   │ 5 │   │ 7 │
      ╌╌╌╌╌╌╌┴───┴╌╌╌┴───┴╌╌╌┴───┴╌╌╌┴───┴╌╌╌╌╌╌╌╌╌╌


.. code-block::

   >>> offset_start = np.byte_bounds(Z2)[0] - np.byte_bounds(Z1)[0]
   >>> print(offset_start) # bytes
   8 
   
   >>> offset_stop = np.byte_bounds(Z2)[-1] - np.byte_bounds(Z1)[-1]
   >>> print(offset_stop) # bytes
   -16

Converting these offsets into indices is straightforward using the `itemsize`
and taking into account that the `offset_stop` is negative (end-bound of `Z2`
is logically smaller than end-bound of `Z1` array). We thus need to add the
items size of Z1 to get the right end index.
   
.. code-block::

   >>> start = offset_start // Z1.itemsize
   >>> stop = Z1.size + offset_stop // Z1.itemsize
   >>> print(start, stop, step)
   1, 8, 2

Last we test our results:

.. code-block::

   >>> print(np.allclose(Z1[start,stop,step], Z2))
   True
   

Exercice
++++++++

As an exercise, you can improve this first and very simple implementation by
taking into account:

* Negative steps
* Multi-dimensional arrays

  
Sources
+++++++

* `find_index <../code/find_index.py>`_ (solution to the exercise)
