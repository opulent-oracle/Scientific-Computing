# random numbers 
#Estimating π (Pi)

import numpy as np

# Number of random points
N = 1000

# Generate random coordinates
x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)

# Identify points inside the circle
inside_circle = (x**2 + y**2) <= 1

# Count points inside the circle
inside = np.sum(inside_circle)

# Estimate pi
pi_estimate = 4 * inside / N

print("Total points:", N)
print("Points inside circle:", inside)
print("Estimated value of pi:", pi_estimate)