Anatomy of an array
===============================================================================

.. contents:: **Contents**
   :local:
        

Introduction
------------
      
As explained in the Preface_, you should have a basic experience with NumPy to
read this book. If this is not the case, you'd better start with a beginner
tutorial before coming back here. Consequently I'll only give here a quick
reminder on the basic anatomy of NumPy arrays, especially regarding the memory
layout, view, copy and the data type. They are critical notions to
understand if you want your computation to benefit from NumPy philosophy.

Let's consider a simple example where we want to clear all the values from an
array which has the dtype `np.float32`. How does one write it to maximize speed? The
below syntax is rather obvious (at least for those familiar with NumPy) but the
above question asks to find the fastest operation.

.. code-block:: python

   >>> Z = np.ones(4*1000000, np.float32)
   >>> Z[...] = 0

If you look more closely at both the dtype and the size of the array, you can
observe that this array can be casted (i.e. viewed) into many other
"compatible" data types. By compatible, I mean that `Z.size * Z.itemsize` can
be divided by the new dtype itemsize.

.. code-block:: python

   >>> timeit("Z.view(np.float16)[...] = 0", globals())
   100 loops, best of 3: 2.72 msec per loop
   >>> timeit("Z.view(np.int16)[...] = 0", globals())
   100 loops, best of 3: 2.77 msec per loop
   >>> timeit("Z.view(np.int32)[...] = 0", globals())
   100 loops, best of 3: 1.29 msec per loop
   >>> timeit("Z.view(np.float32)[...] = 0", globals())
   100 loops, best of 3: 1.33 msec per loop
   >>> timeit("Z.view(np.int64)[...] = 0", globals())
   100 loops, best of 3: 874 usec per loop
   >>> timeit("Z.view(np.float64)[...] = 0", globals())
   100 loops, best of 3: 865 usec per loop
   >>> timeit("Z.view(np.complex128)[...] = 0", globals())
   100 loops, best of 3: 841 usec per loop
   >>> timeit("Z.view(np.int8)[...] = 0", globals())
   100 loops, best of 3: 630 usec per loop
                
Interestingly enough, the obvious way of clearing all the values is not the
fastest. By casting the array into a larger data type such as `np.float64`, we
gained a 25% speed factor. But, by viewing the array as a byte array
(`np.int8`), we gained a 50% factor. The reason for such speedup are to be
found in the internal NumPy machinery and the compiler optimization. This
simple example illustrates the philosophy of NumPy as we'll see in the next
section below.


Memory layout
-------------

The `NumPy documentation
<https://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html>`_ defines the
ndarray class very clearly:

  *An instance of class ndarray consists of a contiguous one-dimensional segment
  of computer memory (owned by the array, or by some other object), combined
  with an indexing scheme that maps N integers into the location of an item in
  the block.*

Said differently, an array is mostly a contiguous block of memory whose parts
can be accessed using an indexing scheme. Such indexing scheme is in turn
defined by a `shape
<https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.shape.html#numpy.ndarray.shape>`_
and a `data type
<https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ and this is
precisely what is needed when you define a new array:

.. code:: python

   Z = np.arange(9).reshape(3,3).astype(np.int16)

Here, we know that Z itemsize is 2 bytes (`int16`), the shape is (3,3) and
the number of dimensions is 2 (`len(Z.shape)`).

.. code:: pycon

   >>> print(Z.itemsize)
   2
   >>> print(Z.shape)
   (3, 3)
   >>> print(Z.ndim)
   2

Furthermore and because Z is not a view, we can deduce the
`strides <https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.strides.html#numpy.ndarray.strides>`_ of the array that define the number of bytes to step in each dimension when traversing the array.

.. code:: pycon

   >>> strides = Z.shape[1]*Z.itemsize, Z.itemsize
   >>> print(strides)
   (6, 2)
   >>> print(Z.strides)
   (6, 2)
  
With all these information, we know how to access a specific item (designed by
an index tuple) and more precisely, how to compute the start and end offsets:

.. code:: python

   offset_start = 0
   for i in range(Z.ndim):
       offset_start += Z.strides[i] * index[i]
   offset_end = offset_start + Z.itemsize

Let's see if this is correct using the `tobytes
<https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.tobytes.html>`_
conversion method:

.. code:: python

   >>> Z = np.arange(9).reshape(3, 3).astype(np.int16)
   >>> index = 1, 1
   >>> print(Z[index].tobytes())
   b'\x04\x00'
   >>> offset_start = 0
   >>> for i in range(Z.ndim):
   ...     offset_start += Z.strides[i] * index[i]
   >>> offset_end = offset_start + Z.itemsize
   >>> print(Z.tobytes()[offset_start:offset_end]
   b'\x04\x00'


This array can be actually considered from different perspectives (i.e. layouts):
   
**Item layout**
   
.. code::
   :class: output

                  shape[1]
                    (=3)
               ┌───────────┐   

            ┌  ┌───┬───┬───┐  ┐ 
            │  │ 0 │ 1 │ 2 │  │
            │  ├───┼───┼───┤  │     
   shape[0] │  │ 3 │ 4 │ 5 │  │ len(Z)
    (=3)    │  ├───┼───┼───┤  │  (=3)
            │  │ 6 │ 7 │ 8 │  │
            └  └───┴───┴───┘  ┘

**Flattened item layout**
   
.. code::
   :class: output
  
   ┌───┬───┬───┬───┬───┬───┬───┬───┬───┐
   │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │
   └───┴───┴───┴───┴───┴───┴───┴───┴───┘

   └───────────────────────────────────┘
                  Z.size
                   (=9)
   

**Memory layout (C order, big endian)**
   
.. code::
   :class: output

                            strides[1]
                              (=2)
                     ┌─────────────────────┐

             ┌       ┌──────────┬──────────┐ ┐
             │ p+00: │ 00000000 │ 00000000 │ │
             │       ├──────────┼──────────┤ │
             │ p+02: │ 00000000 │ 00000001 │ │ strides[0]
             │       ├──────────┼──────────┤ │   (=2x3)
             │ p+04  │ 00000000 │ 00000010 │ │
             │       ├──────────┼──────────┤ ┘
             │ p+06  │ 00000000 │ 00000011 │ 
             │       ├──────────┼──────────┤
   Z.nbytes  │ p+08: │ 00000000 │ 00000100 │
   (=3x3x2)  │       ├──────────┼──────────┤
             │ p+10: │ 00000000 │ 00000101 │
             │       ├──────────┼──────────┤
             │ p+12: │ 00000000 │ 00000110 │
             │       ├──────────┼──────────┤
             │ p+14: │ 00000000 │ 00000111 │
             │       ├──────────┼──────────┤
             │ p+16: │ 00000000 │ 00001000 │
             └       └──────────┴──────────┘

                     └─────────────────────┘   
                           Z.itemsize
                        Z.dtype.itemsize
                              (=2) 


If we now take a slice of `Z`, the result is a view of the base array `Z`:
                        
.. code-block:: python

   V = Z[::2,::2]

Such view is specified using a shape, a dtype **and** strides because strides
cannot be deduced anymore from the dtype and shape only:

**Item layout**
   
.. code::
   :class: output

                  shape[1]
                    (=2)
               ┌───────────┐   

            ┌  ┌───┬╌╌╌┬───┐  ┐           
            │  │ 0 │   │ 2 │  │            ┌───┬───┐
            │  ├───┼╌╌╌┼───┤  │            │ 0 │ 2 │
   shape[0] │  ╎   ╎   ╎   ╎  │ len(Z)  →  ├───┼───┤
    (=2)    │  ├───┼╌╌╌┼───┤  │  (=2)      │ 6 │ 8 │
            │  │ 6 │   │ 8 │  │            └───┴───┘
            └  └───┴╌╌╌┴───┘  ┘           
                                          
**Flattened item layout**
   
.. code::
   :class: output
  
   ┌───┬╌╌╌┬───┬╌╌╌┬╌╌╌┬╌╌╌┬───┬╌╌╌┬───┐       ┌───┬───┬───┬───┐
   │ 0 │   │ 2 │   ╎   ╎   │ 6 │   │ 8 │   →   │ 0 │ 2 │ 6 │ 8 │
   └───┴╌╌╌┴───┴╌╌╌┴╌╌╌┴╌╌╌┴───┴╌╌╌┴───┘       └───┴───┴───┴───┘
   └─┬─┘   └─┬─┘           └─┬─┘   └─┬─┘
     └───┬───┘               └───┬───┘  
         └───────────┬───────────┘
                  Z.size
                   (=4)

   

**Memory layout (C order, big endian)**
   
.. code::
   :class: output
   
                 ┌        ┌──────────┬──────────┐ ┐             ┐
               ┌─┤  p+00: │ 00000000 │ 00000000 │ │             │
               │ └        ├──────────┼──────────┤ │ strides[1]  │
             ┌─┤    p+02: │          │          │ │   (=4)      │ 
             │ │ ┌        ├──────────┼──────────┤ ┘             │ 
             │ └─┤  p+04  │ 00000000 │ 00000010 │               │
             │   └        ├──────────┼──────────┤               │ strides[0] 
             │      p+06: │          │          │               │   (=12)
             │            ├──────────┼──────────┤               │
   Z.nbytes ─┤      p+08: │          │          │               │
     (=8)    │            ├──────────┼──────────┤               │
             │      p+10: │          │          │               │
             │   ┌        ├──────────┼──────────┤               ┘              
             │ ┌─┤  p+12: │ 00000000 │ 00000110 │
             │ │ └        ├──────────┼──────────┤
             └─┤    p+14: │          │          │
               │ ┌        ├──────────┼──────────┤
               └─┤  p+16: │ 00000000 │ 00001000 │
                 └        └──────────┴──────────┘
                               
                          └─────────────────────┘
                                Z.itemsize
                             Z.dtype.itemsize
                                   (=2)                                        


                        
Views and copies
----------------

Views and copies are important concepts for the optimization of your numerical
computations. Even if we've already manipulated them in the previous section,
the whole story is a bit more complex.

Direct and indirect access
++++++++++++++++++++++++++

First, we have to distinguish between `indexing
<https://docs.scipy.org/doc/numpy/user/basics.indexing.html#>`_ and `fancy
indexing <https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html#advanced-indexing>`_. The first will always return a view while the second will return a
copy. This difference is important because in the first case, modifying the view
modifies the base array while this is not true in the second case:

.. code:: pycon

   >>> Z = np.zeros(9)
   >>> Z_view = Z[:3]
   >>> Z_view[...] = 1
   >>> print(Z)
   [ 1.  1.  1.  0.  0.  0.  0.  0.  0.]
   >>> Z = np.zeros(9)
   >>> Z_copy = Z[[0,1,2]]
   >>> Z_copy[...] = 1
   >>> print(Z)
   [ 0.  0.  0.  0.  0.  0.  0.  0.  0.]

Thus, if you need fancy indexing, it's better to keep a copy of your fancy index
(especially if it was complex to compute it) and to work with it:

.. code:: pycon

   >>> Z = np.zeros(9)
   >>> index = [0,1,2]
   >>> Z[index] = 1
   >>> print(Z)
   [ 1.  1.  1.  0.  0.  0.  0.  0.  0.]

If you are unsure if the result of your indexing is a view or a copy, you can
check what is the `base` of your result. If it is `None`, then you result is a
copy:

   
.. code:: pycon

   >>> Z = np.random.uniform(0,1,(5,5))
   >>> Z1 = Z[:3,:]
   >>> Z2 = Z[[0,1,2], :]
   >>> print(np.allclose(Z1,Z2))
   True
   >>> print(Z1.base is Z)
   True
   >>> print(Z2.base is Z)
   False
   >>> print(Z2.base is None)
   True

Note that some NumPy functions return a view when possible (e.g. `ravel
<https://docs.scipy.org/doc/numpy/reference/generated/numpy.ravel.html>`_)
while some others always return a copy (e.g. `flatten
<https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.flatten.html#numpy.ndarray.flatten>`_):

.. code:: pycon

    >>> Z = np.zeros((5,5))
    >>> Z.ravel().base is Z
    True
    >>> Z[::2,::2].ravel().base is Z
    False
    >>> Z.flatten().base is Z
    False

   
Temporary copy
++++++++++++++

Copies can be made explicitly like in the previous section, but the most
general case is the implicit creation of intermediate copies. This is the case
when you are doing some arithmetic with arrays:

.. code:: pycon

   >>> X = np.ones(10, dtype=np.int)
   >>> Y = np.ones(10, dtype=np.int)
   >>> A = 2*X + 2*Y

In the example above, three intermediate arrays have been created. One for
holding the result of `2*X`, one for holding the result of `2*Y` and the last
one for holding the result of `2*X+2*Y`. In this specific case, the arrays are
small enough and this does not really make a difference. However, if your
arrays are big, then you have to be careful with such expressions and wonder if
you can do it differently. For example, if only the final result matters and
you don't need `X` nor `Y` afterwards, an alternate solution would be:

.. code:: pycon

   >>> X = np.ones(10, dtype=np.int)
   >>> Y = np.ones(10, dtype=np.int)
   >>> np.multiply(X, 2, out=X)
   >>> np.multiply(Y, 2, out=Y)
   >>> np.add(X, Y, out=X)

Using this alternate solution, no temporary array has been created. Problem is
that there are many other cases where such copies needs to be created and this
impact the performance like demonstrated on the example below:

.. code:: pycon

   >>> X = np.ones(1000000000, dtype=np.int)
   >>> Y = np.ones(1000000000, dtype=np.int)
   >>> timeit("X = X + 2.0*Y", globals())
   100 loops, best of 3: 3.61 ms per loop
   >>> timeit("X = X + 2*Y", globals())
   100 loops, best of 3: 3.47 ms per loop
   >>> timeit("X += 2*Y", globals())
   100 loops, best of 3: 2.79 ms per loop
   >>> timeit("np.add(X, Y, out=X); np.add(X, Y, out=X)", globals())
   1000 loops, best of 3: 1.57 ms per loop
          


Conclusion
----------

As a conclusion, we'll make an exercise. Given two vectors `Z1` and `Z2`. We
would like to know if `Z2` is a view of `Z1` and if yes, what is this view ?

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

First, we need to check if `Z1` is the base of `Z2`

.. code-block::

   >>> print(Z2.base is Z1)
   True

At this point, we know `Z2` is a view of `Z1`, meaning `Z2` can be expressed as
`Z1[start:stop:step]`. The difficulty is to find `start`, `stop` and
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
         ↓                                       ↓ 
      ╌╌╌┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬╌╌
   Z1    │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │
      ╌╌╌┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴╌╌

         byte_bounds(Z2)[0]      byte_bounds(Z2)[-1]
             ↓                           ↓ 
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

   >>> print(np.allclose(Z1[start:stop:step], Z2))
   True

As an exercise, you can improve this first and very simple implementation by
taking into account:

* Negative steps
* Multi-dimensional arrays

`Solution <code/find_index.py>`_ to the exercise.


                        
