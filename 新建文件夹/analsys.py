#!/usr/bin/env python 3.5
# -*- coding: utf-8 -*-
# @Time    : 2021/2/12 9:31
# @Author  : m1556
# @File    : analsys.py
# @Version : test
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#定义坐标轴
fig = plt.figure()
ax1 = plt.axes(projection='3d')

class Three_body:
	list_init_val = []
	m1 = 1
	m2 = 2.5
	m3 = 3.4
	G = 1
	i_n = 100000
	f_h = 0.05
	list2D_values = []

	def __init__(self, m1, m2, m3, list_x1, list_v1, list_x2, list_v2, list_x3, list_v3):
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3
		for i in range(3):
			self.list_init_val.append(list_x1[i])

		for i in range(3):
			self.list_init_val.append(list_v1[i])

		for i in range(3):
			self.list_init_val.append(list_x2[i])

		for i in range(3):
			self.list_init_val.append(list_v2[i])

		for i in range(3):
			self.list_init_val.append(list_x3[i])

		for i in range(3):
			self.list_init_val.append(list_v3[i])

	def representation_equation(self, list_val):
		x1 = list_val[0]
		y1 = list_val[1]
		z1 = list_val[2]
		dx1 = list_val[3]
		dy1 = list_val[4]
		dz1 = list_val[5]
		x2 = list_val[6]
		y2 = list_val[7]
		z2 = list_val[8]
		dx2 = list_val[9]
		dy2 = list_val[10]
		dz2 = list_val[11]
		x3 = list_val[12]
		y3 = list_val[13]
		z3 = list_val[14]
		dx3 = list_val[15]
		dy3 = list_val[16]
		dz3 = list_val[17]

		f_r12 = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) + (z2 - z1) * (z2 - z1))
		f_r23 = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3) + (z2 - z3) * (z2 - z3))
		f_r13 = math.sqrt((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1) + (z3 - z1) * (z3 - z1))
		e12 = [(x2 - x1) / f_r12, (y2 - y1) / f_r12, (z2 - z1) / f_r12]
		e21 = [(x1 - x2) / f_r12, (y1 - y2) / f_r12, (z1 - z2) / f_r12]
		e23 = [(x3 - x2) / f_r23, (y3 - y2) / f_r23, (z3 - z2) / f_r23]
		e32 = [(x2 - x3) / f_r23, (y2 - y3) / f_r23, (z2 - z3) / f_r23]
		e13 = [(x3 - x1) / f_r13, (y3 - y1) / f_r13, (z3 - z1) / f_r13]
		e31 = [(x1 - x3) / f_r13, (y1 - y3) / f_r13, (z1 - z3) / f_r13]

		# 3600 * 24 * 365
		f_times_d = 1
		f_times_dd = 1
		ddx1 = self.G * self.m2 / (f_r12 * f_r12) * e12[0] + self.G * self.m3 / (f_r13 * f_r13) * e13[0]
		ddy1 = self.G * self.m2 / (f_r12 * f_r12) * e12[1] + self.G * self.m3 / (f_r13 * f_r13) * e13[1]
		ddz1 = self.G * self.m2 / (f_r12 * f_r12) * e12[2] + self.G * self.m3 / (f_r13 * f_r13) * e13[2]

		ddx2 = self.G * self.m1 / (f_r12 * f_r12) * e21[0] + self.G * self.m3 / (f_r23 * f_r23) * e23[0]
		ddy2 = self.G * self.m1 / (f_r12 * f_r12) * e21[1] + self.G * self.m3 / (f_r23 * f_r23) * e23[1]
		ddz2 = self.G * self.m1 / (f_r12 * f_r12) * e21[2] + self.G * self.m3 / (f_r23 * f_r23) * e23[2]

		ddx3 = self.G * self.m1 / (f_r13 * f_r13) * e31[0] + self.G * self.m2 / (f_r23 * f_r23) * e32[0]
		ddy3 = self.G * self.m1 / (f_r13 * f_r13) * e31[1] + self.G * self.m2 / (f_r23 * f_r23) * e32[1]
		ddz3 = self.G * self.m1 / (f_r13 * f_r13) * e31[2] + self.G * self.m2 / (f_r23 * f_r23) * e32[2]

		list_val_result = []
		list_val_result.append(f_times_d * dx1)
		list_val_result.append(f_times_d * dy1)
		list_val_result.append(f_times_d * dz1)
		list_val_result.append(f_times_dd * ddx1)
		list_val_result.append(f_times_dd * ddy1)
		list_val_result.append(f_times_dd * ddz1)
		list_val_result.append(f_times_d * dx2)
		list_val_result.append(f_times_d * dy2)
		list_val_result.append(f_times_d * dz2)
		list_val_result.append(f_times_dd * ddx2)
		list_val_result.append(f_times_dd * ddy2)
		list_val_result.append(f_times_dd * ddz2)
		list_val_result.append(f_times_d * dx3)
		list_val_result.append(f_times_d * dy3)
		list_val_result.append(f_times_d * dz3)
		list_val_result.append(f_times_dd * ddx3)
		list_val_result.append(f_times_dd * ddy3)
		list_val_result.append(f_times_dd * ddz3)

		return list_val_result

	def rouge_kutta_iter_formula(self, list_val):
		f_h = self.f_h
		list_k1 = self.representation_equation(list_val)
		list_k2 = self.representation_equation([list_val[i] + 0.5 * f_h * list_k1[i] for i in range(len(list_val))])
		list_k3 = self.representation_equation([list_val[i] + 0.5 * f_h * list_k2[i] for i in range(len(list_val))])
		list_k4 = self.representation_equation([list_val[i] + f_h * list_k3[i] for i in range(len(list_val))])

		list_val_result = [f_h / 6.0 * (list_k1[i] + 2.0 * list_k2[i] + 2.0 * list_k3[i] + list_k4[i]) for i in range(len(list_val))]
		list_val_result = [list_val_result[i] + list_val[i] for i in range(len(list_val))]
		return list_val_result

	def run(self):
		list_val = self.list_init_val
		for i in range(self.i_n):
			self.list2D_values.append(list_val)
			list_val = self.rouge_kutta_iter_formula(list_val)

			if i % 1500 == 0 and i > 2000:
				self.plot_graph(i)
				plt.show()
				plt.pause(0.001)

	def plot_graph(self, i_index_end):
		array_X1 = [self.list2D_values[i][0] for i in range(i_index_end - 2000, i_index_end)]
		array_Y1 = [self.list2D_values[i][1] for i in range(i_index_end - 2000, i_index_end)]
		array_Z1 = [self.list2D_values[i][2] for i in range(i_index_end - 2000, i_index_end)]
		array_X2 = [self.list2D_values[i][6] for i in range(i_index_end - 2000, i_index_end)]
		array_Y2 = [self.list2D_values[i][7] for i in range(i_index_end - 2000, i_index_end)]
		array_Z2 = [self.list2D_values[i][8] for i in range(i_index_end - 2000, i_index_end)]
		array_X3 = [self.list2D_values[i][12] for i in range(i_index_end - 2000, i_index_end)]
		array_Y3 = [self.list2D_values[i][13] for i in range(i_index_end - 2000, i_index_end)]
		array_Z3 = [self.list2D_values[i][14] for i in range(i_index_end - 2000, i_index_end)]


		ax1.plot3D(array_X1, array_Y1, array_Z1, 'r-')
		ax1.plot3D(array_X2, array_Y2, array_Z2, 'g-')
		ax1.plot3D(array_X3, array_Y3, array_Z3, 'b-')
		# plt.plot(array_X1, array_Y1, 'r-')
		# plt.plot(array_X2, array_Y2, 'g-')
		# plt.plot(array_X3, array_Y3, 'b-')


if __name__ == '__main__':
	list_x1 = [0, -100, 10]
	list_v1 = [1, 0, 0]
	list_x2 = [0, 0, 0]
	list_v2 = [0, 0, 0]
	list_x3 = [0, 50, 3]
	list_v3 = [2, 0, 0.0001]
	m1 = 30
	m2 = 100
	m3 = 5
	three_body = Three_body(m1, m2, m3, list_x1, list_v1, list_x2, list_v2, list_x3, list_v3)
	three_body.run()