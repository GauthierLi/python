import random as rdm
from pylab import *
import numpy as np

# 生成1000个训练目标
a = []
for i in range(5000):
    b = rdm.uniform(-1.5,2.5)                 # y
    c = rdm.uniform(-0.5,2.5)                 # x
    if b+c>1 and b-c<1 and b+3*c<5:
        a += [[b,c,1]]
    else:
        a += [[b,c,-1]]
print(a)
X1 = []
Y1 = []
X2 = []
Y2 = []
for i in a:
    if i[2]==1:
        X1 += [i[1]]
        Y1 += [i[0]]
    else:
        X2 += [i[1]]
        Y2 += [i[0]]
scatter(X1,Y1,s=5,c = 'r')
scatter(X2,Y2,s=5,c = 'b')
show()

# 定义激活函数
def y(X,W):
    if np.dot(np.transpose(X),W) > 0:        # X = [y, x, -1]  W = [W1 , W2, sita]
        return 1
    else:
        return -1

# 隐层第一个神经元
# 感知器初始化
W1 = [0.01, 0.01, 0.01]
for i in a:
    Y = y([i[0], i[1], -1], W1)
    for j in range(len(W1)):
        W1[j] += (1/5000)*(i[2] - Y)*i[j]
