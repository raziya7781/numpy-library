import numpy as np

# create an array
arr = np.array([1, 2, 3, 4, 5])

# check if none of the elements is zero
result = np.all(arr != 0)

print("Array:", arr)
print("None of the elements is zero:", result)
