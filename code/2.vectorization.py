#  vectorisation example 
#  sin^2(x)+cos^2(x)=1
#  calculate for x=[0,pi/2,pi]

import numpy as np
x = np.array([0, np.pi/2, np.pi])
y = np.sin(x)**2 + np.cos(x)**2

print("Angles:", x)
print("Results:", y)



# angles = np.array([0, np.pi/4, np.pi/3, np.pi/2])
# write a program that ;
# Calculates the sine of every angle.
# Calculates the cosine of every angle.
# Calculates the square of each sine value plus the square of each cosine value.
# Prints all three results.

import numpy as np

x = np.array([0, np.pi/4, np.pi/3, np.pi/2])
y = np.sin(x)
z = np.cos(x)
w = y**2 + z**2

print ("Angles:", x)
print ("sine values:",y)
print ("cosine values:", z)
print ("results:", w)














