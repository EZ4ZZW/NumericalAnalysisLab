import numpy as np
import math as m

def f(x):
    return x**3-x-2

def binary(x, y):
    res = 0
    eps = 1e-3
    h = 1e-3
    l = x
    r = y
    while l <= r:
        mid = (l+r)/2
        if abs(f(mid)-0) < eps:
            return mid
        if f(mid) < 0:
            l = mid + h
        else:
            r = mid - h
    return -1

answer = binary(1.0, 2.0)
print(np.around(answer, 4))
