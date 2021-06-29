from pylab import *

def least_square(X, Y, arange_step_list,label_list, color='green'):
    scatter(X, Y, c=color, marker='.')
    R_trans = np.array([[1] * len(X), [i_1 for i_1 in X]])
    R = np.transpose(R_trans)
    A = np.matmul(np.linalg.inv(np.matmul(R_trans, R)), np.matmul(R_trans, Y))
    Y_1 = []
    for i in np.arange(arange_step_list[0], arange_step_list[1], arange_step_list[2]):
        q_0 = np.transpose(np.array([1, i]))
        q_1 = np.matmul(A, q_0)
        Y_1.append(q_1)
    Xn1 = np.arange(arange_step_list[0], arange_step_list[1], arange_step_list[2])
    scatter(Xn1, Y_1, s=0.1)
    xlabel(label_list[0])
    ylabel(label_list[1])
    show()
    return A

# example: least_squres.least_square(list_of_open, list_of_close, [13, 18, 0.02],['close','open'])
