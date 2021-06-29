import tushare as ts
import pandas as pd
import best_deal_method as bdm
import matplotlib.pyplot as plt
import least_squres

pro = ts.pro_api('9136ced5612848d3b38cd96dde5059fe40bf4914d28676fa1c12aeaa')
df = pro.daily(ts_code='000001.SZ', start_date='20200101', end_date='20200226')
# keys
# ['ts_code', 'trade_date', 'open', 'high', 'low', 'close', 'pre_close', 'change', 'pct_chg', 'vol', 'amount']
tuple_of_open_close = bdm.pre_processing(df)
# example: ('20200102', {'open': 16.649999999999999, 'close': 16.870000000000001})

# close 2nd open data
list_of_open = []
list_of_close = []
for ele in tuple_of_open_close:
    list_of_open.append(ele[1]['open'])
    list_of_close.append(ele[1]['close'])
del list_of_open[0]
list_of_close.pop()
print(least_squres.least_square(list_of_open, list_of_close, [13, 18, 0.02],['close','open']))
