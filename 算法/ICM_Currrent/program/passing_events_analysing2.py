# from passing_events_analysing1 ,we can get our training set winner_learning_data + losser_learning_data
from passing_events_analysing1 import winner_learning_data_rate, losser_learning_data_rate, \
    learning_set_rate_after_normalization, mean_list, derta_list, winner_learning_data, losser_learning_data
import pandas as pd
import random


random.seed()

matches_data = pd.read_csv(open('matches.csv'))
# # now we define a new teacher signal's weigth
# teacher_signal_weight = []
# print(matches_data[:3])
# for i in range(38):
#     q = matches_data[i:i + 1]
#     if q['OwnScore'][i] + q['OpponentScore'][i] != 0:
#         q_num = abs(q['OwnScore'][i] - q['OpponentScore'][i]) / (q['OwnScore'][i] + q['OpponentScore'][i])
#     else:
#         q_num = 0
#     teacher_signal_weight.append(q_num)
# print(teacher_signal_weight)
# for i in range(38):
#     winner_learning_data[i][1] = winner_learning_data[i][1] * teacher_signal_weight[i]
#     losser_learning_data[i][1] = losser_learning_data[i][1] * teacher_signal_weight[i]
#
#
# # define a functioin to plot each element's distribution
# def ele_point_plot(list_for_learning, num):
#     x_set = []
#     y_set = []
#     for ele in list_for_learning:
#         x_set.append(ele[0][num])
#         y_set.append(ele[1])
#     plt.plot(x_set, y_set, 'd')
#     plt.xlabel(num, fontsize=14)
#     plt.ylabel('win or loss', fontsize=14)
#
#
# for i in range(11):
#     ele_point_plot(winner_learning_data, i)
#     ele_point_plot(losser_learning_data, i)
#     plt.show()
#

# --------------------------------------nerve_net_work------------------------------------------------------------------
# nerve net of four floor
import numpy as np
import random
import matplotlib.pyplot as plt

random.seed()


# nerve net of four floor
class NerveNet():
    def __init__(self, form_list):
        self.input_matrix = []
        self.output_matrix = []
        self.weight_matrix = []
        self.threshold_matrix = []
        self.error_matrix = []
        for i in range(len(form_list)):
            # the input floor
            self.input_matrix.append([0 for j in range(form_list[i])])
            self.output_matrix.append([0 for j in range(form_list[i])])
            self.error_matrix.append([0 for j in range(form_list[i])])
            if i == 0:
                self.threshold_matrix.append([0 for j in range(form_list[0])])
            else:
                self.threshold_matrix.append([random.uniform(0, 0.1) for j in range(form_list[i])])
            if i < len(form_list) - 1:
                self.weight_matrix.append(
                    np.reshape(np.array([random.uniform(0, 0.1) for j in range(form_list[i] * form_list[i + 1])]),
                               [form_list[i], form_list[i + 1]]))

    @staticmethod
    def sigmoid(x):
        # define sigmoid function
        return (2 / (1 + np.exp(-x))) - 1

    @staticmethod
    def sigmoid_deriv(x):
        return 0.5 * (1 + NerveNet.sigmoid(x)) * (1 - NerveNet.sigmoid(x))

    @staticmethod
    def list_sigmoid(lst):
        q = []
        for ele in lst:
            q.append(NerveNet.sigmoid(ele))
        return q

    @staticmethod
    def list_sigmoid_deriv(lst):
        q = []
        for ele in lst:
            q.append(NerveNet.sigmoid_deriv(ele))
        return q

    def data_input(self, lst):
        for i in range(4):
            if i == 0:
                # calculate the input of input_floor
                self.input_matrix[0] = np.array(lst)
                # calculate the output of input_floor (have not any change)
                self.output_matrix[0] = self.input_matrix[0].tolist()
            else:
                # calculate the input of the first hide floor
                q = np.dot(np.array(self.output_matrix[i - 1]), np.array(self.weight_matrix[i - 1]))
                self.input_matrix[i] = q
                # calculate the output of the first hide floor
                q1 = NerveNet.list_sigmoid(np.array(self.input_matrix[i]) - np.array(self.threshold_matrix[i]))
                self.output_matrix[i] = q1
        return self.output_matrix[3]

    def learning_once(self, lst, speed=1):
        # learning speed
        alpha = 0.3 * speed
        beta = 0.4 * speed
        q_output = self.data_input(lst[0])

        # calculate the error of floor
        for i in [3, 2, 1, 0]:
            if i == 3:
                self.error_matrix[i] = [-2 * (lst[1] - q_output[0]) * NerveNet.sigmoid_deriv(self.input_matrix[i][0] -
                                                                                             self.threshold_matrix[i][
                                                                                                 0])]
            else:
                self.error_matrix[i] = np.dot(np.array(self.error_matrix[i + 1]), self.weight_matrix[i].T) * np.array(
                    NerveNet.list_sigmoid_deriv(np.array(self.input_matrix[i]) - np.array(self.threshold_matrix[i])))

        # change the weight and the threshold
        for i in [2, 1, 0]:
            for j in range(len(self.weight_matrix[i])):
                for k in range(len(self.weight_matrix[i][0])):
                    self.weight_matrix[i][j][k] -= alpha * self.error_matrix[i + 1][k] * self.output_matrix[i][j]
            self.threshold_matrix[i + 1] = (np.array(self.threshold_matrix[i + 1]) + beta * np.array(
                self.error_matrix[i + 1])).tolist()

    def learning_n_times(self, learning_set, n):
        monitor = []
        time = 0
        while time < n:
            for ele in learning_set:
                time += 1
                self.learning_once(ele)
                monitor.append(self.threshold_matrix[2][0])
        return monitor


win_net = NerveNet([11, 14, 14, 1])
Y = win_net.learning_n_times(learning_set_rate_after_normalization, 27000)
X = [i for i in range(len(Y))]
plt.plot(X, Y)
plt.show()
for i in range(38):
    print(learning_set_rate_after_normalization[i][1], ',',
          win_net.data_input(learning_set_rate_after_normalization[i][0])[0])


def my_model(lst):
    return win_net.data_input(lst)[0]


# get the list of the optimal data which is after normalization
factor_to_win = []
for i in range(11):
    set = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    set[i] = 1
    factor_to_win.append(my_model(set))
print(factor_to_win)
# result
factor_to_win = [-0.5801078679636702, -0.98495943748985304, 0.97881415897561874, -0.99880078824552943,
                 -0.33291779264271792, -0.68276448946141344, -0.97073702488308466, -0.69908097906941058,
                 -0.98332037234977021, -0.029094574401479223, -0.75407110071245342]
print('\n', win_net.data_input(
    [-0.5801078679636702, -0.98495943748985304, 0.97881415897561874, -0.99880078824552943, -0.33291779264271792,
     -0.68276448946141344, -0.97073702488308466, -0.69908097906941058, -0.98332037234977021, -0.029094574401479223,
     -0.75407110071245342]
))

# anti_normalization
final_win_factor_list = []
for i in range(11):
    q = factor_to_win[i] * derta_list[i] + mean_list[i]
    final_win_factor_list.append(q)
print(final_win_factor_list)
# result
final_win_factor_list = [129.0776809068127, 77.9958890234888, 5314.844617894659, 1868.8745314494613, 13.726945784017213,
                         186.53819822598442, 0.9711863561572205, 10.432631199340484, 1.14508868180727,
                         2.4371190073318174, 1.7708923457618795]
# normalizaton
initial_data = [129, 78, 5315, 1869, 13, 187, 1, 10, 1, 2, 2]
after_normalizaton = []
for i in range(11):
    q = (initial_data[i] - mean_list[i]) / derta_list[i]
    after_normalizaton.append(q)
print(after_normalizaton)
print('Huskies_average_win_rate', win_net.data_input(after_normalizaton))
print(win_net.data_input([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
