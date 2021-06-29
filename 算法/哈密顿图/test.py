import numpy as np

a = [0, 0, 1, 0, 1]
b = ['a', 'b', 'c', 'd', 'e']

q = []
for i in range(len(a)):
    if a[i] * b[i] != '':
        q.append(a[i] * b[i])
print(q)
