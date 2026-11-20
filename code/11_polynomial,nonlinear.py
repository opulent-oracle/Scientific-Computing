import numpy as np

coefficients = [1, -5, 6]

roots = np.roots(coefficients)

print("Roots:", roots)

# f(x)=e^x-5

import numpy as np
from scipy.optimize import root_scalar

def f(x):
    return np.exp(x) - 5

result = root_scalar(f, bracket=[0, 3], method='brentq')

print("Root:", result.root)
print("Function value:", f(result.root))

# real world applicaton
# a population growth model:
#P(t)=100e^{0.2t}
#determine when the population reaches 500.

import numpy as np
from scipy.optimize import root_scalar

def population(t):
    return 100 * np.exp(0.2*t) - 500

result = root_scalar(population, bracket=[0, 20], method='brentq')

print("Time to reach 500:", result.root)