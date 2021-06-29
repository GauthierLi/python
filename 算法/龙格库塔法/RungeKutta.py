# -*- coding:utf-8 -*-
import math
from pylab import *


def aim_func(*y):
    return y[1]

def Runge_Kutta(function, intervall, step, *args):
    '''

    :param function: 微分方程满足的y'=f(y, x)的关系,并且画图
    :param intervall: 想要画出的区间
    :param step: 要求的精度，比如精度0.1，精度0.01等等
    :param args: 给出初值(x_0, y_0)初值必须和区间左边对齐
    :return: 返回一个y的值列
    '''
    lenth = len(args)
    # 定义步长
    h = step
    x_n = [intervall[0] + h * i for i in range(math.ceil((intervall[-1] - intervall[0]) / step))]
    # 开辟空间存放结果
    y_n = []
    # 将x_0和y_0放入列表中
    y_n.append(args[1])
    for i in range(len(x_n)):
        k_1 = function(x_n[i], y_n[i])
        k_2 = function(x_n[i] + (h / 2), y_n[i] + (h * k_1 / 2))
        k_3 = function(x_n[i] + (h / 2), y_n[i] + (h * k_2 / 2))
        k_4 = function(x_n[i] + (h / 2), y_n[i] + (h * k_3))
        q = y_n[i] + h * (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6
        y_n.append(q)
    del y_n[-1]
    scatter(x_n, y_n, s=0.1)
    xlabel('x')
    ylabel('y')
    show()
    return y_n


def fun(*args):
    return np.cos(args[0])**2/(1+np.exp(-args[0]))


a = Runge_Kutta(fun, [-np.pi/4, np.pi/4], 0.001, -np.pi/4, 0)
print(a)
