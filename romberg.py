import numpy as np

def f(x):
    return np.sin(x)

def trapezcomp(l, r, k):
    h = (r - l)/k
    x = l
    Sum = f(x)
    for i in range(1, k):
        x += h
        Sum += 2*f(x)
    return (Sum + f(r))*h*0.5

def romberg(x, y, n):
    I = np.zeros((n, n))
    for i in range(0, n):
        I[i, 0] = trapezcomp(x, y, 2**i)
        for j in range(0, i):
            I[i, j+1] = (4**(j+1)*I[i, j] - I[i-1, j])/(4**(j+1)-1)
    return I[n-1, n-1]

answer = romberg(1.0, 2.0, 4)
print(answer)
