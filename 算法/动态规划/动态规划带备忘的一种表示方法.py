import math


def MEMOIRIZED_CUT_ROD(p, n):
    r = [0] * (n + 1)
    for i in range(n + 1):
        r[i] = -math.inf
        # 初始记忆数组
    return MEMOIRIZED_CUT_ROD_AUX(p, n, r)


def MEMOIRIZED_CUT_ROD_AUX(p, n, r):
    # 定义有记忆切割算法
    if r[n] >= 0:
        # 寻找记忆是否存在，若存在则直接读取记忆
        return r[n]
    if n == 0:
        q = 0
        # 递归终点
    else:
        q = -math.inf
        # 初始化搬运工
        for i in range(n):
            if i <= 9:
                q = MAX(q, p[i] + MEMOIRIZED_CUT_ROD_AUX(p, n - i - 1, r))
    r[n] = q
    return q


def MAX(a, b):
    # 定义取最大函数
    if a > b:
        return a
    else:
        return b

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
for i in range(40):
    print('切割长度为{}的铁棒收益为{}'.format(i+1 , MEMOIRIZED_CUT_ROD(p, i+1)))
