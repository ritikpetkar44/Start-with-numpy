# ===============================
# NUMPY FINAL PRACTICE SCRIPT
# ===============================

import numpy as np   # numpy import kiya

# -------------------------------
# 1. Array Creation
# -------------------------------
arr1 = np.array([1, 2, 3, 4])   # simple 1D array
arr2 = np.array([[1, 2], [3, 4]])  # 2D array

print("1D Array:", arr1)
print("2D Array:\n", arr2)

# -------------------------------
# 2. Datatype Check
# -------------------------------
print("Datatype of arr1:", arr1.dtype)

# -------------------------------
# 3. Shape & Size
# -------------------------------
print("Shape:", arr2.shape)   # rows x columns
print("Size:", arr2.size)     # total elements

# -------------------------------
# 4. Change Elements
# -------------------------------
arr2[0, 1] = 10   # element update
print("Updated array:\n", arr2)

# -------------------------------
# 5. Zeros & Ones Matrix
# -------------------------------
zero_mat = np.zeros((2, 3))  # null matrix
one_mat = np.ones((2, 3))    # ones matrix

print("Zero Matrix:\n", zero_mat)
print("One Matrix:\n", one_mat)

# -------------------------------
# 6. Reshape & Identity Matrix
# -------------------------------
arr3 = np.arange(6)   # 1D array [0-5]
reshaped = arr3.reshape(2, 3)

identity = np.eye(3)   # identity matrix

print("Reshaped:\n", reshaped)
print("Identity Matrix:\n", identity)

# -------------------------------
# 7. Arange & Linspace
# -------------------------------
arange_arr = np.arange(0, 10, 2)
linspace_arr = np.linspace(0, 1, 5)

print("Arange:", arange_arr)
print("Linspace:", linspace_arr)

# -------------------------------
# 8. Empty & Ravel
# -------------------------------
empty_mat = np.empty((2, 2))  # random garbage values
flattened = reshaped.ravel()  # 2D -> 1D

print("Empty Matrix:\n", empty_mat)
print("Flattened Array:", flattened)

# -------------------------------
# 9. Transpose & Count Non-Zero
# -------------------------------
transpose = reshaped.T
count_nonzero = np.count_nonzero(reshaped)

print("Transpose:\n", transpose)
print("Non-zero elements:", count_nonzero)

# -------------------------------
# 10. Argmax, Argmin, Argsort
# -------------------------------
arr4 = np.array([3, 1, 5, 2])

print("Max index:", np.argmax(arr4))
print("Min index:", np.argmin(arr4))
print("Sorted indices:", np.argsort(arr4))

# -------------------------------
# 11. Arithmetic Operations
# -------------------------------
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# -------------------------------
# 12. Square & Square Root
# -------------------------------
print("Square:", np.square(a))
print("Square Root:", np.sqrt(a))

# -------------------------------
# 13. Axis Sum
# -------------------------------
mat = np.array([[1, 2, 3], [4, 5, 6]])

print("Row-wise sum:", np.sum(mat, axis=1))  # row sum
print("Column-wise sum:", np.sum(mat, axis=0))  # column sum

# -------------------------------
# END
# -------------------------------
