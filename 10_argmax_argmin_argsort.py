# Argmax, Argmin, and Argsort
#1 argmax
"""
argmax se hum array me maximum value ke index ko find kar sakte hain. iska syntax hai:
numpy.argmax(arr)
"""
import numpy as np
a = np.array([1, 3, 2, 5, 4])
index_max = np.argmax(a)
print("Index of maximum value:", index_max)
"""output:
Index of maximum value: 3
"""



#2 argmin
"""argmin se hum array me minimum value ke index ko find kar sakte hain. iska syntax hai:
numpy.argmin(arr)
"""
index_min = np.argmin(a)
print("Index of minimum value:", index_min)
"""output:
Index of minimum value: 0
"""



#3 argsort
"""argsort se hum array ke elements ko sort karne ke liye unke indices ko return karte hain. iska syntax hai:
numpy.argsort(arr)
"""
sorted_indices = np.argsort(a)
print("Indices of sorted array:", sorted_indices)
"""output:
Indices of sorted array: [0 2 1 4 3]
"""