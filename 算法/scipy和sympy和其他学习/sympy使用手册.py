# coding:utf-8
from sympy import *

# #---------------------------------------------------多项式求解--------------------------------------------------------
# # 定义变量
# x = symbols('x')
# y = symbols('y')
# fx = 5*x + 4
# # 使用sympy中的evalf函数传值
# y1 = fx.evalf(subs={x:6})
# print(y1)


# #--------------------------------------------------函数方程求解-------------------------------------------------------
# #求解方程，只能求解基本有解方程
# #解方程 有限解
# #定义变量
# x = Symbol('x')
# fx = x**2 + 2*x + 1
# #可求解直接给出解向量
# print(solve(fx, x))


# # 解方程无穷多解
# # 定义变量
# x = Symbol('x')
# y = Symbol('y')
# fx = x * 3 + y ** 2
# # 得到是x与y的关系式，
# print(solve(fx, x, y))
#
#
# #解方程组
# #定义变量
# x = Symbol('x')
# y = Symbol('y')
# f1 = x + y - 3
# f2 = x - y + 5
# #求解方程组
# print(solve([f1, f2], [x, y]))


# #---------------------------------------------------------求和--------------------------------------------------------
# #定义变量
#
# n = Symbol('n')
# f = 2*n
# #前面参数放函数，后面放变量的变化范围
# s = summation(f,(n,1,100))
# print(s)
#
#
# #--------------------------------------------------------求极限-------------------------------------------------------
# # 注意，math包中sin和很多数学函数会报错，要用sympy中的，无穷大用 sympy.oo 表示
# #求极限使用limit方法
# #定义变量与函数
# x = Symbol('x')
# f1 = sin(x)/x
# f2 = (1 + x)**(1/x)
# f3 = (1 + 1/x)**x
# #三个参数是 函数，变量，趋向值
# lim1 = limit(f1, x, 0)
# lim2 = limit(f2, x, 0)
# lim3 = limit(f3, x, oo)
# print(lim1, lim2, lim3)


# #-----------------------------------------------------求导------------------------------------------------------------
# # 求导使用diff方法
# x = Symbol('x')
# f1 = 2 * x ** 4 + 3 * x + 6
# # 参数是函数与变量
# f1_ = diff(f1, x)
# print(f1_)
# f2 = sin(x)
# f2_ = diff(f2, x)
# print(f2_)
# # 求偏导
# y = Symbol('y')
# f3 = 2 * x ** 2 + 3 * y ** 4 + 2 * y
# # 对x，y分别求导，即偏导
# f3_x = diff(f3, x)
# f3_y = diff(f3, y)
# print(f3_x)
# print(f3_y)


# #-----------------------------------------------求积分----------------------------------------------------------------
# #求定积分用 integrate方法
# x = Symbol('x')
# f = 2*x
# #参数传入 函数，积分变量和范围
# result = integrate(f,(x,0,1))
# print(result)
# # 上面的求法有点烂，难的就罢工不干了。scipy 能解决很多数值计算，包括多重积分。
#
# #求多重积分，先求里面的积分，再求外面的
# x,t = symbols('x t')
# f1 = 2*t
# f2 = integrate(f1,(t,0,x))
# result = integrate(f2,(x,0,3))
# print(result)
#
# #求不定积分其实和定积分区别不大
# x = Symbol('x')
# f = (E**x+2*x)
# f_ = integrate(f,x)
# print(f_)
#

# ----------------------------------------------------数学符合---------------------------------------------------------
# # 虚数单位i
# sympy.I
#
# # 自然对数低e
# sympy.E
#
# # 无穷大
# sympy.oo
#
# # 圆周率
# sympy.pi
#
# # 求n次方根
# sympy.root(8, 3)
#
# # 求对数
# sympy.log(1024, 2)
#
# # 求阶乘
# sympy.factorial(4)
#
# # 三角函数
# sympy.sin(sympy.pi)
# sympy.tan(sympy.pi / 4)
# sympy.cos(sympy.pi / 2)

# #---------------------------------------------向下取整，向上取整，四舍五入----------------------------------------------
# import math
#
# # 向上取整
# print("math.ceil---")
# print("math.ceil(2.3) => ", math.ceil(2.3))
# print("math.ceil(2.6) => ", math.ceil(2.6))
#
# # 向下取整
# print("\nmath.floor---")
# print("math.floor(2.3) => ", math.floor(2.3))
# print("math.floor(2.6) => ", math.floor(2.6))
#
# # 四舍五入
# print("\nround---")
# print("round(2.3) => ", round(2.3))
# print("round(2.6) => ", round(2.6))
#
# # 这三个的返回结果都是浮点型
# print("\n\nNOTE:every result is type of float")
# print("math.ceil(2) => ", math.ceil(2))
# print("math.floor(2) => ", math.floor(2))
# print("round(2) => ", round(2))
