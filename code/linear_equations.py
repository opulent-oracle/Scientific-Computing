# a company has two types of servers:
# - Type A uses 4 CPU units and 8 GB of memory.
# - Type B uses 2 CPU units and 12 GB of memory.
# - The total usage is 20 CPU units and 72 GB of memory.

import numpy as np

# Coefficients of the equations
A = np.array([
    [4, 2],
    [8, 12]
])

# Known totals
b = np.array([20, 72])

# Solve the equations
solution = np.linalg.solve(A, b)

print("Type A servers:", solution[0])
print("Type B servers:", solution[1])

# Verify the solution
print("Verification:", A @ solution)

# Example 2 
# 2x + y = 8
# x + y = 5

import numpy as np

A = np.array([
    [2, 1],
    [1,1]
])

# the known totals 

B = np.array([8, 5])

# solve the equations 
solution = np.linalg.solve(A, B)

print("value of x:", solution [0])
print("value of y:", solution [1])

# verify the solution 
print("Solution verification:", A @ solution)