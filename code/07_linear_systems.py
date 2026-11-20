import numpy as np

# Initial guesses
x = 0.0
y = 0.0

# Number of iterations
iterations = 10

for i in range(iterations):

    x_new = (11 - y) / 10
    y_new = (11 - x) / 10

    x = x_new
    y = y_new

    print(f"Iteration {i + 1}: x = {x:.6f}, y = {y:.6f}")

    # example 2

    import numpy as np

# Initial guesses
x = 5.0
y = 3.0

# Number of iterations
iterations = 5

for i in range(iterations):

    x_new = (11 - y) / 10
    y_new = (11 - x) / 10

    x = x_new
    y = y_new

    print(f"Iteration {i + 1}: x = {x:.6f}, y = {y:.6f}")