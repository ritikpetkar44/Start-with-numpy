"""
This module provides a single function, `dtype`, which is used to create
a data type object that describes the type of data stored in a numpy array. 
its allows you to specify the type of data that you want to store in a numpy array, such as integers, floating-point numbers, or complex numbers.
"""
import numpy as np


#assigning a numpy array with a specific data type
#In this example, we are creating a numpy array with the data type of int32, 
# which means that the array will store 32-bit integers.

a= np.array([1, 2, 3, 45, 56],np.int32)
print(a)

#The dtype attribute of a numpy array returns the data type of the elements in the array.

print(a.dtype)
