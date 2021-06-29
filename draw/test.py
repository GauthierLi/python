import matplotlib.pyplot as plt
import numpy as np

X = [3030,3050,3080,4010,4100,4200,5100,5200,5280,5300]
X_1 = [5.60,5.64,5.90,7.00,7.14,7.20,7.35,8.50,8.60,8.64]
X_2 = [3640,3760,3620,4570,4600,4750,7900,5450,5530,6200]

Y = [3000,3020,3050,4010,4030,4050,5030,5070,5300,5330]
Y_1 = [5.64,5.72,5.98,7.00,7.36,7.04,8.34,8.76,9.00,9.10]
Y_2 = [3590, 3710,3760,4670,4760,4860,6210,6470,6520,6590]

fig = plt.figure(figsize=(10,7))
ax1 = fig.add_subplot(111)
line1 ,= ax1.plot(X, X_1, c = 'b',marker='o')
line2 ,= ax1.plot(Y, Y_1,c = '#22958A',marker='x')
plt.tick_params(labelsize=23)
ax1.set_ylabel('Volume Flow/ L.min^-1',fontdict={'weight':'normal', 'size':23})
ax1.set_xlabel('rotation /rpm',fontdict={'weight':'normal', 'size':23})


ax2 = ax1.twinx()

line3 ,= ax2.plot(X, X_2, c = 'r',marker='o')
line4 ,= ax2.plot(Y, Y_2,c = '#951594',marker='x')
plt.tick_params(labelsize=23)
ax2.set_ylabel('Pressure Difference /Pa',fontdict={'weight':'normal', 'size':23})
ax2.set_xlabel('333',fontdict={'weight':'normal', 'size':23})
ax1.set_xticklabels(X,rotation=0,fontdict={'weight':'normal', 'size':23})
plt.legend((line1, line2, line3, line4), ('VF of water','VF of 0.06% xanthan gum(aq)','PD of water','PD of 0.06% xanthan gum(aq)'), loc='upper left',fontsize=23)
plt.show()