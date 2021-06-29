from sympy import *
# KTT算法一般式
# 设置变量
I_min = 34180.22846955232
P_max = 100000
k = 276893.8503279474
e = symbols('e')
h = symbols('h')
b = symbols('b')
alpha1 = symbols('alpha1')
alpha2 = symbols('alpha2')
alpha3 = symbols('alpha3')
alpha4 = symbols('alpha4')
alpha5 = symbols('alpha5')
# 构造拉格朗日等式
Lagrange = e*h + 2*e*b + alpha1*((I_min - e*h**3)/12-(e*b*h**2)/2) + alpha2*(P_max/(e*h+2*e*b)-k*(e/h)**2)-e*alpha3-h*alpha4-b*alpha5
# 构造KTT条件
dife = diff(Lagrange,e)
difh = diff(Lagrange,h)
difb = diff(Lagrange,b)
difalpha1 = diff(Lagrange,alpha1)
difalpha2 = diff(Lagrange,alpha2)
difalpha3 = diff(Lagrange,alpha3)
difalpha4 = diff(Lagrange,alpha4)
difalpha5 = diff(Lagrange,alpha5)
print([dife,difh,difb,difalpha1,difalpha2,difalpha3,difalpha4,difalpha5])
solution = solve([dife,difh,difb,difalpha1,difalpha2,difalpha3,difalpha4,difalpha5],[e,h,b,alpha1,alpha2,alpha3,alpha4,alpha5])
print(solution)
