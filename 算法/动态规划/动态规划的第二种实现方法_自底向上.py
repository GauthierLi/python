import math


def BOTTOM_UP_CUT_ROD(p, n):
    # 自下而上的切割方法

    r = [0] * (n + 1)
    slice = [0] * n
    # 记录每次拟切割位置，最后一个数据为最优切割位置
    for j in range(n):
        q = -math.inf
        # 初始化搬运工
        for i in range(j + 1):
            if i > 9:
                continue
            else:
                if q < (p[i] + r[j - i]):
                    q = p[i] + r[j - i]
                    slice[j] = i + 1
                    # 记录每次切割
        r[j + 1] = q
        # 搬运最大的钻石
    return [r[n], slice[n - 1]]


def MAX(a, b):
    # 定义取最大函数
    if a > b:
        return a
    else:
        return b


p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
for i in range(40):
    print('切割长度为{}的铁棒收益为{},在{}英尺处切割'.format(i + 1, BOTTOM_UP_CUT_ROD(p, i + 1)[0], BOTTOM_UP_CUT_ROD(p, i + 1)[1]))
