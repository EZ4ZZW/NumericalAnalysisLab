import numpy as np

def linear(x, y, x0):
    res = y[1] + (y[1] - y[0])*(x0 - x[1])/(x[1] - x[0])
    return res

x = np.array([0.5, 0.6])
y = np.array([-0.6931, -0.5108])
answer = linear(x, y, 1)
print(np.around(answer, 4))
