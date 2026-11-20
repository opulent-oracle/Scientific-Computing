# LU decomposition 

import numpy as np 
from scipy.linalg import lu

A = np.array([[2, 1], [1, 3]])

P, L, U = lu(A)

print("Original matrix A:")
print (A)

print ("Permutation matrix P:")
print(P)
print("Lower triangular matrix L:")
print(L)
print("Upper triangular matrix U:")
print(U)

print("verifiation:")
print(P @ L @ U)

print("Is the decomposition correct?")
print(np.allclose(A, P @ L @ U))