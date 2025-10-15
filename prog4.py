import numpy as np

# create an array
arr = np.array([4, 2, 7, 2, 9, 7, 2, 4])

print("Array:", arr)

# maximum and minimum
print("\nMax value:", np.max(arr))
print("Min value:", np.min(arr))

# indices of max and min
print("\nIndex of Max value (argmax):", np.argmax(arr))
print("Index of Min value (argmin):", np.argmin(arr))

# repr -> string representation of array
print("\nRepr of array:", repr(arr))

# count occurrences of non-zero elements
print("\nCount of non-zero elements:", np.count_nonzero(arr))

# bincount -> frequency of each integer value
print("\nBincount (frequency count):", np.bincount(arr))

# unique values and their counts
unique_vals, counts = np.unique(arr, return_counts=True)
print("\nUnique values:", unique_vals)
print("Counts:", counts)
