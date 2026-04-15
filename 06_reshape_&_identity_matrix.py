"""
Reshaping arrays and identity matrix in NumPy
This module provides functions to reshape arrays and create identity matrices in NumPy.
You can reshape an array using the np.reshape() function and create an identity matrix using the np.eye() function.
Example usage:

"""

import numpy as np

# Create a 1D array of shape (10,)
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.int64)
print("Original array:")
print(a)

"""output:
[ 1  2  3  4  5  6  7  8  9 10]
"""
# Reshape the array to shape (2, 5)
# 2*5=10 ELEMENTS
a1 = a.reshape(2, 5)
print("Reshaped array (2, 5):")
print(a1)

"""
identity matrix is a square matrix with ones on the main diagonal and zeros elsewhere.
2 tpes of identity matrix are:
1. np.eye(n): creates an identity matrix of size n x n.
2. np.identity(n): creates an identity matrix of size n x n.
"""
# Create an identity matrix of size 4 x 4 using np.eye()
#1st type of identity matrix

i= np.eye(4, dtype=int)
print("Identity matrix using np.eye():")
print(i)
"""
Output:
[[1 0 0 0]
 [0 1 0 0]
 [0 0 1 0]
 [0 0 0 1]]
INT dtype is used to create an identity matrix with integer values.
"""

#2nd type of identity matrix
i1= np.identity(4)
print("Identity matrix using np.identity():")
print(i1)

"""Output:
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
 default FLOAT dtype is used to create an identity matrix with float values.
 """