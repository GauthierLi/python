import math
from pylab import *
import random

random.seed()


def aim_func(*y):
    return y[1]


def Runge_Kutta( function, intervall, step, *args):
    '''

    :param function: equation which satisfied y'=f(y, x),and draw piction
    :param intervall: input the interval to fraw
    :param step: precision like 0.1，0.01 ...
    :param args: give the initial number (x_0, y_0) 初值必须和区间左边对齐
    :return: return a list of function
    '''
    lenth = len(args)
    # define the step
    h = step
    x_n = [intervall[0] + h * i for i in range(math.ceil((intervall[-1] - intervall[0]) / step))]
    y_n = []
    y_n.append(args[1])
    frequence_controler = 0
    for i in range(len(x_n)):
        k_1 = function(x_n[i], y_n[i])
        k_2 = function(x_n[i] + (h / 2), y_n[i] + (h * k_1 / 2))
        k_3 = function(x_n[i] + (h / 2), y_n[i] + (h * k_2 / 2))
        k_4 = function(x_n[i] + (h / 2), y_n[i] + (h * k_3))
        q = (y_n[i] + h * (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6)
        if q <0:
            q = 0
        elif q>1:
            q = 1
        y_n.append(q)
    del y_n[-1]
    scatter(x_n, y_n, s=0.1, marker='o')
    xlabel('events_time')
    ylabel('foal_rate')
    return y_n


# when k = 6.15146464e-06
k1 = 6.15146464 * (10 ** (-6))


def fun(*args):
    return 30 * k1 * (2 * args[1] - 1) / (1 - 60 * k1 * args[0])


# when k = 1.27035477e-05
k2 = 1.27035477 * (10 ** (-5))


def fun1(*args):
    return 30 * k2 * (2 * args[1] - 1) / (1 - 60 * k2 * args[0])


Runge_Kutta( fun, [0, 700], 0.001, 0.00, 0.49)
Runge_Kutta( fun1, [0, 700], 0.001, 0.00, 0.49)
show()

# for i in range(10):
#     Runge_Kutta('b', fun, [0, 300], 0.005, 0.00, 0.01 + 0.1*i)
#     Runge_Kutta('r', fun1, [0, 300], 0.005, 0.00, 0.01 + 0.1*i)
# show()