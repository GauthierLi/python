# coding: utf-8
# 自顶向下的算法
# 效率比较低，反复调用函数计算已计算过的值，每增长一英尺，算法所用的时间就会增长几乎一倍，时间复杂度为2^n
import math
from numba import jit,njit
# GPU加速模块

@njit
def CUT_ROD(p, n):
    # 定义最大价值函数
    if n == 0:
        return 0
    else:
        q = -math.inf
        # 定义搬运工小人
        for i in range(n):
            if i <= 9:
                q = MAX(q, p[i] + CUT_ROD(p, n - i - 1))
                # 比较钻石大小
                # 使用了分治思想，切成左右两块，左边不再切割，取右边的最优值
        return q

@jit
def MAX(a, b):
    # 定义取最大函数
    if a > b:
        return a
    else:
        return b


p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
for i in range(26):
    print('切割长度为{}的铁棒最佳收益为{}'.format(i+1, CUT_ROD(p, i + 1)))
