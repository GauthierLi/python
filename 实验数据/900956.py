from datetime import datetime
import numpy as np
from pylab import *
import pandas as pd
import matplotlib.pyplot as plt
stock = pd.read_csv(open('900956.csv'))
date = stock['日期_Date']
#  市盈率
PE = np.array(stock['市盈率_PE'])
# 每股收益
EPS = np.array(stock['每股收益(摊薄)(元/股)_EPS'])
# 股票价格
SP = PE*EPS
SP[24]=6
data1 = pd.DataFrame({'date':date,'SP':SP})
xs= [datetime.datetime.strptime(i, '%Y/%m/%d')for i in date]
plt.xlabel('time')
plt.ylabel('price of stock')
plt.plot(xs,SP,'o-',color='#539536')
print(data1)
plt.show()


