#!/usr/bin/env python 3.5
# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 13:35
# @Author  : m1556
# @File    : calcCombination.py

'''
该文档是第一次关于递归的尝试，通过使用递归树，来得到所有对应组合的线性序
将结点Node作为树的分叉的枝干，然后放置于数组之中。
最后，通过递归，读取所有的枝干。
'''
class Node:
	value = 0
	nextNode = []

	def __init__(self, value):
		self.value = value
		self.nextNode = []

# 产生组合树
def findCombinationTree(array=[], n=1):
	if (n > len(array)):
		return []

	if (n == 1):
		result = []
		for i in array:
			node = Node(i)
			result.append(node)
		return result
	else:
		result = []
		for i in array:
			node = Node(i)
			arrayNew = []
			for j in array:
				if j > i:
					arrayNew.append(j)

			node.nextNode = findCombinationTree(arrayNew, n - 1)
			result.append(node)

		return result

# 打印组合树中的所有树枝
def takeAllPath(node=Node(-1)):
	if (len(node.nextNode) == 0):
		return [[node.value]]
	else:
		path = []
		for i in node.nextNode:
			previousNodes = takeAllPath(i)
			for j in previousNodes:
				pathTempory = []
				pathTempory.append(node.value)
				for k in j:
					pathTempory.append(k)

				path.append(pathTempory)

	return path

# 生成树 + 打印树枝
def getCombination(array=[], n=0):
	combination = findCombinationTree(array, n)
	result = []
	for i in combination:
		l = takeAllPath(i)
		for j in l:
			if len(j) == n:
				result.append(j)

	return result

if __name__ == '__main__':
	s = [i for i in range(50)]
	print(getCombination(s, 6))