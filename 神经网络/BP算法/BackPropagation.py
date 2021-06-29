# coding:utf-8
import numpy as np
import random


def sigmoid(x):
    # 定义sigmoid函数
    q = 1 / (1 + np.exp(-x / 2))
    return q


def error_fonction(list1, list2):
    sum = 0
    if len(list1) != len(list2):
        raise print('错误！向量维度不同')
    else:
        q_list = np.array(list1) - np.array(list2)
        for i in q_list:
            sum += i ** 2
        return np.sqrt(sum)


class NerveCell:
    # 定义神经元类

    def __init__(self, input_list=None):
        """
        :param input_list: 作为神经元的初始化输入列表，此操作可以确定这个神经元的突触数目
        """
        random.seed()
        if input_list is None:
            input_list = []
        self.input_list = input_list
        # 定义突触数目(确定后不再随意变动)
        self.synapse_num = len(self.input_list)
        # 初始化突触权重(随学习改动)
        self.weight_arr = np.array([1 for i in range(self.synapse_num)], dtype=np.float)
        # 定义net_ij(做运算，需要更新)
        self.net = np.dot(np.array(self.input_list), self.weight_arr)
        # 初始化阈值(随学习改动)
        self.threshold = 0.00001
        # 定义神经元的输出Y(做运算，需要更新)
        self.output = sigmoid(self.net - self.threshold)
        '''
        example:
            a_list_of_nerve = []
            for i in range(3):
                a_list_of_nerve.append(Nerve_cell([0]))
            print(a_list_of_nerve)
        '''

    def input(self, input_list):
        self.input_list = input_list
        self.update()

    def update(self):
        self.net = np.dot(np.array(self.input_list), self.weight_arr)
        self.output = sigmoid(self.net - self.threshold)

    # 检查神经元各个参数是否出错
    def check(self):
        self.update()
        net_0 = np.dot(self.weight_arr, np.array(self.input_list))
        if net_0 - self.net > 0.001 or sigmoid(net_0 - self.threshold) - self.output > 0.001:
            return False
        else:
            return True

    def print_para(self):
        print('突触数目：    {}'.format(self.synapse_num))
        print('突触权重：    {}'.format(self.weight_arr))
        print('神经元阈值：  {}'.format(self.threshold))
        print('神经元的输入：{}'.format(self.input_list))
        print('神经元的net:  {}'.format(self.net))
        print('神经元的输出：{}'.format(self.output))
        print('\n', '\n')


class NerveNet:
    # 定义神经网络类

    def __init__(self, floor, num_of_each_floor_list):
        # 定义神经网络层数
        self.floor = floor
        # 定义神经网络每层的神经元个数
        self.num_of_each_floor_list = num_of_each_floor_list
        # 开辟初始矩阵空间存放神经元
        self.matrix_of_nerve_cell = []
        # 开辟初始矩阵空间存放节点误差
        self.matrix_of_node_error = []
        print('-------------------神经网络初始化---------------------')
        if floor != len(num_of_each_floor_list):
            print('警告！初始化失败，检查网络层数与神经元数目列表')
        else:
            print('{}层神经网络，隐层数{}'.format(self.floor, self.floor - 2))

    def creat(self):
        print('-----------------神经网络搭建开始---------------------')
        self.matrix_of_nerve_cell = [[] for i in range(self.floor)]
        for i_0 in range(self.floor):
            print('第{}层神经网络构建中'.format(i_0 + 1))
            for j in range(self.num_of_each_floor_list[i_0]):
                if i_0 == 0:
                    self.matrix_of_nerve_cell[i_0].append(NerveCell([1]))
                    self.matrix_of_nerve_cell[i_0][j].threshold = 0
                    self.matrix_of_nerve_cell[i_0][j].update()
                else:
                    self.matrix_of_nerve_cell[i_0].append(
                        NerveCell([j.output for j in self.matrix_of_nerve_cell[i_0 - 1]]))
        print('-----------------神经网络搭建结束---------------------')

    def input_and_calacule(self, list_of_input):
        """
        fonction: 用于计算神经网络计算，属于操作，没有输出结果
        :param list_of_input: 神经网络的输入
        """
        for i in range(len(list_of_input)):
            self.matrix_of_nerve_cell[0][i].input([list_of_input[i]])
            self.matrix_of_nerve_cell[0][i].update()

    # 稍后把此方法放到最后
    def output_of_nerve_net(self, list_of_input):
        """
        foncton: 计算神经网络的输出
        :param list_of_input: 神经网络的输入
        :return: 输出神经网络的结果
        """
        self.input_and_calacule(list_of_input)
        q = []
        for j in range(self.num_of_each_floor_list[-1]):
            q.append(self.matrix_of_nerve_cell[self.floor - 1][j].output)
        return q

    def one_times_learning(self, list_of_learning, study_vilocity=0.05):
        """
        fonction: 学习并且修改对应的权值
        :param list_of_learning: 学习列表，其格式应该为[ [[学习参数1]，[教师信号1]], [[学习参数2]，[教师信号2]], ...[[学习参n]，[教师信号n]] ]
        :param study_vilocity: 学习速率
        :return:
        """

        self.matrix_of_node_error = [[] for i in range((self.floor - 1))]
        # 初始化误差矩阵
        the_error_of_this_turn = 0
        # 定义单轮的误差
        for ele in list_of_learning:
            # 向前学习并且记录输出值
            output_list = self.output_of_nerve_net(ele[0])
            # 开始计算误差
            the_error_of_this_turn += error_fonction(ele[1], output_list)
            # 开始计算节点误差
            range_list = [i_0 for i_0 in range(self.floor - 1)]
            range_list.reverse()
            # 定义上一层对该节点的层权列表
            weight_list = [[] for i_1 in range((self.floor - 1))]
            for i_2 in range_list:
                # 倒序计算(第i层)的误差
                if i_2 == self.floor - 2:
                    for j in range(self.num_of_each_floor_list[i_2 + 1]):
                        # 计算输出层节点误差
                        q = -(ele[1][j] - output_list[j]) * output_list[j] * (1 - output_list[j])
                        self.matrix_of_node_error[i_2].append(q)
                        print(q)
                        # 更新权值
                        # 简写差异列表
                        error_list_in_simple = np.array(
                            [self.matrix_of_nerve_cell[i_2][k_0].output for k_0 in
                             range(self.num_of_each_floor_list[i_2])])
                        error_list_in_simple = study_vilocity * q * error_list_in_simple
                        self.matrix_of_nerve_cell[i_2 + 1][j].weight_arr -= error_list_in_simple
                        # 更新阈值
                        self.matrix_of_nerve_cell[i_2 + 1][j].threshold += study_vilocity * q
                        self.matrix_of_nerve_cell[i_2 + 1][j].update()
                else:
                    # 计算第i层的第j个神经元节点误差
                    for j in range(self.num_of_each_floor_list[i_2 + 1]):
                        weight_list[i_2] = np.array([self.matrix_of_nerve_cell[i_2 + 2][k].weight_arr[j] for k in
                                                     range(self.num_of_each_floor_list[i_2 + 2])])
                        array_q = np.array(self.matrix_of_node_error[i_2 + 1])
                        weight_sum = np.dot(weight_list[i_2], array_q)
                        # 简写隐层节点输出
                        output_q = self.matrix_of_nerve_cell[i_2][j].output
                        # 计算隐层节点误差
                        q = output_q * (1 - output_q) * weight_sum
                        self.matrix_of_node_error[i_2].append(q)
                        # 更新权值
                        # 简写差异列表
                        error_list_in_simple = np.array(
                            [self.matrix_of_nerve_cell[i_2][k_0].output for k_0 in
                             range(self.num_of_each_floor_list[i_2])])
                        error_list_in_simple = study_vilocity * q * error_list_in_simple
                        self.matrix_of_nerve_cell[i_2 + 1][j].weight_arr -= error_list_in_simple
                        # 更新阈值
                        self.matrix_of_nerve_cell[i_2 + 1][j].threshold += study_vilocity * q
                        self.matrix_of_nerve_cell[i_2 + 1][j].update()
        print('已学习{}次'.format(len(list_of_learning)))
        print('-----------------本轮学习结束---------------------')
        return the_error_of_this_turn


if __name__ == '__main__':
    a = NerveNet(2, [2, 1])
    teacher_list = np.array([[[0.5, 0.05], [1.0]], [[0.05, 0.5], [1.0]], [[0.95, 0.5], [0.0]], [[0.5, 0.95], [0.0]]])
    a.creat()
    epsilon = 0.05
    b = 100
    i = 0
    while b > epsilon and i < 10000:
        i += 1
        b = a.one_times_learning(teacher_list, study_vilocity=0.4)
        a.matrix_of_nerve_cell[1][0].print_para()
    print(a.output_of_nerve_net([0.95, 0.5]))
    print(b, i)
