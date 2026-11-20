#f(x)=(x-3)^2+4

from scipy.optimize import minimize_scalar

# Define the function
def f(x):
    return (x - 3)**2 + 4

# Find the minimum value
result = minimize_scalar(f, bounds=(0, 10), method="bounded")

print("Optimal x:", result.x)
print("Minimum value:", result.fun)

#Real-world application:
#Suppose a company estimates its production cost using:
#C(x)=(x-50)^2+100

from scipy.optimize import minimize_scalar

def production_cost(x):
    return (x - 50)**2 + 100

result = minimize_scalar(
    production_cost,
    bounds=(0, 100),
    method="bounded"
)

print("Optimal production level:", result.x)
print("Minimum production cost:", result.fun)

