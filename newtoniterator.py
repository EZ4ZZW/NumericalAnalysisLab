import numpy as np
import math as m

# f(x) = x**3 - x - 2
# df/dx = 3x**2 -1

def df(x):    
    return 3*x**2 - 1

def f(x):
    return x**3 - x - 2

def newton(x):
    eps = 1e-7
    x0 = x
    x1 = x0 - f(x0)/df(x0)
    while abs(x1-x0) > eps:
        t = x1
        x1 = t - f(t)/df(t)
        x0 = t
    return x1

answer = newton(1.0)
print(np.around(answer, 4))
