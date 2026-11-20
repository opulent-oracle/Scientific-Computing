# example of how to calculate eigenvalues and eigenvectors of a matrix using numpy in python.

import numpy as np

A = np.array([
    [2, 0],
    [0, 3]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigevalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

# Example 2 

import numpy as np

A = np.array([
    [4, 0],
    [0, 2]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)