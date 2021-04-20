import numpy as np

def ode(x, y):
    return y - 2 * x / y

def f(x):
    return np.sqrt(1+2*x)

def RungeKutta(bound, start):
    h = 0.1
    n = int(bound/h)
    x = np.zeros(n)
    y = np.zeros(n)
    sample = np.zeros(n)
    for i in range(0, n):
        x[i] = 0+i*h
        sample[i] = f(x[i])
    y[0] = start
    for i in range(1, n):
        k1 = ode(x[i-1], y[i-1])
        k2 = ode(x[i-1] + h/2, y[i-1] + h/2*k1)
        k3 = ode(x[i-1] + h/2, y[i-1] + h/2*k2)
        k4 = ode(x[i-1] + h, y[i-1] + h * k3)
        y[i] = y[i-1] + h/6*(k1 + 2 * k2 + 2 * k3 + k4)
    return y, sample

y, sample = RungeKutta(2, 1)
print(y)
print(y)

