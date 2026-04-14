"""
This module provides functions to get the shape and size of numpy arrays.
shape is a tuple that represents the dimensions of the array, while size is the total number of elements in the array.
"""
import numpy as np


""""Example usage:"""

a=np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float64)

""""shape means the number of rows and columns in the array, 
while size means the total number of elements in the array."""
print(a)
print("Shape of the array:", a.shape)
print("Size of the array:", a.size)
