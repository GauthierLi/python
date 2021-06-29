import sympy

# 定义目标函数
# 定义变量
x = sympy.Symbol('x')
J_x = x ** 2 - 14 * x + 17

# 定义步长列表
h = []
h_current = sympy.Symbol('h_current')
# 定义点列
x_n = [1 * 10 ** (-6)]
#  求梯度
j_x = sympy.diff(J_x, x)
print(j_x.evalf(subs={x: 8}))
i = 0
while j_x.evalf(subs={x: x_n[i]}) < 0.000001:
    # 错误：evalf方法不能传递参数，只能传递数值
    v = x_n[i] - h_current * j_x.evalf(subs={x: x_n[i]})
    u = j_x.evalf(subs={x: x_n[i]})
    y = j_x.evalf(subs={x: v}) * u
    # 错误：evalf方法不能传递参数，只能传递数值
    w = sympy.solve(y, h_current)
    h.append(w[0])
    i = i + 1
    x_current = x_n[i - 1] + u * h[i - 1]
    x_n.append(x_current)
print(x_n)
