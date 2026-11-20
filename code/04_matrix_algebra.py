#Representing matrices in python is done as follows:

import numpy as np

A = np.array([[1, 2], [3, 4]])
print("Matrix:", A)

# to check the shape of the matrix we say:

print(A.shape)  # This tells us the number of rows and columns.

# matrix addition 

import numpy as np

A = np.array([
    [2, 3],
    [1, 4]
])

B = np.array([
    [6, 8],
    [7, 5]
])

result = A + B

print(result)


# matrix mulptiplication

import numpy as np
A = np.array([
    [2, 3],
    [1, 4]
])
B = np.array([
    [6, 8],
    [7, 5]
])
result = A @ B  # or np.dot(A, B) can also be used for matrix multiplication
print(result)

# A * B performs element-wise multiplication, not matrix multiplication. For matrix multiplication, we use the @ operator or np.dot().

# Matrix determinant
det_A = np.linalg.det(A)
print("Determinant of A:", det_A)

# matrix inverse 

inverse = np.linalg.inv(A)

print(inverse)

# to verify result = A @ inverse

#  matrix transpose 

transpose_A = A.T
print("Transpose of A:", transpose_A)

# MATRIX OPERATION 
# A = [2, 3]    B = [1, 2] 
#     [4, 5]        [3, 4]
# Write a Python program that:
#1. Creates both matrices using NumPy.
#2. Displays their dimensions.
#3. Adds the matrices.
#4. Multiplies them element by element.
#5. Performs matrix multiplication.
#6. Calculates the determinant of A.
#7. Calculates the inverse of A.

import numpy as np 

A = np.array([
    [2, 3],
    [4, 5]
])

B = np.array([
    [1, 2],
    [3, 4]
])

X = A + B
Y = A * B
Z = A @ B
W = np.linalg.det(A)
P = np.linalg.inv(A)

print("sum of matrices:", X)
print("element-wise product:", Y)
print("matrix product:", Z)
print("determinant of A:", W)
print("inverse of A:", P)

