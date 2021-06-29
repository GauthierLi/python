# coding:utf-8
# --------------------------------------------------分治法求阶层--------------------------------------------------------
# def J(n):
#     if n <= 0:
#         return print('n必须为正整数')
#     elif n == 1:
#         return 1
#     else:
#         return n * J(n - 1)
#
#
# print(J(5))

# --------------------------------------------------分治法快速排序------------------------------------------------------
# def quick_sort(A):
#     current_sum = 0
#     left = []
#     mid = []
#     right = []
#     A_sort = []
#
#     if len(A) == 0:
#         return A
#
#     if len(A) == 1:
#         A_sort.append(A[0])
#         return A_sort
#     else:
#         for i in A:
#             current_sum = current_sum + i
#         average = current_sum / len(A)
#         for i in A:
#             if i < average:
#                 left.append(i)
#             elif i == average:
#                 mid.append(i)
#             else:
#                 right.append(i)
#         return quick_sort(left) + mid + quick_sort(right)
#
#
# if __name__ == '__main__':
#     A = [11, 14, 55, 56, 114, 8, 0, 11, 556, 1.2, 12, 12]
#     print('after the quick sort, the list', A, 'become \n', quick_sort(A))

# --------------------------------------------------创建栈类以及栈的操作------------------------------------------------
'''
类里面有类对象cls,实例对象self，实例方法，类方法@classmethod，静态方法@staticmetho
实例对象可以调用所有方法，类对象只能调用类方法，类方法可以修改类参数，实例方法只能修改实例参数
'''


# class stack:
#     def __init__(self):
#         self.stack = []
#         self.top = 0
#
#     # 定义压入的实例方法
#     def push(self, item):
#         self.stack.append(item)
#         self.top += 1
#
#     # 定义弹出的实例方法
#     def pop(self):
#         # 删除栈顶端元素
#         if self.stackempty():
#             raise IndexError('error! stack is underflow!')
#         else:
#             pop = self.stack.pop()
#             self.top -= 1
#             return pop
#
#     # 定义检查栈是否空的方法
#     def stackempty(self):
#         if self.top == 0:
#             return True
#         else:
#             return False
#
#     # 定义检查栈中元素的个数
#     def sizes(self):
#         return self.top
#
#     # 定义检索栈顶的方法
#     def peek(self):
#         return self.stack[-1]
#
#
# if __name__ == '__main__':
#     A = stack()
#     print(A.stackempty())
#     A.push(4)
#     A.push('dog')
#     print(A.peek())
#     A.pop()
#     A.pop()
#     print(A.stack)
#     A.pop()


# --------------------------------------------------------队列实现------------------------------------------------------
# class Queue():
#
#     def __init__(self, size):
#         self.queue = []
#         self.size = size + 1
#         self.head = 0
#         self.tail = 0
#
#     def enqueue(self, element):
#         if self.isfull():
#             raise IndexError('queue is full')
#         else:
#             self.queue.append(element)
#             self.tail = (self.tail + 1) % self.size
#
#     def dequeue(self):
#         if self.isempty():
#             raise IndexError('queue is empty')
#         else:
#             self.queue.pop(0)
#             self.head = (self.head + 1) % self.size
#
#     def isfull(self):
#         return self.tail - self.head + 1 == self.size
#
#     def isempty(self):
#         return self.head == self.tail
#
#
# if __name__ == '__main__':
#     q = Queue(5)
#     for i in range(5):
#         q.enqueue(i + 1)
#     for i in range(2):
#         q.dequeue()
#     q.enqueue(7)
#     q.enqueue('dog')
#     q.dequeue()
#     print(q.queue,type(q.queue), q.head, q.tail)


# ------------------------------------------------------用类定义循环队列------------------------------------------------
# class que():
#
#     def __init__(self, size):
#         self.queue = []
#         self.size = size
#
#     def enqueue(self, x):
#         if len(self.queue) < self.size:
#             self.queue.append(x)
#         else:
#             del self.queue[0]
#             self.queue.append(x)
#
#
# if __name__ == '__main__':
#     Q = que(5)
#     for i in range(10):
#         Q.enqueue(i)
#     print(Q.queue)
# # --------------------------------------------------链表的实现----------------------------------------------------------
# class Node(object):
#     # 定义节点类
#     def __init__(self, ele):
#         self.ele = ele
#         self.next = None
#
#
# # node = Node(100)
# class Single_Link_List(object):
#     '''单链表'''
#
#     def __init__(self, node=None):
#         self.__head = node
#
#     def isempty(self):
#         # 链表是否为空
#         return self.__head == None
#
#     def length(self):
#         # 链表长度
#         # 定义一个current游标数数
#         cur = self.__head
#         # 定义一个计数器count
#         count = 0
#         while cur != None:
#             count += 1
#             cur = cur.next
#         return count
#
#     def travel(self):
#         # 遍历整个链表
#         cur = self.__head
#         while cur != None:
#             print(cur.ele, end=' ')
#             cur = cur.next
#
#     def add(self, item):
#         # 链表表头添加元素
#         pass
#
#     def append(self, item):
#         # 链表链尾添加元素
#         node = Node(item)
#         cur = self.__head
#         if self.isempty():
#             self.__head = node
#         else:
#             while cur.next != None:
#                 cur = cur.next
#             cur.next = node
#
#     def insert(self, position, item):
#         # 指定位置添加元素
#         pass
#
#     def remove(self, item):
#         # 删除某个节点
#         pass
#
#     def search(self, item):
#         # 查找某个节点是否存在
#         pass
