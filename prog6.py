import numpy as np

# create a 2D array
arr = np.array([[10, 25, 8],
                [15, 5, 30],
                [20, 35, 12]])

print("Array:\n", arr)

# find index of max and min along axis 0 (column-wise)
print("\nColumn-wise:")
print("Index of max values:", np.argmax(arr, axis=0))
print("Index of min values:", np.argmin(arr, axis=0))

# find index of max and min along axis 1 (row-wise)
print("\nRow-wise:")
print("Index of max values:", np.argmax(arr, axis=1))
print("Index of min values:", np.argmin(arr, axis=1))
