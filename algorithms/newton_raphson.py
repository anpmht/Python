# define the function to find the roots of
def func(x):
    return x**3 - 2*x - 5

# define the Newton-Raphson algorithm
def newton_raphson(x0, tol, max_iter):
    i = 0
    while i < max_iter:
        f = func(x0)
        h = 1e-5 # small step size
        df = (func(x0 + h) - func(x0 - h))/(2*h) # central difference approximation of derivative
        x1 = x0 - f/df
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
        i += 1
        print(x0)
    return None

# set the initial guess, tolerance, and maximum number of iterations
x0 = 6
tol = 1e-9
max_iter = 1000

# call the newton_raphson function
root = newton_raphson(x0, tol, max_iter)

# print the result
if root is not None:
    print("Root found: x = ", root)
else:
    print("Root not found within ", max_iter, " iterations.")
