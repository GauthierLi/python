# learning data must normalization
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
                q = NerveNet.sigmoid_deriv(self.input_matrix[i][0] - self.threshold_matrix[i][0])
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


if __name__ == '__main__':
    test = NerveNet([2, 1, 1, 1])
    print('test.input_matrix', test.input_matrix)
    print('weight_matrix', test.weight_matrix)
    print('threshold_matrix', test.threshold_matrix)
    print('-----------------after------------------')
    Y = test.learning_n_times([[[1, 1], 1], [[2.8, 4], -1]], 100000)
    Y = Y[400:800]
    X = [i for i in range(len(Y))]
    plt.plot(X, Y)
    plt.show()
    print('test.input_matrix', test.input_matrix)
    print('weight_matrix', test.weight_matrix)
    print('threshold_matrix', test.threshold_matrix)
    print(test.error_matrix)
    print(test.data_input([1, 1]))
    print(test.data_input([2.8, 4]))

