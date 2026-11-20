import numpy as np

x = 0.1
y = 0.2
z = 0.3

result = x + y

print("Calculated result:", result)
print("Expected result:", z)
print("Exact comparison:", result == z)
print("Approximate comparison:", np.isclose(result, z))

# The output differs from the expected value due to floating point representation errors in computers 
# The result ==z returns false because the calculated result's stored floating points differ slightly from the expected value of z.
# The np.isclose(result, z) returns true because it checks if the two values are sufficiently close to each other within a tolerance.
