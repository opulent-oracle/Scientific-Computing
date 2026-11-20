import numpy as np
from scipy.integrate import solve_ivp

# Define the differential equation
def f(t, y):
    return 2 * t

# Time values at which we want results
t_eval = np.linspace(0, 1, 11)

# Solve the ODE
solution = solve_ivp(
    f,
    (0, 1),
    [1],
    t_eval=t_eval
)

# Display results
print("Time:", solution.t)
print("Values of y:", solution.y[0])

#Real-world application:a population of bacteria grows at a rate proportional to its current population.

import numpy as np
from scipy.integrate import solve_ivp

def population_growth(t, P):
    return 0.2 * P

time_points = np.linspace(0, 10, 11)

result = solve_ivp(
    population_growth,
    (0, 10),
    [100],
    t_eval=time_points
)

print("Time:", result.t)
print("Population:", result.y[0])