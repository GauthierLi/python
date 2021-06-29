# learning data must normalization
import numpy as np
import matplotlib.pyplot as plt
import random

random.seed()


# class of queue simple
class Queue():
    def __init__(self, size):
        self.size = size
        self.queue = []

    def enqueue(self, x):
        if len(self.queue) < self.size:
            self.queue.append(x)
        else:
            del self.queue[0]
            self.queue.append(x)


# nerve net of four floor
class NerveNet():

    def __init__(self, form_list):
        self.lenth = len(form_list)
        self.input_matrix = []
        self.output_matrix = []
        self.weight_matrix = []
        self.threshold_matrix = []
        self.error_matrix = []
        for i in range(self.lenth):
            # the input floor
            self.input_matrix.append([0 for j in range(form_list[i])])
            self.output_matrix.append([0 for j in range(form_list[i])])
            self.error_matrix.append([0.1 for j in range(form_list[i])])
            if i == 0:
                self.threshold_matrix.append(np.array([0 for j in range(form_list[i])]))
            else:
                self.threshold_matrix.append(np.array([random.uniform(0, 0.1) for j in range(form_list[i])]))
            if i < len(form_list) - 1:
                self.weight_matrix.append(
                    np.reshape(np.array([random.uniform(0, 0.1) for j in range(form_list[i] * form_list[i + 1])]),
                               [form_list[i], form_list[i + 1]]))

    @staticmethod
    def sigmoid(x):
        # mu is the parametre of sigmoid
        mu = 2
        # define sigmoid function
        return (2 / (1 + np.exp(-2 * x / mu))) - 1

    @staticmethod
    def sigmoid_deriv(x):
        # mu is the parametre of sigmoid
        mu = 2
        return (1 / mu) * (1 + NerveNet.sigmoid(x)) * (1 - NerveNet.sigmoid(x))

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
        for i in range(self.lenth):
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
        return self.output_matrix[self.lenth - 1]

    def learning_once(self, lst, speed=1):
        # learning speed
        alpha = 0.3 * speed
        beta = 0.4 * speed
        q_output = self.data_input(lst[0])

        # calculate the error of floor
        error_index_list = [self.lenth - 1 - i for i in range(self.lenth)]
        for i in error_index_list:
            if i == self.lenth - 1:
                self.error_matrix[i] = -2 * (np.array(lst[1]) - np.array(q_output)) * NerveNet.list_sigmoid_deriv(
                    np.array(self.input_matrix[i]) - np.array(self.threshold_matrix[i]))
            else:
                self.error_matrix[i] = np.dot(np.array(self.error_matrix[i + 1]), self.weight_matrix[i].T) * np.array(
                    NerveNet.list_sigmoid_deriv(np.array(self.input_matrix[i]) - np.array(self.threshold_matrix[i])))

        # change the weight and the threshold
        threshold_index_list = [self.lenth - 2 - i for i in range(self.lenth - 1)]
        for i in threshold_index_list:
            for j in range(len(self.weight_matrix[i])):
                for k in range(len(self.weight_matrix[i][0])):
                    self.weight_matrix[i][j][k] -= alpha * self.error_matrix[i + 1][k] * self.output_matrix[i][j]
            self.threshold_matrix[i + 1] = (self.threshold_matrix[i + 1] + beta * np.array(
                self.error_matrix[i + 1])).tolist()

    def learning_n_times(self, learning_set, expect_error):
        monitor = []
        time = 0
        while np.abs(self.error_matrix[self.lenth - 1][0]) >= expect_error and time < 25000:
            for ele in learning_set:
                time += 1
                self.learning_once(ele)
                monitor.append(self.error_matrix[self.lenth - 1][0])
        return monitor


if __name__ == '__main__':
    # test for nerve net
    a_net = NerveNet([2, 3, 2])
    Y = a_net.learning_n_times([[[0, 0.5], [-1, 0]], [[0.5, 1], [0, 1]], [[0.5, 0], [-1, 0]], [[1, 0.5], [0, 1]]],
                               1e-03)
    X = [i for i in range(len(Y))]
    plt.plot(X, Y)
    plt.show()
    print('test.input_matrix', a_net.input_matrix)
    print('weight_matrix', a_net.weight_matrix)
    print('threshold_matrix', a_net.threshold_matrix)
    print('error_matrix', a_net.error_matrix)
    print(a_net.data_input([0, 0.5]))
    print(a_net.data_input([0.5, 1]))
    print(a_net.data_input([0.5, 0]))
    print(a_net.data_input([1, 0.5]))
