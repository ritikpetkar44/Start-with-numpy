"""
empty() and ravel()
----------------------------
ye ek simple function hai jo ek array create karta hai bina kisi initial value ke.
 iska use tab hota hai jab hume ek array ki zarurat hoti hai lekin hume uske initial values ki parwah nahi hoti.

ravel() function ka use hota hai multi-dimensional array ko 1D array me convert karne ke liye."""
import numpy as np
a = np.empty((3, 3))
print(a)
"""output:
random values in a 3x3 array
"""


b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)
"""output:
ek 3x3 array with values from 1 to 9
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""
c = b.ravel()
print(c)
"""output:
ek 1D array with values from 1 to 9
[1 2 3 4 5 6 7 8 9]
"""