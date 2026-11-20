# bisection method for root finding 

import scipy.optimize as opt

def f(x):
    return x**2 - 9

root = opt.bisect(f, 2, 4)

print("Root:", root)
print("Function value at root:", f(root)) # it substitutes the root back to the original function.

# fixed-point iteration method for root finding 
x = 1.0

for i in range(10):
    x_new = 2 - x**2
    x = x_new

    print(f"Iteration {i + 1}: x = {x:.6f}")

# f(x)=x^2-16

import scipy.optimize as opt
def f(x):
     return x**2 - 16

root = opt.bisect(f, 1, 5)

print("Root:", root)
print("Function value at root:", f(root))