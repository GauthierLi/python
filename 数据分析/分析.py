import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import seaborn.regression as snsl
from datetime import datetime
import tushare as ts
import numpy as np


# 股票收盘价走势
sns.set_style("whitegrid")
# 开始时间结束时间，选取一年的数据
end = datetime.today()
start = datetime(end.year-5,end.month,end.day)
end = str(end)
start = str(start)
# 选取一只股票
stock = ts.get_hist_data('900956',start,end)

# 闭市价格
A = list(stock['close'])
a = stock['close'].plot(legend = True,figsize = (10,4))
a.invert_xaxis()
x = pd.DataFrame(stock)
pd.DataFrame.to_excel(x,'stock900956.xls')



# 每日涨跌幅度
stock['Daily Return'] = stock['close'].pct_change()
B = list(stock['Daily Return'])
for i in range(len(B)):
    if B[i]==0:
        B[i] = B[i-1]
b = stock['Daily Return'].plot(legend = True,figsize=(10,4))
b.invert_xaxis()
plt.show()


# 每日开盘价格
c = stock['open'].plot(legend = True,figsize = (10,4))
c.invert_xaxis()



# 股票市盈率PER
# d = []
# for i in range(len(A)):
#     e = A[i]/B[i]
#     d.append(e)
# D = dict(stock['close']).keys()
# D1=list(D)
# E = pd.DataFrame(d,index=D1)
# E1 = E.plot(legend = True,figsize = (10,4))
# E1.invert_xaxis()
d = ts.get_today_all()

# ------------------------------------------------------------------------------------------------------------------------

# # get the quarter gdp from tushare
# a = ts.get_gdp_quarter()
# # get year-gdp
# A = ts.get_gdp_year()
# # get the list of quarter
# quarter = np.array(a['quarter'])[-73::-1]
# for i in range(len(quarter)):
#     quarter[i] = str(quarter[i])
#     b, c, d = quarter[i].partition('.')
#     d = int(d)/4
#     quarter[i] = int(b)+d
# # get a list of gdp of a quarter
# gdp_quarter = np.array(a['gdp'])[-73::-1]
# for i in range(len(gdp_quarter)):
#     j = i%4
#     if j != 0:
#         for k in range(j):
#             gdp_quarter[i] = gdp_quarter[i] - gdp_quarter[i-k-1]
# # plot the line quarter-gdp
# plt.plot(quarter, gdp_quarter,label='qG', linewidth=2)
# plt.legend()
# plt.xlabel('quarter')
# plt.ylabel('GDP(\\one hundred million)')
#
# year = np.array(A['year'])[0:19]
# gdp_year = np.array(A['gdp'])[0:19]
# plt.plot(year, gdp_year,label='yG', linewidth=2)
# plt.legend()
# plt.show()
# print(year, '\n', gdp_year)
# # print(a)
#
# plt.plot(quarter[-1:-9:-1],gdp_quarter[-1:-9:-1],'rv', label='qG', linewidth=5)
# plt.legend()
# plt.xlabel('quarter')
# plt.ylabel('GDP(\\one hundred million)')
plt.show()
