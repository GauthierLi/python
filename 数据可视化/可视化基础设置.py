import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# print(plt.style.available)  打印（查看）风格列表
# ['seaborn-notebook', 'seaborn-bright', 'seaborn-pastel', 'seaborn', 'seaborn-poster', 'Solarize_Light2', '_classic_test', 'seaborn-whitegrid', 'bmh', 'seaborn-ticks', 'seaborn-muted', 'seaborn-darkgrid', 'classic', 'fivethirtyeight', 'seaborn-dark', 'ggplot', 'seaborn-dark-palette', 'tableau-colorblind10', 'fast', 'seaborn-deep', 'dark_background', 'seaborn-talk', 'grayscale', 'seaborn-paper', 'seaborn-white', 'seaborn-colorblind']
plt.style.use('classic')      # 默认使用经典风格
fig = plt.figure()            # 创建图像
ax = plt.axes()               # 创建坐标轴对象
# fig,ax = plt.subplots()     同时创建出图像和坐标轴
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
plt.title('例图')
ax.set_xlabel('X轴')
ax.set_ylabel('y轴')
# plt.legend(['y=100x+10'], loc='upper left')   # 在左上角显示图例
# ax.legend([line1, line2, line3], ['label1', 'label2', 'label3'], loc='lower right')
# 给三条线设置图例，位置在右下角
ax.spines['top'].set_visible(False)   # 隐藏上边框，下边框bottom，左边框left，右边框right
'''
ax.set_xticks([])                              # 隐藏X轴刻度和刻度值
ax.xsxis.set_major_formatter(plt.NullFormatter())   # 只隐藏刻度值，同时保留刻度
'''
# 设置坐标轴刻度和刻度标签
ax.set_xticks([1,2,3])                         # 设置X轴刻度
ax.set_yticks([1,2,3])
ax.set_xticklabels(['one', 'two', 'three'])   # 设置X轴刻度标签
ax.set_yticklabels(['one', 'two', 'three'])
# ax1 = fig.add_axes()   # 图中图
# fig,ax = plt.subplots(2, 2, sharex=True, sharey=True)
# 设置对中文的支持
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
'''
# 将图像保存到当前文件夹的file_name.png文件之中
fig.savefig('file_name.png')
'''
plt.show()