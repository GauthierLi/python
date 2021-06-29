# coding:utf-8
import numpy as np
from pylab import *

X = np.array([i + 1 for i in range(11)])
T_0 = np.array([44, 198, 217, 321, 544, 634, 897, 1377, 2076, 2844, 4515])
T = [np.log(i) for i in T_0]
scatter(X, T_0)


# 定义损失函数
def L(T, X, W):
    l = len(X)
    M = np.transpose(T) - np.dot(np.transpose(X), W)  # X.shape(n*2),W.shape(2*1)
    return (np.dot(np.transpose(M), M)) / l


Xn = [[1] * len(X), X]
W = np.dot(np.dot(np.linalg.inv(np.dot(Xn, np.transpose(Xn))), Xn), np.transpose(T))
Y = []
for i in np.arange(0, 12, 0.03):
    Y += [W[0] + W[1] * i]
Xn1 = np.arange(0, 12, 0.03)
Y_real = [np.exp(i) for i in Y]
scatter(Xn1, Y_real, s=0.1)
xlabel('day^th')
ylabel('number')
print('损失值：{}'.format(L(T, Xn, W)))
show()

# 拟合函数
def F(x):
    q = np.exp(W[0]) * np.exp(W[1] * x)
    return q
print('预测明天有{}例被感染'.format(F(12)))

truncation_error = []
for i in range(11):
    q = T_0[i] - F(i+1)
    truncation_error.append(q)
print(truncation_error)
