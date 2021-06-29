import numpy as np
from pylab import *
import pandas as pd
import matplotlib.pyplot as plt

experimen_data = pd.read_csv(open('data.csv'))
plt.plot(list(experimen_data['拉伸应变 (位移)'][1:]), list(experimen_data['拉伸应力'][1:]), color='black')
plt.xlabel('stretching strain', fontsize=14)
plt.ylabel('stretching stress', fontsize=14)

# 第一个最大值
max = 0.0
n = 0
for i in experimen_data['拉伸应力'][1:]:
    if eval(i) > max:
        max = eval(i)
        continue
    n += 1
    if n > 100:
        break
print('the first max value is:{}'.format(max))

# 斜率
X0 = list(experimen_data['拉伸应变 (位移)'][1:1000])
X = []
for i in X0:
    a = eval(i)
    X.append(a)
T0 = list(experimen_data['拉伸应力'][1:1000])
T = []
for i in T0:
    a = eval(i)
    T.append(a)

Xn = [[1] * len(X), X]
W = np.dot(np.dot(np.linalg.inv(np.dot(Xn, np.transpose(Xn))), Xn), np.transpose(T))
print('slop is {}'.format(W[1]))

# 绘制拟合曲线
Y = []
for i in np.arange(0, 0.02, 0.00001):
    Y += [W[0] + W[1] * i]
Xn1 = np.arange(0, 0.02, 0.00001)
plt.plot(Xn1, Y)

# 寻找最小点


# 索引第一个最大值坐标
# 确定屈服左边界
D0 = list(experimen_data['拉伸应力'][1:])
D = []
for i in D0:
    a = eval(i)
    D.append(a)
index_max = D.index(max)
# 从图上看出屈服应力应小于400
min = 400
n = 0
for i in experimen_data['拉伸应力'][index_max:]:
    if eval(i) < min:
        min = eval(i)
        continue
    n += 1
    if n > 500:
        break
print('the min value in yield interval is:{}'.format(min))

# 最大应力
stress_max = 0
for i in D:
    if i > stress_max:
        stress_max = i
print('the max stress is {}'.format(stress_max))

# 画出几条直线标识
Xn2 = np.arange(0, 0.15, 0.00001)
Stress_max = []
Max = []
Min = []
for i in Xn2:
    Max.append(max)
    Min.append(min)
    Stress_max.append(stress_max)
plt.plot(Xn2, Max)
plt.plot(Xn2, Min)
plt.plot(Xn2, Stress_max)
plt.show()
