import matplotlib.pyplot as plt
import numpy as np


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fake_fac(n):
    return np.sqrt(2 * np.pi * n) * np.power((n / np.e), n)


Y_0 = []
Y_1 = []
error = []
X = []
for i in range(100):
    Y_0.append(factorial(i))
    Y_1.append(fake_fac(i))
    error.append((Y_0[-1] - Y_1[-1])/Y_0[-1])
    X.append(i)
plt.scatter(X, Y_0, label='real',marker='o')
plt.scatter(X, Y_1, label='fake',marker='x')
plt.legend()
plt.show()
plt.plot(X, error)
plt.title('error rate')
plt.show()
