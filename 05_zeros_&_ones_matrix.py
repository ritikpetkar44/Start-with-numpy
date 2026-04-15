"""
how to create zeros and ones matrix in numpy
This module provides functions to create zeros and ones matrices in numpy.
You can create a zeros matrix using the np.zeros() function and a ones matrix using the np.ones() function.
Example usage:

"""
import numpy as np

# Create a zeros matrix of shape (3, 3)

b= np.zeros((3, 3))
print("Zeros Matrix:")
print(b)

"""output:
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]"""

# Create a ones matrix of shape (3, 3)
a = np.ones((3, 3), dtype=np.int32)
print("Ones Matrix:")
print(a)

"""output:
[[1 1 1]
 [1 1 1]
 [1 1 1]]"""
