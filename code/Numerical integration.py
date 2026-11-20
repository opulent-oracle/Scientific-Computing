# trapezoidal rule 

import numpy as np
from scipy.integrate import trapezoid

x = np.linspace(0, 2, 1000)
y = x**2

area = trapezoid(y, x)

print("Approximate area:", area)

# simpson's rule

import numpy as np
from scipy.integrate import simpson

x = np.linspace(0, 2, 100)
y = x**2

area = simpson(y, x=x)

print("Approximate area:", area)

#Real-world application: Calculating distance travelled.
#Suppose a vehicle's velocity changes over time.

import numpy as np
from scipy.integrate import trapezoid

time = np.array([0, 1, 2, 3, 4])
velocity = np.array([0, 5, 10, 15, 20])

distance = trapezoid(velocity, time)

print("Distance travelled:", distance, "metres")
