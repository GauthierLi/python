'''
import numpy as np

a = np.array([0, 1, 2, 3, 4])
b = np.arange(5)
c = np.linspace(0, 5, 5)
print(a, '\n', b,'\n', c)
a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
print(a[::2, ::2])
print(a[::2, ::2].shape)
a = np.arange(25)
a = a.reshape((5,5))
print(a)
print (b.dot(c))

'''


'''

# Boolean masking
# 布尔屏蔽
import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 2 * np.pi, 50)
b = np.sin(a)
plt.plot(a,b)
mask = b >= 0
plt.plot(a[mask], b[mask], 'bo')
mask = (b >= 0) & (a <= np.pi / 2)
plt.plot(a[mask], b[mask], 'go')
plt.show()

'''

'''
# numpy 求矩阵逆
import numpy as np
a = [[0]*10 for i in range(10)]
for i in range(10):
    for j in range(10):
        a[i][j] = (j+1)**(i+1)
a = np.array(a)
print(a)
print(np.linalg.inv(a))

'''
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3*np.pi, 0.01)
y = np.sin(x)
y1 = np.cos(x)
plt.plot(x,y)
plt.plot(x,y1)
plt.xlabel('value y')
plt.ylabel('value x')
plt.title('x-y relationship')
plt.legend(['sin','cos'])
plt.show()
'''

'''
import numpy as np
a = np.arange(15)**2
i = np.array([0, 1, 3, 5, 6])
print(a[i])

palette = np.array([[0, 0, 0],                # black
                    [255, 0, 0],              # red
                    [0, 255, 0],              # green
                    [0, 0, 255],              # blue
                    [255, 255, 255]])       # white
image = np.array([[0, 1, 2, 0],           # each value corresponds to a color in the palette
                  [0, 3, 4, 0]])
print(palette[image])



from pylab import *

n = 1024
X = [1,2,3,4,5,6]
Y = [7,8,9,9,5,3]

scatter(X,Y)
scatter(Y,X)
show()
'''
'''
import numpy as np
arr1 = np.array([[1, 2, 5], [4, 5, 5]])
print(arr1,  '\t', arr1.sum(0), '\t', arr1.sum(1))
print(arr1.mean(),22/6,arr1.mean(0),arr1.mean(1))
'''
import cv2

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
