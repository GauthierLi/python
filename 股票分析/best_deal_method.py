# pre-processing the dataframe
def pre_processing(df_stock):
    q_dict = {}
    for i in range(len(df_stock)):
        q = df_stock[i:i + 1]
        q_dict[q['trade_date'][i]] = {'open': q['open'][i], 'close': q['close'][i]}
    q_list = list(zip(q_dict.keys(), q_dict.values()))
    q_list.sort()
    q_tuple = tuple(q_list)
    return q_tuple


def best_deal_fund_func(DataFrame):
    pass
