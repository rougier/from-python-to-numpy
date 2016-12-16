Custom vectorization
===============================================================================

.. contents:: **Contents**
   :local:

      
Introduction
------------

One of the strength of Numpy is that it allows you to write your own array
class. The mechanism is a bit tedious but it is worth the effort.


Typed list
----------

We would like to define a typed list object such that if offers both the Python
list API and the Numpy array API (with some restriction of course). We would
like for example to be able to write:

.. code:: python

   >>> l = TypedList(int)
   >>> l.append(1)

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
