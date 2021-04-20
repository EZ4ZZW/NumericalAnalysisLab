import numpy as np
import math as m

def f(x):
    return m.sin(x)/x

def Calc():
    eps = 1e-7
    Flag = True
    l = 0.0
    r = 1.0
    h = r - l
    t1 = 1.0*(h/2)*(1+f(r))
    t2 = 0.0
    while Flag:
        sum = 0
        x = l + h/2
        while x < r:
            sum += f(x)
            x += h
        t2 = t1/2 + h*sum/2
        h /= 2.0
        if abs(t2 - t1) < abs(eps):
            Flag = False
        t1 = t2
    res = t2
    return res

answer = Calc()
print(np.around(answer, 6))
