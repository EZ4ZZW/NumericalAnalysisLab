import numpy as np

def GetColumRes(arr, j):
    n = len(arr[:,0])
    colum = np.zeros(n)
    for i in range(j-1, n):
        colum[i] = (arr[i, j-1] - arr[i-1, j-1])/(arr[i, 0] - arr[i-j+1, 0])
    return colum

def CalculateDividedDiffernces(x, y):
    n = len(x)
    arr = np.zeros((n, n+1))
    arr[0:n, 0] = x
    arr[0:n, 1] = y
    for i in range(2, n+1):
        arr[:, i] = GetColumRes(arr, i)
    print(arr)
    return arr

def newton(x, y, x0):
    res = y[0]
    n = len(x)
    factor = 1
    DD = CalculateDividedDiffernces(x, y)
    for i in range(1,n):
        factor *= (x0-x[i-1])
        res += DD[i, i+1]*factor
    return res

x = np.array([0.5, 0.6, 0.4, 0.7])
y = np.array([-0.6931, -0.5108, -0.9163, -0.3567])
answer = newton(x, y, 1)
print(np.around(answer, 4))
