# Newton-Raphson method for root finding

import scipy.optimize as opt

def f(x):
    return x**2 - 9

def df(x):
    return 2*x

root = opt.newton(f, 4, fprime=df)

print("Root:", root)
print("Function value at root:", f(root))

# secant method for root finding

import scipy.optimize as opt

def f(x):
    return x**2 - 16

root = opt. newton(f, 3, fprime=None, x1=5)

print("Root:", root)
print("Function value:", f(root))
