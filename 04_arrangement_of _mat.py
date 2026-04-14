"""
how to change elements in an array
This module provides functions to change the elements of a numpy array.
You can change the elements of an array by using indexing and assignment.

Example usage:"""
import numpy as np
a=np.array([[1, 1, 1], [1, 1, 1],[1, 1, 1]], dtype=np.float64)

""""To change the elements of an array, you can use indexing and assignment.
in array indexing starts from 0, so the first element is at index 0, the second element is at index 1, and so on."""

print(a)
a[0, 0] = 10
a[1, 1] = 20
a[2, 2] = 30


print("Array after changing elements:")
print(a)
print(a.dtype)
