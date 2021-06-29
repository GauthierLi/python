import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
x = np.arange(-3.5, 3.5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)
z = 3.5 ** 2 - x ** 2 - (0.7 * y) ** 2
ax.plot_surface(x, y, z, rstride=1, cstride=1)
ax.contourf(x, y, z, zdir='z', offset=-2)
plt.savefig('pic.png',bbox_inches='tight')
