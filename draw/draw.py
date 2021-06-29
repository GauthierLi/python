# _*_ encoding:utf-8 _*_
import matplotlib.pyplot as plt
import numpy as np

X = [i for i in np.arange(0, 100)]
Y_1 = [0.0175 + 0.5 * 8.0176 * 10 ** (-6) * i ** 2 for i in X]
Y_2 = [0.025 + 0.5 * 3.1429 * 10 ** (-6) * i ** 2 for i in X]
plt.plot(X, Y_1, label='E_1')
plt.plot(X, Y_2, label='E_2')
plt.legend()
plt.xlabel('w-rotation speed rad/s')
plt.ylabel('E-mechanical energy J')
plt.show()
