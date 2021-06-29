import matplotlib.pyplot as plt
import numpy as np

s = [0.99]
i = [0.01]
r = [0]
t = [i for i in np.arange(0, 20, 0.01)]
N = 1300000000
lambda_0 = 2
w = 0.5
step = 0.01
for j in range(len(t) - 1):
    q_0 = s[-1] - lambda_0 * s[-1] * i[-1] * step
    q_1 = i[-1] + (lambda_0 * s[-1] * i[-1] - w * i[-1]) * step
    q_2 = r[-1] + w * i[-1] * step
    s.append(q_0)
    i.append(q_1)
    r.append(q_2)
print(s)
print(i)
print(r)
print(t)
plt.plot(t, s, label='s')
plt.plot(t, i, label='i')
plt.plot(t, r, label='r')
plt.legend()
plt.show()
