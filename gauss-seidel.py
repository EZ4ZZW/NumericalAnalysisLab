import numpy as np

def GaussSeidel(A, B, N, x):
    L = np.tril(A)
    U = A - L

    for i in range(N):
        x = np.dot(np.linalg.inv(L), B - np.dot(U, x))
    return x

A = np.array([[2.0, 1.0], [5.0, 7.0]])
B = np.array([11.0, 13.0])
x = np.array([1.0, 1.0])

answer = GaussSeidel(A, B, 30, x)

print(answer)
