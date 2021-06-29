import numpy as np
from pylab import *

X = np.array([i + 1 for i in range(11)])
truncation_error = [-42.074025662697778, 69.591352494981379, 25.434883495707936, 35.215556550669646, 117.65542532993686, -2.0377568376106865, -51.866368092253538, -38.556505596657189, -35.783374265615748, -306.44224811423692, -184.95477739503804]
Y = np.array(truncation_error)
scatter(X, Y)


R_trans = np.array([[1]*11, [i_1 for i_1 in X], [i_2**2 for i_2 in X], [i_3**3 for i_3 in X], [i_4**4 for i_4 in X], [i_5**5 for i_5 in X], [i_6**6 for i_6 in X]])
R = np.transpose(R_trans)
A = np.matmul(np.linalg.inv(np.matmul(R_trans,R)), np.matmul(R_trans, Y))
Y_1 = []
for i in np.arange(0, 12, 0.03):
    q_0 = np.transpose(np.array([1, i , i**2, i**3, i**4, i**5, i**6]))
    q_1 = np.matmul(A, q_0)
    Y_1.append(q_1)
Xn1 = np.arange(0, 12, 0.03)
scatter(Xn1, Y_1, s=0.1)
xlabel('day^th')
ylabel('number')
show()
