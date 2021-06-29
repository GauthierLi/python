import tushare as ts
pro = ts.pro_api('9136ced5612848d3b38cd96dde5059fe40bf4914d28676fa1c12aeaa')
# df = pro.income(ts_code = '600000.SH',start_date= '20180101',end_date='20191208',field='ts_code,ann_date')
df = pro.weekly(ts_code = '900956.SH',start_date= '20140101',end_date='20191208',fields='trade_date, close, open')
df1 = pro.weekly(ts_code='600000.SH', start_date='20180101', end_date='20181101', fields='ts_code,trade_date,open,high,low,close,vol,amount')
print(df)
print(df1)