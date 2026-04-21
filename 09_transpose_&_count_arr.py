"""
transpose() and count_nonzero()
transpose() is used to change the shape of an array without changing its data.
transpose se hum array ke dimensions ko swap kar sakte hain. For example, 
agar humare paas ek 2D array hai jiska shape (m, n) hai, to uska transpose hume ek n x m array dega."""

import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
"""output:
[[1 2 3]
 [4 5 6]]
"""
b = a.transpose()
print(b)
"""output:
[[1 4]
 [2 5]
 [3 6]]
"""


"""count_nonzero() function ka use hota hai array me non-zero elements ki counting ke liye.
ye function hume batata hai ki array me kitne non-zero elements hain. iska syntax hai:
numpy.count_nonzero(arr)"""

c = np.array([[0, 1, 2], [3, 0, 4], [5, 6, 0]])
print(c)
"""output:
[[0 1 2]
 [3 0 4]
 [5 6 0]]
"""