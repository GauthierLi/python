# note：在选择区间时候尽可能大的选择区间，
# 将可能最优值包含进去，同事最高温度一般设置最好不要超过1，这样依概率的时候才不会太活泼


import random
import numpy


# 用类定义循环队列
class que():

    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, x):
        if len(self.queue) < self.size:
            self.queue.append(x)
        else:
            del self.queue[0]
            self.queue.append(x)

    def dequeue(self):
        del self.queue[0]


def f(x):
    # 定义优化函数f,f在-27处取得全局最优-67243.25
    q = 1 / 4 * x ** 4 + 19 / 3 * x ** 3 - 225 / 2 * x ** 2 - 243 * x + 7
    # q = x ** 2 + 50 * x + 625
    return q


# 定义概率触发器
def Probablity_trigger(p):
    a = random.random()
    if a <= p:
        return 1
    else:
        return 0


# 定义概率函数
def Probablity(q, x, T):
    if f(q) < f(x):
        return 1
    else:
        return numpy.exp(((f(x) - f(q)) / T))


# 定义邻域Epsilon
Epsilon = 50
# 初始化数组x
x = que(2)
x.enqueue(0)
x.enqueue(255)
# 初始化温度
T = 25
# 设置低温T_min
T_min = 0.0000003

while T > T_min:
    # 初始化队列，连续15次没有发生变化的时候终止循环
    Que = que(15)
    # 初始化指针
    i = 0
    while True:
        i += 1
        # 先判断
        if Que.queue == [0] * 15 or i > 10240:
            break
        random.seed()
        # 取随机数
        random_q = random.uniform(-1, 1)
        # 得到新值X[i+1]的搬运工小q
        q = x.queue[1] + random_q * Epsilon
        # 判断新值是否被接受
        p = Probablity(q, x.queue[1], T)
        print(p)
        if Probablity_trigger(p) != 0:
            # 开始计数,利用循环队列计数
            Que.enqueue(1)
            x.enqueue(q)
            print(Que.queue, '\n', x.queue, '\n', T)
        else:
            Que.enqueue(0)
            print(Que.queue, '\n', x.queue, '\n', T)
            continue

    # 退火降温
    T = 0.999 * T

print('全局最优点取值于', x.queue[1])
