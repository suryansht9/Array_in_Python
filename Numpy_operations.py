import numpy as np

# Create two NumPy arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
add = a + b

# Element-wise multiplication
multiply = a * b

# Dot product
dot_product = np.dot(a, b)

# Square root of elements in a
sqrt_a = np.sqrt(a)

# Mean of array b
mean_b = np.mean(b)

# Print results
print("Array a:", a)
print("Array b:", b)
print("Addition:", add)
print("Multiplication:", multiply)
print("Dot product:", dot_product)
print("Square root of a:", sqrt_a)
print("Mean of b:", mean_b)
