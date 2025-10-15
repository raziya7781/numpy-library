import numpy as np

# create an array
arr = np.array([4, 7, 2, 9, 5, 1, 8, 3])

print("Original Array:", arr)

# specify a number
num = 5

# elements less than num
less_than_num = arr[arr < num]
print("\nElements less than", num, ":", less_than_num)

# elements greater than num
greater_than_num = arr[arr > num]
print("Elements greater than", num, ":", greater_than_num)
