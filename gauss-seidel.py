import numpy as np

def GaussSeidel(A, B, N, x):
    L = np.tril(A)
    U = A - L

    for i in range(N):
        x = np.dot(np.linalg.inv(L), B - np.dot(U, x))
    return x

A = np.array([[10, -1, -2], [-1, 10, -2], [-1, -1, 5]])
B = np.array([7.2, 8.3, 4.2])
x = np.array([1.0, 1.0, 1.0])

answer = GaussSeidel(A, B, 30, x)

print(answer)
