import numpy as np

def ode(x, y):
    return y - 2 * x / y

def f(x):
    return np.sqrt(1+2*x)

def Euler(bound, start):
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
        yp = y[i-1] + h*ode(x[i-1], y[i-1])
        yc = y[i-1] + h*ode(x[i], yp)
        y[i] = (yp+yc)/2.0
    return y, sample

answer,sample = Euler(2, 1)
print(answer)
print(sample)
