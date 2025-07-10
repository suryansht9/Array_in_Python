import numpy as np

# Create two 2D arrays (matrices)
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Matrix multiplication (dot product)
C = np.dot(A, B)

# Transpose of matrix A
A_T = np.transpose(A)

# Inverse of matrix A (if it's invertible)
A_inv = np.linalg.inv(A)

# Print results
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("A dot B (Matrix multiplication):\n", C)
print("Transpose of A:\n", A_T)
print("Inverse of A:\n", A_inv)
