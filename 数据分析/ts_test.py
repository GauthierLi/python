import tushare as ts
import seaborn as sns
import seaborn.regression as snsl
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 开始时间结束时间，选取一年的数据
end = datetime.today()
start = datetime(end.year-1,end.month,end.day)
end = str(end)
start = str(start)
# 选取一只股票
stock = ts.get_hist_data('900956')
a = list(stock.to_dict()['high'].keys())
b =[]
for i in a:
    A,B,C = str(i).partition('-')
    D,E,F = str(C).partition('-')
    b += [''.join([A,D,F])]
print(b)

print(stock['close'])


