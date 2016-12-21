Beyond Numpy
===============================================================================

.. contents:: **Contents**
   :local:

Back to Python
--------------

You've almost reached the end of the book and, hopefully, you've learned that
Numpy is a very versatile and powerful library. However in the meantime, you've
to remember that Python is also quite a powerful tool. In fact, in some few
specific cases, it might be more powerful than Numpy. Let's consider for
example an interesting exercise that has been proposed by Tucker Balch in his
`Coursera's Computational Investing
<https://www.coursera.org/learn/computational-investing>`_ course. The exercise
is written as:

Write the most succinct code possible to compute all "legal" allocations to 4
stocks such that:

* The allocations are in 1.0 chunks, and the allocations sum to 10.0
* Only "pure" NumPy is allowed (no external libraries)
* Can you do it without a "for"?"

`Yaser Martinez <http://yasermartinez.com/blog/index.html>`_ collected the
different answers from the community and the proposed solutions yield
surprising results. But let's start with he most obvious Python solution:

.. code:: python

   def solution_1():
       # Brute force
       # 14641 (=11*11*11*11) iterations & tests
       Z = []
       for i in range(11):
           for j in range(11):
               for k in range(11):
                   for l in range(11):
                       if i+j+k+l == 10:
                           Z.append((i,j,k,l))
       return Z

This solution is the slowest solution because it requires 4 loops, and more
importantly, it tests all the different combinations (11641) of 4 integers
between 0 and 10 to retain only combinations whose sum is 10. We can of course
get rid of the 4 loops using itertools, but the code remains slow:

.. code:: python

   import itertools as it

   def solution_2():
       # Itertools
       # 14641 (=11*11*11*11) iterations & tests
       return [(i,j,k,l)
               for i,j,k,l in it.product(range(11),repeat=4) if i+j+k+l == 10]

One of the best solution that has been proposed by Nick Popplas takes advantage
of the fact we can have intelligent imbricated loops that will allow us to
directly build each tuple without any test as shown below:

.. code:: python

   def solution_3():
       return [(a, b, c, (10 - a - b - c))
               for a in range(11)
               for b in range(11 - a)
               for c in range(11 - a - b)]

The best numpy solution by Yaser Martinez uses a different strategy with a
restriced set of tests:

.. code:: python

   def solution_4():
       X123 = np.indices((11,11,11)).reshape(3,11*11*11)
       X4 = 10 - X123.sum(axis=0)
       return np.vstack((X123, X4)).T[X4 > -1]

If we benchmark these methods, we get:

.. code:: pycon

   >>> timeit("solution_1()", globals())
   100 loops, best of 3: 1.9 msec per loop
   >>> timeit("solution_2()", globals())
   100 loops, best of 3: 1.67 msec per loop
   >>> timeit("solution_3()", globals())
   1000 loops, best of 3: 60.4 usec per loop
   >>> timeit("solution_4()", globals())
   1000 loops, best of 3: 54.4 usec per loop

The Numpy solution is the fastest but the pure Python solution is comparable.
But let me introduce a small modification to the Python solution:

.. code:: python

   def solution_3_bis():
       return ((a, b, c, (10 - a - b - c))
               for a in range(11)
               for b in range(11 - a)
               for c in range(11 - a - b))

If we benchmark it, we get:

.. code:: pycon

   >>> timeit("solution_3_bis()", globals())
   10000 loops, best of 3: 0.643 usec per loop

You read it right, we have gained a factor 100 just by replacing square
brackets with parenthesis. How is that possible ? The explanation can be found
by looking at the type of the returned object:

.. code:: pycon

    >>> print(type(solution_3()))
    <class 'list'>
    >>> print(type(solution_3_bis()))
    <class 'generator'>

The `solution_3_bis()` returns a generator that can be used to generate the
full list or to iterate over all the different elements. In any case, the huge
speedup comes from the non-instantiation of the full list and it is thus
important to wonder if you need an actual instance of your result or if a
simple generator might do the job.


Numpy & co
----------

Beyond numpy, there are several other Python packages that are worth a look
because they address similar yet different class of problems using different
technology (compilation, virtual machine, just in time compilation, GPU,
compression, etc.). Depending on your specific problem and your hardware, one
package may be better than the other. Let's illustrate their usage using a very
simple example where we want to compute an expression based on two float
vectors:

.. code:: python

   import numpy as np
   a = np.random.uniform(0, 1, 1000).astype(np.float32)
   b = np.random.uniform(0, 1, 1000).astype(np.float32)
   c = 2*a + 3*b

   
NumExpr
+++++++

The `numexpr <https://github.com/pydata/numexpr/wiki/Numexpr-Users-Guide>`_
package supplies routines for the fast evaluation of array expressions
elementwise by using a vector-based virtual machine. It's comparable to SciPy's
weave package, but doesn't require a separate compile step of C or C++ code.

.. code:: python

   import numpy as np
   import numexpr as ne

   a = np.random.uniform(0, 1, 1000).astype(np.float32)
   b = np.random.uniform(0, 1, 1000).astype(np.float32)
   c = ne.evaluate("2*a + 3*b")

   
Cython
++++++

`Cython <http://cython.org>`_ is an optimising static compiler for both the
Python programming language and the extended Cython programming language (based
on Pyrex). It makes writing C extensions for Python as easy as Python itself.

.. code:: python

   import numpy as np
          
   def evaluate(np.ndarray a, np.ndarray b):
       cdef int i
       cdef np.ndarray c = np.zeros_like(a)
       for i in range(a.size):
           c[i] = 2*a[i] + 3*b[i]
       return c

   a = np.random.uniform(0, 1, 1000).astype(np.float32)
   b = np.random.uniform(0, 1, 1000).astype(np.float32)
   c = evaluate(a, b)
   
   
Numba
+++++

`Numba <http://numba.pydata.org>`_ gives you the power to speed up your
applications with high performance functions written directly in Python. With a
few annotations, array-oriented and math-heavy Python code can be just-in-time
compiled to native machine instructions, similar in performance to C, C++ and
Fortran, without having to switch languages or Python interpreters.

.. code:: python

   from numba import jit
   import numpy as np

   @jit
   def evaluate(np.ndarray a, np.ndarray b):
       c = np.zeros_like(a)
       for i in range(a.size):
           c[i] = 2*a[i] + 3*b[i]
       return c

   a = np.random.uniform(0, 1, 1000).astype(np.float32)
   b = np.random.uniform(0, 1, 1000).astype(np.float32)
   c = evaluate(a, b)


Theano
++++++

`Theano <http://www.deeplearning.net/software/theano/>`_ is a Python library
that allows you to define, optimize, and evaluate mathematical expressions
involving multi-dimensional arrays efficiently. Theano features tight
integration with NumPy, transparent use of a GPU, efficient symbolic
differentiation, speed and stability optimizations, dynamic C code generation
and extensive unit-testing and self-verification.

.. code:: python

   import numpy as np
   import theano.tensor as T

   x = T.fvector('x')
   y = T.fvector('y')
   z = 2*x + 3*y
   f = function([x, y], z)

   a = np.random.uniform(0, 1, 1000).astype(np.float32)
   b = np.random.uniform(0, 1, 1000).astype(np.float32)
   c = f(a, b)

   
PyCUDA
++++++

`PyCUDA <http://mathema.tician.de/software/pycuda>`_ lets you access Nvidia's
CUDA parallel computation API from Python.

.. code:: python

   import numpy as np
   import pycuda.autoinit
   import pycuda.driver as drv
   from pycuda.compiler import SourceModule
   
   mod = SourceModule("""
       __global__ void evaluate(float *c, float *a, float *b)
       {
         const int i = threadIdx.x;
         c[i] = 2*a[i] + 3*b[i];
       }
   """)

   evaluate = mod.get_function("evaluate")

   a = np.random.uniform(0, 1, 1000).astype(np.float32)
   b = np.random.uniform(0, 1, 1000).astype(np.float32)
   c = np.zeros_like(a)
   
   evaluate(drv.Out(c), drv.In(a), drv.In(b), block=(400,1,1), grid=(1,1))


PyOpenCL
++++++++

`PyOpenCL <http://mathema.tician.de/software/pyopencl>`_ lets you access GPUs
and other massively parallel compute devices from Python.

.. code:: python
          
   import numpy as np
   import pyopencl as cl

   a = np.random.uniform(0, 1, 1000).astype(np.float32)
   b = np.random.uniform(0, 1, 1000).astype(np.float32)
   c = np.empty_like(a)
   
   ctx = cl.create_some_context()
   queue = cl.CommandQueue(ctx)

   mf = cl.mem_flags
   gpu_a = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a)
   gpu_b = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b)

   evaluate = cl.Program(ctx, """
       __kernel void evaluate(__global const float *gpu_a;
                              __global const float *gpu_b;
                              __global       float *gpu_c)
       {
           int gid = get_global_id(0);
           gpu_c[gid] = 2*gpu_a[gid] + 3*gpu_b[gid];
       }
   """).build()

   gpu_c = cl.Buffer(ctx, mf.WRITE_ONLY, a.nbytes)
   evaluate.evaluate(queue, a.shape, None, gpu_a, gpu_b, gpu_c)
   cl.enqueue_copy(queue, c, gpu_c)



Scipy & co
----------

If there are several additional packages for Numpy, there is a trillion
additional packages for scipy. In fact, every domain of science probably has
its own package and most of the examples we've been studying until now could
have been solved in two or three calls to a method in the relevant package.
But of course, it was not the goal an programming things yourself is generally
a good exercise if you have some spare time. The biggest difficulty at this
point is to find these relevant packages. Here is a very short list of packages
that are well-maintained, well tested and may simplify your scientific life
(depending on your domain). There are of course many more and depending on your
specific needs, chances are you do not have to program everything by
yourself. For an extensive list, have a look at the `Awesome python list
<https://awesome-python.com>`_.

scikit-learn
++++++++++++

`scikit-learn <http://scikit-learn.org/stable/>`_ is a free software machine
learning library for the Python programming language. It features various
classification, regression and clustering algorithms including support vector
machines, random forests, gradient boosting, k-means and DBSCAN, and is
designed to interoperate with the Python numerical and scientific libraries
NumPy and SciPy.


scikit-image
++++++++++++

`scikit-image <http://scikit-image.org>`_ is a Python package dedicated to
image processing, and using natively NumPy arrays as image objects. This
chapter describes how to use scikit-image on various image processing tasks,
and insists on the link with other scientific Python modules such as NumPy and
SciPy.

SympPy
++++++

`SymPy <http://www.sympy.org/en/index.html>`_ is a Python library for symbolic
mathematics. It aims to become a full-featured computer algebra system (CAS)
while keeping the code as simple as possible in order to be comprehensible and
easily extensible. SymPy is written entirely in Python.

Astropy
+++++++

The `Astropy <http://www.astropy.org>`_ project is a community effort to
develop a single core package for astronomy in Python and foster
interoperability between Python astronomy packages.


Cartopy
+++++++

`Cartopy <http://scitools.org.uk/cartopy/>`_ is a Python package designed to
make drawing maps for data analysis and visualisation as easy as
possible. Cartopy makes use of the powerful PROJ.4, numpy and shapely libraries
and has a simple and intuitive drawing interface to matplotlib for creating
publication quality maps.


Brian
+++++

`Brian <http://www.briansimulator.org>`_ is a free, open source simulator for
spiking neural networks. It is written in the Python programming language and
is available on almost all platforms. We believe that a simulator should not
only save the time of processors, but also the time of scientists. Brian is
therefore designed to be easy to learn and use, highly flexible and easily
extensible.


Conclusion
----------

Numpy is a very versatile library but still, it does not mean you have to use
it in every situation. In this chapter, we've seen some alternatives (including
Python itself) that are worth a look. As always, the choice belongs to you. You
have to consider what is the best solution for you in term of development time,
computation time and effort in maintenance. In one hand, if you design your
own solution, you'll have to test it and to maintain it, but in exchange,
you'll be free to design it the way you want. On the other hand, if you decide
to rely on a third-party package, you'll save time in development and benefit
from community-support even though you might have to adapt the package to your
specific needs. The choice is up to you.
