def nor(lst):
    average = 0
    derta = 0
    s = 0
    for ele in lst:
        s += ele
    average = s/len(lst)
    s = 0
    for ele in lst:
        s += (ele - average)**2
    derta = s/len(lst)
    q_list = []
    for ele in lst:
        q_list.append((ele - average)/derta)
    return q_list

print(nor([1, 2.8]))
print(nor([1,4]))