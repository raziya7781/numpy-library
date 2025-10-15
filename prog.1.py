import numpy as np

# 1. array() -> create array
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([4, 3, 2, 1])
print("Array 1:", arr1)
print("Array 2:", arr2)

# 2. add() -> element-wise addition
print("Addition:", np.add(arr1, arr2))

# 3. all() -> check if all elements are True (non-zero or condition holds)
print("All > 0 in arr1:", np.all(arr1 > 0))

# 4. greater() -> element-wise comparison
print("arr1 > arr2:", np.greater(arr1, arr2))

# 5. greater_equal() -> element-wise comparison
print("arr1 >= arr2:", np.greater_equal(arr1, arr2))

# 6. less() -> element-wise comparison
print("arr1 < arr2:", np.less(arr1, arr2))

# 7. less_equal() -> element-wise comparison
print("arr1 <= arr2:", np.less_equal(arr1, arr2))

# 8. equal() -> element-wise equality
print("arr1 == arr2:", np.equal(arr1, arr2))

# 9. allclose() -> check if two arrays are approximately equal
arr3 = np.array([1.000001, 2.000001])
arr4 = np.array([1.000002, 2.000002])
print("arr3 and arr4 allclose?:", np.allclose(arr3, arr4))

# 10. zeros() -> create array filled with zeros
print("Zeros array:", np.zeros((2, 3)))

# 11. ones() -> create array filled with ones
print("Ones array:", np.ones((2, 3)))

# 12. linspace() -> create evenly spaced numbers
print("Linspace 0 to 1 (5 numbers):", np.linspace(0, 1, 5))

# 13. tolist() -> convert array to Python list
print("Array to list:", arr1.tolist())
