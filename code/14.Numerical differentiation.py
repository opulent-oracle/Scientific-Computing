def f(x):
    return x**2

x = 3
h = 0.001

forward = (f(x + h) - f(x)) / h

backward = (f(x) - f(x - h)) / h

central = (f(x + h) - f(x - h)) / (2*h)

print("Forward difference:", forward)
print("Backward difference:", backward)
print("Central difference:", central)