Introduction
===============================================================================

Numpy is all about vectorization.

If you are familiar with Python, this is the main difficulty you'll face
because it requires for you to change your way of thinking and your new friends
are named vectors, arrays, views or ufuncs.

Let's take a very simple example: random walk. One possible object oriented
approach would be to define a `RandomWalker` class and to write with a walk
method that would return current position after each (random) steps. It's nice,
but is is slow:

**Object oriented approach**

.. code:: python

   class RandomWalker:
      def __init__(self):
          self.steps = []
          self.position = 0

      def walk(self, n):
          yield self.position
          for i in range(n):
              step = 2*random.randint(0, 1) - 1
              self.position += step
              yield self.position
           
   walker = RandomWalker()
   walk = []
   for position in walker.walk(1000):
       walk.append(position)


       
**Functional approach**

For such a simple problem, we can probably save the class definition and
concentrate only on the walk method that compute successive positions after
each random steps.

.. code:: python

   def random_walk(n):
       position = 0
       walk = [position]
       for i in range(n):
           step = 2*random.randint(0, 1)-1
           position += step
           walk.append(position)
       return walk

   walk = random_walk(1000)

**Vectorized approach**

But, we can further simplifying things by considering a random walk to be
composed of a number of steps and corresponding positions are the cumulative
sum of these steps.

.. code:: python
       
   steps = 2*np.random.randint(0, 2, size=n) - 1
   walk = np.cumsum(steps)

   
