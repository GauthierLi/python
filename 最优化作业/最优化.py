import numpy as np
import matplotlib.pyplot as plt

L = 503
E = 75000
mu = 0.33
k = 4*E*np.pi**2/(12*(1 - mu**2))
P_max = 10**5
I_min = P_max*L**2/(E*np.pi**2)
alpha = (3*P_max**2/(32*I_min*k**2))**(1/5)
e = (6*alpha**3*I_min)**0.25
h = e/alpha
b = h*1/6
s = P_max/(k*alpha**2)
print(e,h,b,k)

# 定义函数
def L(P_max):
    L = 503
    E = 75000
    mu = 0.33
    k = 4 * E * np.pi ** 2 / (12 * (1 - mu ** 2))
    I_min = P_max * L ** 2 / (E * np.pi ** 2)
    alpha = (3 * P_max ** 2 / (32 * I_min * k ** 2)) ** (1 / 5)
    e = (6 * alpha ** 3 * I_min) ** 0.25
    h = e / alpha
    b = h * 1 / 6
    s = P_max / (k * alpha ** 2)
    return [P_max, I_min, alpha, e, h, b, s]
print(L(10**5))

L_matrix=[]
for i in range(10**5, 10*10**5, 10**5):
    L_matrix.append(L(i))
print(L_matrix)


e_vector = []
h_vector = []
b_vector = []
s_vector = []
P_max_vector = []
for i in range(9):
    P_max_vector.append(L_matrix[i][0]/10**5)
    e_vector.append(L_matrix[i][3])
    h_vector.append(L_matrix[i][4])
    b_vector.append(L_matrix[i][5])
    s_vector.append(L_matrix[i][6])

plt.figure(num='min')

# 画出e-P_max图像
plt.subplot(2,2,1)
plt.plot(P_max_vector,e_vector)
plt.xlabel('P_max /10^5', fontsize = 14)
plt.ylabel('e', fontsize = 14)


# 画出h-P_max图像
plt.subplot(2,2,2)
plt.plot(P_max_vector,h_vector)
plt.xlabel('P_max/10^5', fontsize = 14)
plt.ylabel('h', fontsize = 14)


# 画出b-P_max图像
plt.subplot(2,2,3)
plt.plot(P_max_vector,b_vector)
plt.xlabel('P_max/10^5', fontsize = 14)
plt.ylabel('b', fontsize = 14)


# 画出s-P_max图像
plt.subplot(2,2,4)
plt.plot(P_max_vector,s_vector)
plt.xlabel('P_max/10^5', fontsize = 14)
plt.ylabel('s', fontsize = 14)
plt.show()

plt.show()

