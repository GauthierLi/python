"""
# 循环输入定义一个m*n的矩阵
print('please input m,n:')
m,n = eval(input())
a = [[0]*n for i in range(m)]                      # 初始化矩阵
for i in range(m):
    for j in range(n):
        a[i][j]=i+j
print('matrice a:')
for i in range(n):
    print(a[i])

------------------------------------------------------------------------------------------------------------------------
# 列表与元组
lock = 'false'
mlist = ['monster', 1, 'Cara', lock]              # 定义列表
print(mlist[0])                                   # 输出列表第一个元素
print(mlist)                                      # 输出整个列表


# 元组
atuple = (0, 'join', 32, 3.5, 'end')
i = 0
while atuple[i]!='end':
    print(atuple[i])
    i+=1

------------------------------------------------------------------------------------------------------------------------
# 序列的操作
string = "learning python"
print(string[0], string[2], string[-2])

list1 = ['l', 'e', 'a', 'n', 'i', 'n', 'g', ' ', 'p', 'y']
print(format(list1[0:8:1]))

print([1, 2, 3]+[4, 5, 6])                          # 序列相加
print(3*[1, 2, 3])                                  # 序列相乘
print([1, 2, 4] > [1, 2, 3, 4])                     # 序列比较
print([1, 2, [2, 3, 4, 5]] > [1, 2, [5]])


------------------------------------------------------------------------------------------------------------------------
# 成员资格验证
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9,)
animals = ['elephant', 'dog', 'cat']
print('elephant' in animals,'100' in numbers)

------------------------------------------------------------------------------------------------------------------------
# 动态创建一个序列
p = []
for i in range(5):
    p += [i]
print(p)

------------------------------------------------------------------------------------------------------------------------
# 动态成员资格验证
user = []
for j in range(5):
    user += [j+1]
print(user)
print('len = {0},max = {1},min = {2},sum = {3}'.format(len(user), max(user), min(user), sum(user)))
                                                      # 取最大值，最小值
while 1:
    a = eval(input('Enter:'))in user                  # eval()函数很重要，此处如果没有eval函数则会返回false
    print(a)
    if(eval(input())==125):
        break

------------------------------------------------------------------------------------------------------------------------
# 阶乘函数
import functools


def mul(a, b):
    return a*b


n = eval(input('input n:'))
if n == 0:
    print('{}!={}'.format(n, 1))
else:
    print('{}!={}'.format(n, functools.reduce(mul, range(1, n+1))))

------------------------------------------------------------------------------------------------------------------------

# enumerate函数与zip函数
animals = ['dog', 'cat', 'elephant', 'penguin']
plants = ['tree', 'flower', 'apple tree', 'branch']
fruits = ['apple', 'pear', 'cherry', 'strawberry']
for i, animal in enumerate(animals):                     # enumerate()函数使用
    print(i, animal)
s = zip(animals, plants, fruits)
l = list(s)
print(l)
l1 = zip(*l)
# for z in range(3):
#     print(list(l1)[z])                                  question:为何出错？？？？
print(list(l1)[0])
print(len(list(l1)))                                      # 编译结果：0
print(list(l1))                                           # 编译结果：[]  answer:zip解压后得到的列表被使用一次后就清空了

------------------------------------------------------------------------------------------------------------------------
a = [0]*5                                                 # 列表的初始化
print(a)                                                  # [0, 0, 0, 0, 0,]
a[0] = 'a'; a[1] = 'b'; a[2] = 'c';a[3] = 'd';a[4] = 'e'  # 元素的赋值
print(a)                                                  # ['a', 'b', 'c', 'd', 'e']
del a[2]                                                  # 元素的删除
print(a)                                                  # ['a', 'b', 'd', 'e']
name = list('perl')
name[1:] = list('ython')                                  # 元素分片赋值
print(name)                                               # ['p', 'y', 't', 'h', 'o', 'n']
name[2:1] = list(' learning')                             # 元素分片赋值的插入
print(name)                                              # ['p','y','','l','e','a','r', 'n','i','n','g','t','h','o','n']
name[2:11] = []                                           # 分片赋值也可用于删除
print(name)                                               # ['p', 'y', 't', 'h', 'o', 'n']
name[2:11:2] = [8, 5]                                     # 分片赋值可设置步长
print(name)                                               # ['p', 'y', 8, 'h', 5, 'n']

------------------------------------------------------------------------------------------------------------------------

# 列表解析
a = [i for i in range(8)]
del a[0]
print(a)                                                  # [1, 2, 3, 4, 5, 6, 7]
b = [x**2 for x in range(10)]
print(b)                                                  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1])
                                                          # [(0,1),(0,3),(2,1),(2,3),(4,1),(4,3)]
matrice_a = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
print([row[0] for row in matrice_a])                      # [1, 2, 3]
print(matrice_a[1])                                       # [2, 3, 4]
print(matrice_a[2][1])                                    # 4

------------------------------------------------------------------------------------------------------------------------
# 适用于序列的操作
x = [2, 2, 3, 5, 2, 6, 88, 7, 2]
print(x.count(2))                                         # 2在x中出现的次数
print(x.index(88))                                        # 88第一次在x中出现的位置


# 下列操作是对原列表进行操作，而不是返回一个新列表
l = [1, 2, 3, 4]
l.append(5)                                               # 在l后面添加一个元素
print(l)                                                  # [1, 2, 3, 4, 5]

------------------------------------------------------------------------------------------------------------------------
# 字典的操作
d1 = { 'name':'gauthier', 'age': 18, 'tall': 177}
print(d1)
d2 = dict()
d22 = dict((['a', 1], ['b', 2], ['c', 3]))                # 字典的序列定义
print(d22)
d3 = dict(name = 'Gauthier', age = 21)                    # 字典的等于号定义
print(d3)


# 字典的访问
print(d3['name'])
d4 = {'name':{'first': 'John', 'last': 'Hank'}, 'score': [60, 55, 67, 88, 95, 100]}
print(d4['name']['last'], d4['score'][5])                 # 字典嵌套字典的关键词索引和字典嵌套序列的关键词索引


# 字典的更行
d3['name'] = 'Gauthier_Li'                                # 字典中关键字的变更
d3['score'] = [55, 58, 66, 88, 100]                       # 字典的添加关键字
print(d3)
del d3['age']                                             # 字典关键字的删除
print(d3)
print('age' in d3)                                        # 检测关键字是否在字典中
print(len(d3))                                            # 检测关键字的个数
print(list(d3))                                           # 打印字典中的关键字


# 新字典的创建
d5 = {}.fromkeys(['name', 'age', 'score'], 'None defined')# 若不给定值，则初始值为None
d5['name'] = 'Gauthier_Li'
d5['age'] = 21
d5['score'] = [58, 66, 88, 98]
print(d5)


# d.keys(), d.values(), d.items()方法
print(d5.keys())                                          # 返回一个包含字典的所有关键字的列表
print(d5.values())                                        # 返回一个包含字典的所有值的列表
print(d5.items())                                         # 返回一个包含所有（关键词，值）的元组的列表


# 字典的复制与删除的方法
p = d5.copy()                                             # 得到一个d5的副本存放于p中
print(d5)

# d5.clear()                                              # 删除字典中的所有元素，使其变为空字典
# print(d5, p)
print(d5.popitem())                                       # 随机删除一个关键词及其值，并返回改（关键词，值）元组
print(d5)


# d.get(), d.pop()方法
d6 = {'name': 'Gauthier_Li', 'sex': 'man', 'age': '21', 'score': [58, 66, 88, 98]}
print(d6.get('name', 'Not exist'))                       # 查找关键字，存在则返回值，不存在则返回value的值，默认返回None

------------------------------------------------------------------------------------------------------------------------
# 调用自己写的函数
import sys
sys.path.append('E:\pymatlab')
from Py_Mat import *

M = Mat([[1,5],[8,4]])
Mat_Print(Mat_Mul(M,M.Inverse()))

------------------------------------------------------------------------------------------------------------------------
# 文件的写入与读取
# 素数表的打印
a = 1
f = open(r'E:\pytest\sushu.txt', 'w')
for j in range(1000):
    count = 0
    for i in range(a):
        if a % (i+1) == 0:
            count += 1
    if count == 2:
        f.writelines([ str(a), '  '])
    a += 1
f.write('end')
f.close()
f = open(r'E:\pytest\sushu.txt','r')
print(f.readlines())

------------------------------------------------------------------------------------------------------------------------
from tkinter import *
from math import *
w = Tk()
w.title('函数曲线')
c = Canvas(w,width = 300,height = 200,bg = 'white')
c.pack()
t = 0
while t<=10*pi:
    x = 3*(cos(t)+t*sin(t))
    y = 3*(sin(t)+t*cos(t))
    x+=150
    y+=100
    c.create_rectangle(x,y,x+0.5,y+0.5)
    t+=0.1

------------------------------------------------------------------------------------------------------------------------
# 快速排序法
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x<pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x>pivot]
    return quicksort(left) + middle + quicksort(right)

a = [26,18,13,65,84,11,158,32,665,849,999,262,1,25]
import random

for i in range(50):
    b = [random.randrange(500)]
    a += b
print(len(a))
print(quicksort(a))

------------------------------------------------------------------------------------------------------------------------

# 一元梯度下降法
def y(x):
    return (x-1)**2-1
x = 0.001
step = 0.0001
while abs(2*x-2)>0.000000001:
    x -= (2*x-2)*step
print(x)

------------------------------------------------------------------------------------------------------------------------

import tushare as ts
import numpy as np
X = list(ts.get_gdp_year()['year'])
Y = list(ts.get_gdp_year()['gdp'])
step = 10000
a = 0.01
def L(a,X,Y):
    N = len(X)
    L = 0
    for i in range(N):
        L += (Y[i]-np.exp(a*X[i]))**2
    return L/N
def DL(a,X,Y):
    N = len(X)
    DL = 0
    for i in range(N):
        DL += 2*(Y[i]-np.exp(a*X[i])*(a*np.exp(a*X[i])))
    return DL/N
while abs(DL(a,X,Y))>0.0001:
    u = 1000000000000
    step = step/u
    if u > 0.0001: u -= 1
    a += DL(a,X,Y)*step
    print(a,'\t', L(a,X,Y), '\t' , DL(a,X,Y) )
------------------------------------------------------------------------------------------------------------------------

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
print(fib(7))
for i in range(6):
    print(i)

# ----------------------------------------------------------------------------------------------------------------------
def mean(numlist):
    s = 0.0
    for num in numlist:
        s = s + num
    return  s/len(numlist)
Is = eval(input('please input numlist:'))
print("平均值：",mean(Is))
# ----------------------------------------------------------------------------------------------------------------------


#-------------------------------------------类的设计--------------------------------------------------------------------
# coding:utf-8
class Horse(object):
    variety = "大宛马"
    def __init__(self, name = "green", height = 0.5, length = 1.3, sex = "male"):
        # self.name是成员变量，name是形参、局部变量
        self.name = name
        self.height = height
        self.length = length
        self.sex = sex
        print("A baby horse is born called", self.name)

    def print_info(self):
        print(self.name, self.height, self.length, self.sex, Horse.variety)#,Horse.address
        Horse.print_variety() # 在对象方法里通过类调用类方法，避免
        Horse().print_ci(200, 100)# 对象调用静态方法
        Horse.print_ci(200, 100) # 类调用静态方法

    @staticmethod
    def print_ci(x, y):
        print(x, y)

    @classmethod
    def pp(cls):
        # 类使用类变量
        print(cls.variety, Horse.variety, cls.address)
        print(Horse().name)  # 对象使用对象的成员变量
    @classmethod
    def print_variety(cls):
        cls.address = "xi'an"
        print("type", type(cls.address))
        print(cls.variety, Horse.variety, cls.address)
        Horse.pp()# 类调用类方法
        Horse().print_ci(100, 100)# 对象调用静态方法

a = Horse("xiaoxuanfeng")
b = Horse("pilihuo", sex = "female")
a.print_info()
b.print_info()
Horse.print_variety()
print("*" * 20)
Horse.pp() # 类调用类方法
Horse.print_ci(12, 23)# 类外类调用静态方法
a.print_ci(23, 31) # 类外对象调用静态方法


# way1
one_to_ninety_nine_list = []
for i in range(100):
    one_to_ninety_nine_list.append(i)
print(one_to_ninety_nine_list)

# way2
one_to_ninety_nine_list1 = [i for i in range(100)]
print(one_to_ninety_nine_list1)

"""
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)




















def factorial(n):
    if n == 0:
        return 1
    q = 1
    for i in range(n):
        q = q * (n - i)
    return q