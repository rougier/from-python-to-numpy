## Anatomy of an array

**Content**

* [Introduction](#introduction)
* [Architecture](#architecture)
* [Broadcasting](#broadcasting)
* [Vectorization](#vectorization)
* [Readability](#readability)
* [Conclusion](#conclusion)

### Introduction <a name="introduction"></a>

Let's consider a simple 2D array and check what kind of information we can get
from it:

    Z = np.arange(5*5).reshape(5,5)
    
You're probably familiar with the most common properties such as shape, dtype, size or
length:

    >>> print(Z.shape)
    (5,5)
    >>> print(Z.dtype)
    dtype('64')
    >>> print(Z.size)
    25
    >>> print(len(Z))
    5

However, some other properties are lesser known or utilized:

    >>> print(Z.itemsize)
    8
    >>> print(Z.flags)
      C_CONTIGUOUS : True
      F_CONTIGUOUS : False
      OWNDATA : False
      WRITEABLE : True
      ALIGNED : True
      UPDATEIFCOPY : False
    >>> print(Z.strides)
    (40,8)


Let's write a `print_info` function that print most of the relevant information:

    >>> print_info(Z)
    ------------------------------
    Interface (item)
      shape:       (5, 5)
      dtype:       int64
      size:        25
      order:       ☑ C  ☐ Fortran

    Memory (byte)
      item size:   8
      array size:  200
      strides:     (40, 8)

    Property
      own data:    ☐ Yes  ☑︎ No
      writeable:   ☑ Yes  ☐︎ No
      contiguous:  ☑ Yes  ☐︎ No
      aligned:     ☑ Yes  ☐︎ No
    ------------------------------

### Numpy architecture <a name="architecture"></a>


| Data type  |  Description                                                         |
|------------|----------------------------------------------------------------------|
| bool       | Boolean (True or False) stored as a byte                             |
| int        | Platform integer (normally either int32 or int64)                    |
| int8       | Byte (-128 to 127)                                                   |
| int16      | Integer (-32768 to 32767)                                            |
| int32      | Integer (-2147483648 to 2147483647)                                  |
| int64      | Integer (9223372036854775808 to 9223372036854775807)                 |
| uint8      | Unsigned integer (0 to 255)                                          |
| uint16     | Unsigned integer (0 to 65535)                                        |
| uint32     | Unsigned integer (0 to 4294967295)                                   |
| uint64     | Unsigned integer (0 to 18446744073709551615)                         |
| float      | Shorthand for float64.                                               |
| float16    | Half precision float: sign bit, 5 bits exponent, 10 bits mantissa    |
| float32    | Single precision float: sign bit, 8 bits exponent, 23 bits mantissa  |
| float64    | Double precision float: sign bit, 11 bits exponent, 52 bits mantissa |
| complex	 | Shorthand for complex128.                                            |
| complex64  | Complex number, represented by two 32-bit floats                     |
| complex128 | Complex number, represented by two 64-bit floats                     |











    → What is numpy useful for
    → Universal functions
    → Mixing C, Fortran and Python

### Broadcasting principles <a name="broadcasting"></a>

From the numpy documentation, we can read that there are 4 broadcasting rules:

1. All input arrays with ndim smaller than the input array of largest ndim,
   have 1's prepended to their shapes.
2. The size in each dimension of the output shape is the maximum of all the
   input sizes in that dimension.
3. An input can be used in the calculation if its size in a particular
   dimension either matches the output size in that dimension, or has value
   exactly 1.
4. If an input has a dimension size of 1 in its shape, the first data entry in
   that dimension will be used for all calculations along that dimension. In
   other words, the stepping machinery of the ufunc will simply not step along
   that dimension (the stride will be 0 for that dimension).

 → Intuitive broadcasting  
 → Weird broadcasting  
 → Strides madness  
 → Exercises  
    
### Vectorization philosophy <a name="vectorization"></a>

Let's consider a simple problem. Given two vectors `X` and `Y`, you have to
compute the sum of `X[i]*Y[j]` for all pairs of indices `i`, `j`. One simple
and obvious solution might to write:

    def compute_1(X, Y):
        result = 0
        for i in range(len(X)):
            for j in range(len(Y)):
                result += X[i] * Y[j]
        return result
    
However, this first and naive implementation requires two loops and you already
know it will be slow.

    >>> X = np.arange(1000)
    >>> timeit("compute_1(X,X)")
    1 loops, best of 3: 0.274481 sec per loop

The question is "how to vectorize the problem?" If you remember your linear
algebra course, you may have identified the expression `X[i] * Y[j]` to be very
similar to a matrix product expression. So maybe we could benefit from some
numpy speedup. One wrong solution would be to write:

    def compute_2(X, Y):
        return (X*Y).sum()
  
This is wrong because the `X*Y` expression will actually compute a new vector Z
such that `Z[i] = X[i] * Y[i]` and this is not what we want. Instead, we can
exploit numpy broadcasting by first reshaping the two vectors and then multiply
them:
  
    def compute_2(X, Y):
        Z = X.reshape(len(X),1) * Y.reshape(1,len(Y))
        return Z.sum()
  
Here we have `Z[i,j] == X[i]*Y[j]` and if we take the sum over ech elements of
Z, we get the expected result. Let's see how much speedup we gain in the
process:
  
    >>> X = np.arange(1000)
    >>> timeit("compute_2(X,X)")
    10 loops, best of 3: 0.00157926 sec per loop
  
This is better, we almost gained a factor of 100. But we can do much better. If
you look more closely at the pure Python version, you can see that the inner
loop is using `X[i]` that does not depend on the `j` index, meaning it can be
removed from the inner loop. Code can be rewritten as:

    def compute_3(X, Y):
        result = 0
        for i in range(len(X)):
            Ysum = 0
            for j in range(len(Y)):
                Ysum += Y[j]
            result += X[i]*Ysum
        return result

But since the inner loop does not depend on the `i` index, we might as well
compute it only once:

    def compute_3(X, Y):
        result = 0
        Ysum = 0
        for j in range(len(Y)):
            Ysum += Y[j]
        for i in range(len(X)):
            result += X[i]*Ysum
        return result

Not so bad, we have removed one loop. What about the other? Using the same
approach, we can write:

    def compute_3(x, y):
        Ysum = = 0
        for j in range(len(Y)):
            Ysum += Y[j]
        Xsum = = 0
        for i in range(len(X)):
            Xsum += X[i]
        return Xsum*Ysum

Finally, having realized we only need the product of the sum over X and Y respectively, 
we can benefit from the `np.sum` function and write:

    def compute_3(x, y):
        return np.sum(y) * np.sum(x)
    
It is shorter, clearear and much faster:

    >>> X = np.arange(1000)
    >>> timeit("compute_3(X,X)")
    1000 loops, best of 3: 3.97208e-06 sec per loop

What we've learned from this simple example is that there is two kinds of
vectorization, the vectorization of your problem and the vectorization of your
code. The first is the most difficult but the most important because this is
where you can expect huge gains in speed. But the latter is nonetheless
important because you can speedup your code even more. For example, let's
rewrite the last solution the Python way:

    def compute_4(x, y):
        return sum(x)*sum(y)

    >>> X = np.arange(1000)
    >>> timeit("compute_4(X,X)")
    1000 loops, best of 3: 0.000155677 sec per loop
    
This new Python version is much faster than the previous one, but still, it is
10x slower than the numpy version. 

### Readability vs optimization <a name="readability"></a>

    → Einsum notation
    → NumExpr
    → Unit-tests
    


### Conclusion <a name="conclusion"></a>
