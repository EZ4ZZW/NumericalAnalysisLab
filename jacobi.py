import numpy as np

def Jacobi(A, B, N, x):
    D = np.diag(A)
    R = A - np.diagflat(D)

    for i in range(N):
        x = (B - np.dot(R, x))/D
    return x

A = np.array([[2.0, 1.0], [5.0, 7.0]])
B = np.array([11.0, 13.0])
x = np.array([1.0, 1.0])

answer = Jacobi(A, B, 30, x)

print(answer)
