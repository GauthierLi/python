import numpy as np
from pylab import *
from passing_events_analysing1 import pass_time_learning_set, pass_distance_learning_set
# 1H传球距离
X = []
Y = []
for ele in pass_distance_learning_set:
    if ele[1] == 1:
        X.append(ele[0][0])
        Y.append(ele[0][1])
X = np.array(X)
Y = np.array(Y)
scatter(X, Y)

R_trans = np.array([[1 for i in X], [i_1 for i_1 in X]])
R = R_trans.T
A = np.matmul(np.linalg.inv(np.matmul(R_trans,R)), np.matmul(R_trans, Y))
Y_1 = []
for i in np.arange(0, 8000, 0.03):
    q_0 = np.transpose(np.array([1, i]))
    q_1 = np.matmul(A, q_0)
    Y_1.append(q_1)
Xn1 = np.arange(0, 8000, 0.03)
scatter(Xn1, Y_1, s=0.1)
xlabel('pass distance in 1H for winner')
ylabel('pass distance in 2H for winner')
show()
print(A)