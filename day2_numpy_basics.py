# Day 2 - NumPy Basics

import numpy as np

# Create array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Array operations
print("Add 2:", arr + 2)
print("Multiply by 3:", arr * 3)

# 2D Array
matrix = np.array([[1, 2], [3, 4]])
print("Matrix:\n", matrix)

# Shape of array
print("Shape:", matrix.shape)

# Mean value
print("Mean:", np.mean(arr))
