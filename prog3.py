import numpy as np

# define two arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 3, 2, 4, 6])

print("Array A:", a)
print("Array B:", b)

# element-wise comparisons
print("\nA > B  :", np.greater(a, b))          # greater
print("A >= B :", np.greater_equal(a, b))     # greater_equal
print("A < B  :", np.less(a, b))              # less
print("A <= B :", np.less_equal(a, b))        # less_equal
print("A == B :", np.equal(a, b))             # equal

# check equality within tolerance
print("\nEqual within tolerance:", np.allclose(a, b, atol=1))
