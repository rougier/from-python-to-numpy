Introduction
===============================================================================

.. contents:: **Contents**
   :local:


Simple example
--------------

.. note::

   You can execute any code below from the `code <code>`_ folder using the
   regular python shell or from inside an IPython session or Jupyter notebook. In
   such a case, you might want to use the magic command `%timeit` instead of the
   `custom one <code/tools.py>`_ I wrote.

Numpy is all about vectorization. If you are familiar with Python, this is the
main difficulty you'll face because you'll need to change your way of thinking
and your new friends (among others) are named "vectors", "arrays", "views" or
"ufuncs".

Let's take a very simple example, random walk. One possible object oriented
approach would be to define a `RandomWalker` class and write a walk
method that would return the current position after each (random) step. It's nice,
it's readable, but it is slow:

**Object oriented approach**

.. code:: python

   class RandomWalker:
       def __init__(self):
           self.position = 0

       def walk(self, n):
           self.position = 0
           for i in range(n):
               yield self.position
               self.position += 2*random.randint(0, 1) - 1
           
   walker = RandomWalker()
   walk = [position for position in walker.walk(1000)]

Benchmarking gives us:

.. code:: pycon

   >>> from tools import timeit
   >>> walker = RandomWalker()
   >>> timeit("[position for position in walker.walk(n=10000)]", globals())
   10 loops, best of 3: 15.7 msec per loop

       
**Procedural approach**

For such a simple problem, we can probably save the class definition and
concentrate only on the walk method that computes successive positions after
each random step.

.. code:: python

   def random_walk(n):
       position = 0
       walk = [position]
       for i in range(n):
           position += 2*random.randint(0, 1)-1
           walk.append(position)
       return walk

   walk = random_walk(1000)

This new method saves some CPU cycles but not that much because this function
is pretty much the same as in the object-oriented approach and the few cycles
we saved probably come from the inner Python object-oriented machinery.

.. code:: pycon

   >>> from tools import timeit
   >>> timeit("random_walk(n=10000)", globals())
   10 loops, best of 3: 15.6 msec per loop

   
**Vectorized approach**
   
But we can do better using the `itertools
<https://docs.python.org/3.6/library/itertools.html>`_ Python module that
offers *a set of functions creating iterators for efficient looping*. If we
observe that a random walk is an accumulation of steps, we can rewrite the
function by first generating all the steps and accumulate them without any
loop:

.. code:: python

   def random_walk_faster(n=1000):
       from itertools import accumulate
       # Only available from Python 3.6
       steps = random.choices([-1,+1], k=n)
       return [0]+list(accumulate(steps))

    walk = random_walk_faster(1000)
   
In fact, we've just *vectorized* our function. Instead of looping for picking
sequential steps and add them to the current position, we first generated all the
steps at once and used the `accumulate
<https://docs.python.org/3.6/library/itertools.html#itertools.accumulate>`_
function to compute all the positions. We got rid of the loop and this makes
things faster:

.. code:: pycon

   >>> from tools import timeit
   >>> timeit("random_walk_faster(n=10000)", globals())
   10 loops, best of 3: 2.21 msec per loop

We gained 250% of computation-time compared to the previous version, not so
bad. But the advantage of this new version is that it makes numpy vectorization
super simple. We just have to translate itertools call into numpy ones.

.. code:: python
       
   def random_walk_fastest(n=1000):
       # No 's' in numpy choice (Python offers choice & choices)
       steps = np.random.choice([-1,+1], 1000)
       return np.cumsum(steps)

   walk = random_walk_fastest(1000)
           
Not too difficult, but we gained a factor 500x using numpy:
 
.. code:: pycon

   >>> from tools import timeit
   >>> timeit("random_walk_fastest(n=10000)", globals())
   1000 loops, best of 3: 14 usec per loop


This book is about vectorization, be it at the code or problem level. We'll
see this difference is important before looking at custom vectorization.


Readability vs speed
--------------------

Before heading to the next chapter, I would like to warn you about a potential
problem you may encounter once you'll have become familiar with numpy. It is a
very powerful library and you can make wonders with it but, most of the time,
this comes at the price of readability. If you don't comment your code at the
time of writing, you won't be able to tell what a function is doing after a few
weeks (or possibly days). For example, can you tell what the two functions
below are doing? Probably you can tell for the first one, but unlikely for the
second (or your name is `Jaime Fernández del Río
<http://stackoverflow.com/questions/7100242/python-numpy-first-occurrence-of-subarray>`_
and you don't need to read this book).

.. code:: python
          
   def function_1(seq, sub):
       return [i for i in range(len(seq) - len(sub)) if seq[i:i+len(sub)] == sub]

   def function_2(seq, sub):
       target = np.dot(sub, sub)
       candidates = np.where(np.correlate(seq, sub, mode='valid') == target)[0]
       check = candidates[:, np.newaxis] + np.arange(len(sub))
       mask = np.all((np.take(seq, check) == sub), axis=-1)
       return candidates[mask]

As you may have guessed, the second function is the
vectorized-optimized-faster-numpy version of the first function. It is 10 times
faster than the pure Python version, but it is hardly readable.
