Anatomy of an array
===============================================================================

.. contents:: **Contents**
   :local:
        

Introduction
------------
      
As explained in the Preface_, you should have a basic experience with numpy to
read this book. If this is not the case, you'd better start with a beginner
tutorial before coming back here. Consequently I'll only give here a quick
reminder on the basic anatomy of numpy arrays, especially regarding the memory
layout, view, copy and the data type. They are critical notions to
understand if you want your computation to benefit from numpy philosophy.

Let's consider a simple example where we want to clear all the values from an
array whose dtype is `np.float32`. What would be the best way? The syntax below
is rather obvious (at least for who is familiar with numpy) but the question is
to known whether this is the fastest way.

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
found in the internal numpy machinery and the compiler optimization. This
simple example illustrates the philosophy of numpy as we'll se in the next
section below.


Memory layout
-------------

The `numpy documentation
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

   >>> print(Z.itemize)
   2
   >>> print(Z.shape)
   (3, 3)
   >>> print(Z.ndim)
   2

Furthermore and because Z is not a view, we can deduce the
`strides <https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.strides.html#numpy.ndarray.strides>`_ of the array that define the number of bytes to step in each dimension when traversing the array.

.. code:: pycon

   >>> strides = Z.shape[0]*Z.itemize, Z.itemize
   >>> print(strides)
   (6, 2)
   >>> print(Z.strides)
   (6, 2)
  
With all these information, we know how to access a specific item (designed by
an index tuple) and more precisely, how to compute the start and end offsets:

.. code:: python

   offset_start = 0
   for i in range(ndim):
       offset_start += strides[i]*index[i]
   offset_end = offset_start + Z.itemsize

Let's see if this is correct using the `tobytes
<https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.tobytes.html>`_
conversion method:

.. code:: python

   >>> Z = np.arange(9).reshape(3,3).astype(np.int16)
   >>> index = 1,1
   >>> print(Z[index].tobytes())
   b'\x04\x00'
   >>> offset = 0
   >>> for i in range(Z.ndim):
   ...     offset + = Z.strides[i]*index[i]
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

|WIP|

..
   .. code:: python

      >>> Z = np.zeros((4,4), dtype=np.int64)
      >>> Zc = np.array(Z, order="C")
      >>> info(Zc)
      >>> Zf = np.array(Z, order="F")
      >>> info(Zf)


   .. code::
      :class: output

      ------------------------------        ------------------------------
        Zc                                    Zf
      ------------------------------        ------------------------------
      Interface (item)                      Interface (item)              
        shape:       (4, 4)                   shape:       (4, 4)         
        dtype:       int64                    dtype:       int64          
        size:        16                       size:        16             
        order:       ☑ C  ☐ Fortran           order:       ☐ C  ☑ Fortran 

      Memory (byte)                         Memory (byte)                 
        item size:   8                        item size:   8              
        array size:  128                      array size:  128            
        strides:     (32, 8)                  strides:     (8, 32)        

      Properties                            Properties                    
        own data:    ☑ Yes    ☐ No            own data:    ☑ Yes    ☐ No    
        writeable:   ☑ Yes    ☐ No            writeable:   ☑ Yes    ☐ No    
        contiguous:  ☑ Yes    ☐ No            contiguous:  ☑ Yes    ☐ No    
        aligned:     ☑ Yes    ☐ No            aligned:     ☑ Yes    ☐ No    
      ------------------------------        ------------------------------



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

As an exercise, you can improve this first and very simple implementation by
taking into account:

* Negative steps
* Multi-dimensional arrays

`Solution <code/find_index.py>`_ to the exercise.


                        
