## PROJECT DOCUMENTATION

### 1. Introduction

This document presents the implementation and analysis of the scientific computing tasks completed using Python.

The project explores various numerical and computational techniques used to solve mathematical problems. It demonstrates how scientific Python libraries can be applied to perform numerical calculations, solve equations, analyze data, and simulate real-world situations.

### 2. Objectives

The main objectives of this project are:

1. To apply scientific computing concepts using Python.
2. To implement numerical methods for solving mathematical problems.
3. To explore the application of NumPy, SciPy, and Matplotlib.
4. To analyze and interpret numerical results.
5. To demonstrate how scientific computing techniques can be applied to practical problems.

### 3. Tools and Technologies

| Tool/Library | Purpose |
|---|---|
| Python | Programming language used for implementation |
| NumPy | Numerical operations and array computations |
| SciPy | Scientific and mathematical computations |
| Matplotlib | Data visualization and plotting |

### 4. Task Implementations and Analysis

This section presents the objectives, methods, inputs, outputs, and interpretation of each task completed in the assignment.

## Task 2: NumPy Arrays and Numerical Computation

This task demonstrates how NumPy arrays can be used to perform numerical calculations on multiple values. The program analyzes 24 hourly temperature readings and calculates the daily mean, minimum and maximum temperatures. It also converts the readings from Celsius to Fahrenheit using the formula F = 1.8C + 32.

**Results and interpretation:** The output summarizes the daily temperature conditions and displays the first six readings in Fahrenheit.

**Parameter variation:** Changing one or more temperature readings affects the calculated mean, minimum and maximum values.

**Modified application:** The same approach can be used to monitor cold-storage temperatures by calculating average, minimum and maximum readings to check whether stored products remain within the required temperature range.


## 6. Task 3: Mathematical Functions and Vectorization

This task demonstrates how NumPy performs mathematical operations on many values simultaneously. The program generates one million network latency measurements in milliseconds, converts them into seconds and squares the values.

**Method:** NumPy vectorized operations are compared with a traditional Python loop. The `timeit` module measures their execution time.

**Results and interpretation:** Both approaches perform the same calculations, but vectorization is generally faster because NumPy processes arrays efficiently. The program also displays the first five calculated values and the measured execution times. The actual speed-up depends on the computer used.

**Parameter variation:** Changing the number of generated measurements affects the amount of data processed and the execution time. Increasing the dataset generally increases the processing time.

**Modified application:** The same technique can be used in image processing. An image can be represented as a NumPy array, and brightness adjustments can be applied to many pixel values simultaneously. This avoids manually processing each pixel using loops.

**Conclusion:** Vectorization makes numerical calculations simpler and more efficient, especially when working with large datasets.

## Task 4: Floating-Point Arithmetic and Numerical Errors

This task explores how computers represent decimal numbers and why small rounding errors occur. The program compares `0.1 + 0.2` with `0.3`, calculates absolute and relative errors, and compares a numerically unstable expression with a more stable one.

**Results and interpretation:** Exact comparison may return `False` because decimal values are not always represented precisely in binary. `np.isclose()` provides a tolerance-based comparison, which is more suitable for numerical calculations.

**Parameter variation:** Changing the approximate value used for √2 changes the calculated absolute and relative errors.

**Modified application:** The same concepts can be applied in financial calculations, where rounding errors may affect totals and balances. Appropriate precision and tolerances help reduce these problems.

## Task 5: Matrix Algebra and Matrix Operations

This task demonstrates how matrices can be used to perform mathematical transformations. The program represents four square corners as coordinate points and applies rotation and scaling matrices using NumPy matrix multiplication.

**Results and interpretation:** The transformed coordinates show how the original square changes position and size. The determinant helps indicate whether the transformation is invertible.

**Parameter variation:** Changing the rotation angle or scaling factors produces different transformed coordinates.

**Modified application:** Matrix operations can also be used in image processing to rotate, resize and transform images represented as numerical arrays.

## Task 6: Solution of Systems of Linear Equations

This task demonstrates how simultaneous linear equations can be solved using `np.linalg.solve()`. The program uses CPU and memory requirements to determine the number of two types of servers. The inputs are the coefficient matrix and the resource totals.

**Results and interpretation:** The solution gives 3 Type A servers and 4 Type B servers. The residual checks whether the calculated solution satisfies the original equations.

**Parameter variation:** Changing the total CPU or memory values changes the number of servers calculated.

**Modified application:** The same method can be used to determine quantities of different products that must be manufactured to meet given material and production requirements.

## Task 7: Gaussian Elimination and LU Decomposition

This task explores how a system of linear equations can be solved through matrix factorization. The program uses SciPy's `lu_factor()` to factor a coefficient matrix once and `lu_solve()` to solve it using different measurement vectors.

**Results and interpretation:** The program produces solutions for the different measurement sets. Small residual norms indicate that the calculated solutions closely satisfy the equations.

**Parameter variation:** Changing the measurement vectors changes the solutions while the same LU factorization can still be reused.

**Modified application:** LU decomposition can be applied in engineering simulations where the same system structure is used repeatedly with different input measurements.

## Task 8: Iterative Methods for Linear Systems

This task compares the Jacobi and Gauss-Seidel methods for solving linear systems. The program models temperatures at five points between two boundaries, using an initial guess and repeatedly updating the temperature estimates.

**Results and interpretation:** Both methods approach the direct solution. The convergence graph shows how the maximum change decreases as the iterations progress. A smaller error indicates that the estimates are becoming more stable.

**Parameter variation:** Changing the tolerance affects how accurately the solution must converge before the program stops.

**Modified application:** Iterative methods can also estimate temperatures across a building or a larger heating system where many connected points must be considered.

## Task 9: Eigenvalues and Eigenvectors

This task demonstrates how eigenvalues and eigenvectors describe the behaviour of matrix transformations. The program uses an adjacency matrix to represent connections between four network nodes and calculates their eigenvalues and eigenvectors using `np.linalg.eig()`.

**Results and interpretation:** The dominant eigenvector is normalized to produce importance scores for the network nodes. A higher score indicates a node with greater influence based on the network's connection structure.

**Parameter variation:** Changing the connections in the adjacency matrix changes the calculated importance scores.

**Modified application:** Eigenvector analysis can also be used in ranking web pages or identifying influential individuals in social networks.

## Task 10: Root Finding – Bisection and Fixed-Point Methods

This task demonstrates two methods of finding the root of a nonlinear equation. The program models a heat-balance equation and uses SciPy's `root_scalar()` for bisection, while fixed-point iteration repeatedly applies a rearranged version of the equation.

**Results and interpretation:** Both methods estimate the equilibrium temperature where the heat-balance function equals zero. The graph shows where the function crosses the horizontal axis.

**Parameter variation:** Changing the starting interval for bisection or the initial guess for fixed-point iteration affects the search process and number of iterations.

**Modified application:** Root-finding methods can also be used to determine the break-even point where business revenue equals total costs.

## Task 11: Root Finding – Newton-Raphson and Secant Methods

This task compares Newton-Raphson and Secant methods for finding roots of nonlinear equations. The program calculates the Internal Rate of Return (IRR) of an investment using its cash flows and Net Present Value (NPV) function.

**Results and interpretation:** Both methods estimate the interest rate at which the NPV becomes zero. A value close to zero when the calculated rate is substituted into the NPV function indicates a successful solution.

**Parameter variation:** Changing the initial guesses affects the starting point of the numerical search and may influence convergence.

**Modified application:** These methods can also be used to solve engineering equations, such as finding the operating point of an electrical circuit.

## Task 12: Polynomial and Nonlinear Equation Solving

This task explores solving polynomial and nonlinear equations numerically. The program uses `scipy.optimize.root()` to find the intersection points between a circle and a parabola by solving two equations simultaneously.

**Results and interpretation:** The program produces intersection coordinates from different initial guesses. Small residual values indicate that the calculated points satisfy both equations.

**Parameter variation:** Changing the initial guesses may lead the solver toward different intersection points.

**Modified application:** Nonlinear equation solving can also be used to determine the position where two curved roads, structures or geometric objects intersect.

## Task 13: Interpolation

This task demonstrates how missing values between known data points can be estimated. The program uses hourly temperature measurements and compares linear interpolation with cubic spline interpolation using SciPy.

**Results and interpretation:** The program estimates temperatures at ten-minute intervals, including 10:30. The graph compares the estimated curves with the original measurements.

**Parameter variation:** Changing the measured temperatures or the time at which an estimate is required produces different interpolated values.

**Modified application:** Interpolation can also be used to estimate missing rainfall measurements between recorded observation times.

## Task 14: Curve Fitting and Approximation

This task demonstrates how a mathematical curve can be fitted to observed data. The program uses server response-time measurements at different numbers of concurrent users and applies `curve_fit()` to estimate a quadratic relationship.

**Results and interpretation:** The fitted curve represents the relationship between the number of users and server response time. RMSE measures the difference between observed and predicted values, while the model estimates response time at 400 users.

**Parameter variation:** Changing the measured response times affects the fitted coefficients and predicted values.

**Modified application:** Curve fitting can also be used to study population growth by fitting a mathematical model to population measurements collected over time.

## Task 15: Numerical Differentiation

This task demonstrates how derivatives can be estimated using numerical data. The program uses GPS position measurements taken at different times to estimate speed through forward, central and backward difference methods.

**Results and interpretation:** The calculated values represent estimated vehicle speeds at the recorded times. The graph shows how speed changes as the vehicle moves.

**Parameter variation:** Changing the position measurements or the time intervals affects the estimated speeds.

**Modified application:** Numerical differentiation can also be used to estimate acceleration from recorded vehicle speed measurements.

## Task 16: Numerical Integration

This task explores how numerical integration estimates accumulated quantities from measured data. The program uses smart-meter power readings collected every two hours and compares the trapezoidal rule with Simpson's rule.

**Results and interpretation:** The calculated results estimate total electrical energy consumed over the recorded period in kilowatt-hours (kWh). The difference between the two estimates shows how the numerical methods compare.

**Parameter variation:** Changing the power readings or measurement times changes the estimated energy consumption.

**Modified application:** Numerical integration can also be used to estimate the total distance travelled by a vehicle from its speed measurements over time.

## Task 17: Ordinary Differential Equations – Euler Method

This task demonstrates how Euler's method approximates the solution of an ordinary differential equation. The program applies Newton's law of cooling to estimate how an object initially at 90°C cools towards an ambient temperature of 25°C over 30 minutes.

**Results and interpretation:** The program calculates the temperature at each time step and compares the numerical estimate with the exact solution. The graph shows the cooling process and the difference between the two solutions.

**Parameter variation:** Changing the step size affects the accuracy and number of calculations. A smaller step size generally produces a more accurate approximation.

**Modified application:** Euler's method can also be used to model population growth by estimating how a population changes over time.

## Task 18: Numerical Solution of ODEs Using SciPy

This task demonstrates how SciPy solves ordinary differential equations using `solve_ivp()`. The program models an RC circuit with a 5V supply, a resistance of 1000 ohms and a capacitance of 0.001 farads.

**Results and interpretation:** The program estimates the capacitor voltage as it charges over five seconds. The numerical solution is compared with the exact mathematical solution to check its accuracy.

**Parameter variation:** Changing the resistance, capacitance or supply voltage affects the charging behaviour and final voltage.

**Modified application:** The same numerical solving technique can be used to model the spread of a disease over time using a system of differential equations.

## Task 19: Numerical Optimization

This task explores how optimization can be used to find the minimum cost while satisfying given constraints. The program uses `scipy.optimize.minimize()` to determine the allocation of two server types while ensuring that their combined processing capacity is at least 1000 units.

**Results and interpretation:** The program displays the optimized allocation, total capacity and estimated planning cost. It also checks nearby whole-number combinations because actual servers cannot be divided into fractions.

**Parameter variation:** Changing the server costs or required capacity affects the optimal allocation and minimum cost.

**Modified application:** Optimization can also be applied to production planning by finding the least expensive combination of raw materials needed to meet a production target.

## Task 20: Random Numbers and Monte Carlo Methods

This task demonstrates how random sampling can be used to estimate probabilities. The program generates 100,000 possible network-demand scenarios using a normal distribution and checks how many exceed the server's capacity of 1000 units.

**Results and interpretation:** The estimated overload probability is calculated by dividing the number of overloaded scenarios by the total number of simulations. The graph shows how the estimated probability changes as more simulations are performed.

**Parameter variation:** Changing the number of simulations, average demand or standard deviation affects the estimated overload probability.

**Modified application:** Monte Carlo simulation can also be used in financial risk analysis to estimate the likelihood of investment losses under uncertain market conditions.