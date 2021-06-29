import numpy as np
from pylab import *

X = list(np.arange(1896, 2012, 4)) + [1906]
X.remove(1916)
X.remove(1940)
X.remove(1944)
X.sort()
T = np.array([12, 11, 11, 11.2, 10.8, 10.8, 10.8, 10.6, 10.8, 10.3, 10.3, 10.3, 10.4, 10.5, 10.2, 10, 9.95, 10.14, 10.06, 10.25, 9.99, 9.92, 9.96, 9.84, 9.87, 9.85, 9.69])
scatter(X,T)


# # 定义拟合函数
# def f(X,W):
#     return np.dot(W,X)


# 定义损失函数
def L(T, X, W):
    l = len(X)
    M = np.transpose(T) - np.dot(np.transpose(X) ,W)                                          # X.shape(n*2),W.shape(2*1)
    return (np.dot(np.transpose(M), M))/l

Xn = [[1]*len(X),X]
W = np.dot(np.dot(np.linalg.inv(np.dot(Xn, np.transpose(Xn))), Xn),np.transpose(T))
Y = []
for i in np.arange(1896,2012,0.1):
    Y += [W[0] + W[1]*i]
Xn1 = np.arange(1896,2012,0.1)
scatter(Xn1,Y,s=0.1)
xlabel('years')
ylabel('second')
show()
print('损失值：{}'.format(L(T,Xn,W)))


