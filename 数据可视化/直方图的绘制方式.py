# demo 1直方图
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# plt.style.use('dark_background')
fig,ax = plt.subplots()
ax.set_title('square numbers')
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y = x*x
plt.bar(x,y)
# 在直方图上显示数字
for a,b in zip(x,y):
    plt.text(a,b+0.2,'%d'%b,ha = 'center', va='bottom',fontsize=16)
plt.show()