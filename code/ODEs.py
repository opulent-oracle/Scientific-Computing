#Euler's method

import numpy as np
def f(t,y):
    return 2*t

h = 0.1
t = 0
y = 1

for i in range(10):
    y = y + h*f(t, y)
    t = t + h
    print(f"Time: {t:.1f}, y: {y:.4f}")

#Real-world application: Population growth
population = 100
h = 1

def growth(t, P):
    return 0.2*P

for t in range(5):
    population = population + h*growth(t, population)
    print(f"Year {t+1}: Population = {population:.2f}")










