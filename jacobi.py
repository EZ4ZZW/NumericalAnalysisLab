import numpy as np

def Jacobi(A, B, N, x):
    D = np.diag(A)
    R = A - np.diagflat(D)

    for i in range(N):
        x = (B - np.dot(R, x))/D
    return x

A = np.array([[10, -1, -2], [-1, 10, -2], [-1, -1, 5]])
B = np.array([7.2, 8.3, 4.2])
x = np.array([1.0, 1.0, 1.0])

answer = Jacobi(A, B, 30, x)

print(answer)
