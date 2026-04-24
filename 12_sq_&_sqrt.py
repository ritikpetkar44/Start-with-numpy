"""
square and square root functions
numpy provides two functions to calculate the square and square root of an array:
1. numpy.square() function is used to calculate the square of each element in an array.
2. numpy.sqrt() function is used to calculate the square root of each element in an array.
"""
import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.square(a)
print(b)
"""output:
[ 1  4  9 16 25]
"""
c = np.sqrt(a)
print(c)
"""output:
[1.         1.41421356 1.73205081 2.         2.23606798]
"""