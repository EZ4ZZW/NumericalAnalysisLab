import numpy as np

def largrange(x, y, x0):
    n = len(x)
    res = 0
    for i in range(n):
        param = np.append(x[:i], x[(i+1):])
        numerator = (x0 - param).prod()
        denominator = (x[i] - param).prod()
        res += y[i]*numerator/denominator
    return res

x = np.array([0.5, 0.6, 0.4, 0.7])
y = np.array([-0.6931, -0.5108, -0.9163, -0.3567])
answer = largrange(x, y, 1)

print(np.around(answer, 4))
