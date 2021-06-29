import numpy as np
from pylab import *
from full_events_analysing import X_win, Y_win, X_tie, Y_tie, X_loss, Y_loss


def least_square(X, Y, color):
    scatter(X, Y, c=color, marker='.')
    R_trans = np.array([[1] * len(X), [i_1 for i_1 in X]])
    R = np.transpose(R_trans)
    A = np.matmul(np.linalg.inv(np.matmul(R_trans, R)), np.matmul(R_trans, Y))
    Y_1 = []
    for i in np.arange(-0.3, 0.5, 0.001):
        q_0 = np.transpose(np.array([1, i]))
        q_1 = np.matmul(A, q_0)
        Y_1.append(q_1)
    Xn1 = np.arange(-0.3, 0.5, 0.001)
    scatter(Xn1, Y_1, s=0.1)
    xlabel('press')
    ylabel('foal_rate')
    show()
    return A


print(least_square(X_win, Y_win, 'blue'))
print(least_square(X_tie, Y_tie, 'green'))
print(least_square(X_loss, Y_loss, 'red'))
