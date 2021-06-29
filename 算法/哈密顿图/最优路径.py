import random
import numpy

'''
问题描述
                      哈密顿图问题
从A到K，11个地点，任意两地之间的距离如下给定，求从A点出发，回到A点，要求所有地点都要去到，并且没有重复的最短路径。

{'A','B',324},{'A','C',556},{'A','D',241},{'A','F',703},{'A','G',521},{'A','J',419},{'A','K',328},
{'B','G',391},{'B','H',230},{'B','I',356},{'B','J',220},
{'C','E',337},{'C','F',642},
{'D','F',829},{'D','K',334},
{'E','F',581},{'E','G',1254},
{'F','G',887},
{'G','H',242},
{'H','I',249},
{'I','J',713},
{'J','K',398}

'''
# 定义路径
dict_of_path = {'AB': 324, 'BA': 324, 'AC': 556, 'CA': 556, 'AD': 241, 'DA': 241, 'AF': 703, 'FA': 703, 'AG': 521,
                'GA': 521, 'AJ': 419, 'JA': 419, 'AK': 328, 'KA': 328,
                'BG': 391, 'GB': 391, 'BH': 230, 'HB': 230, 'BI': 356, 'IB': 356, 'BJ': 220, 'JB': 220,
                'CE': 337, 'EC': 337, 'CF': 642, 'FC': 642,
                'DF': 829, 'FD': 829, 'DK': 334, 'KD': 334,
                'EF': 581, 'FE': 581, 'EG': 1254, 'GE': 1254,
                'FG': 887, 'GF': 887,
                'GH': 242, 'HG': 242,
                'HI': 249, 'IH': 249,
                'IJ': 713, 'JI': 713,
                'JK': 398, 'KJ': 398}


# 初始化路径
# 以A为起点，回到A点
# 最优path = ['D', 'K', 'J', 'B', 'I', 'H', 'G', 'F', 'E', 'C']


# 定义循环列表
class CycQueue():
    def __init__(self, lenth):
        self.lenth = lenth
        self.queque = []

    # 入队
    def enqueue(self, x):
        if len(self.queque) < self.lenth:
            self.queque.append(x)
        else:
            del self.queque[0]
            self.queque.append(x)


# 定义路径是否合理
def check_availiable(list_1):
    list_0 = [ele for ele in list_1]
    list_0.append('A')
    current_path_for_check = CycQueue(2)
    current_path_for_check.enqueue('A')
    for ele in list_0:
        current_path_for_check.enqueue(ele)
        if current_path_for_check.queque[0] + current_path_for_check.queque[1] not in dict_of_path.keys():
            return False
    return True


# 定义两两随机交换的函数
def pairs_in_change(list_0):
    copy_list = [ele for ele in list_0]
    lenth_of_list_0 = len(list_0)
    q_list_0 = [i for i in range(lenth_of_list_0)]
    q_choise_0 = random.choice(q_list_0)
    q_list_0.remove(q_choise_0)
    q_choise_1 = random.choice(q_list_0)
    q_0 = copy_list[q_choise_1]
    copy_list[q_choise_1] = copy_list[q_choise_0]
    copy_list[q_choise_0] = q_0
    return copy_list


# 定义三个交换
def trible_in_change(list_0):
    copy_list = [ele for ele in list_0]
    lenth_of_list_0 = len(list_0)
    # 随机选择三个index
    index_of_list_0 = [i for i in range(lenth_of_list_0)]
    q_choise_0 = random.choice(index_of_list_0)
    index_of_list_0.remove(q_choise_0)
    q_choise_1 = random.choice(index_of_list_0)
    index_of_list_0.remove(q_choise_1)
    q_choise_2 = random.choice(index_of_list_0)
    choise_list = [q_choise_1, q_choise_2, q_choise_0]
    choise_list.sort()
    change_elements = copy_list[choise_list[0]: choise_list[1] + 1]
    for j in range(len(change_elements)):
        copy_list.insert(choise_list[2] + 2 * j + 1, change_elements[j])
        del copy_list[choise_list[0]]
    return copy_list


# 定义概率触发器
def Probablity_trigger(p):
    a = random.random()
    if a <= p:
        return 1
    else:
        return 0


# 定义概率函数
def Probablity(q_list, x_list, T):
    if distance(q_list) < distance(x_list):
        return 1
    else:
        return numpy.exp(((distance(x_list) - distance(q_list)) / T))
        # return 0


# 定义优化目标
def distance(list_0):
    q_sum = 0
    currren_path_for_distance = CycQueue(2)
    currren_path_for_distance.enqueue('A')
    for ele in list_0:
        currren_path_for_distance.enqueue(ele)
        q_sum += dict_of_path[currren_path_for_distance.queque[0] + currren_path_for_distance.queque[1]]
    q_sum += dict_of_path[list_0[-1] + 'A']
    return q_sum


if __name__ == '__main__':
    path = ['B', 'H', 'I', 'J', 'K', 'D', 'F', 'G', 'E', 'C']
    path_que = CycQueue(2)
    path_que.enqueue(path)
    path_que.enqueue(path)
    # 初始化温度
    T = 0.0001
    # 设置低温
    T_min = 0.00001
    while T > T_min:
        # 连续十五次没有发生交换，则终止循环然后降温
        Q = CycQueue(5)
        i = 0
        while True:
            if Q.queque == [0 for j in range(5)] or i > 10240:
                break
            copy_list = [ele for ele in path]
            # 确定是两两换还是三换
            q_list1 = pairs_in_change(copy_list)
            while check_availiable(q_list1) is False:
                q_list1 = pairs_in_change(q_list1)
            q_list2 = trible_in_change(copy_list)
            while check_availiable(q_list2) is False:
                q_list2 = trible_in_change(q_list2)
            if Probablity_trigger(1 / 2) is True:
                q_list = q_list1
            else:
                q_list = q_list2
            i += 1
            # 计算更新的概率
            p = Probablity(q_list, path_que.queque[1], T)
            motive = Probablity_trigger(p)
            if motive == 1:
                path_que.enqueue(q_list)
                Q.enqueue(1)
            else:
                Q.enqueue(0)
            print(Q.queque)
            print(distance(path_que.queque[1]), '温度', T)
        T = 0.9 * T
    path = path_que.queque[1]
    print('最短路径是', ['A'] + path + ['A'], '最短距离', distance(path))
