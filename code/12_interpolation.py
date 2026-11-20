# linear interpolation 
import numpy as np

time = np.array([8, 10, 12])
temperature = np.array([20, 24, 28])

estimated_temp = np.interp(9, time, temperature)

print("Estimated temperature at 9 AM:", estimated_temp)

#polynomial interpolation

import numpy as np
from scipy.interpolate import interp1d

x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])

interpolation = interp1d(x, y, kind='quadratic')

estimated_value = interpolation(2.5)

print("Estimated value:", estimated_value)

#cubic interpolation

import numpy as np
from scipy.interpolate import CubicSpline

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

spline = CubicSpline(x, y)

estimated_value = spline(2.5)

print("Estimated value:", estimated_value)


