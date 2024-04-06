import numpy as np

# Define the matrix
A = np.array([[1, 1, 3], [1, 3, -3], [-2, -4, -4]])

# Calculate the square of the matrix
A_square = np.dot(A, A)
A_cube = np.dot(A,A_square)

# Print the square of the matrix
print(A_cube)