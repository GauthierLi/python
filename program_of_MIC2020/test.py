import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


a = [(29.0, 'Huskies_M7'), (50.0, 'Huskies_D10'), (58.0, 'Huskies_M10'), (62.0, 'Huskies_M5'), (69.5, 'Huskies_D9'),
     (82.5, 'Huskies_M11'), (94.0, 'Huskies_M13'), (101.0, 'Huskies_F3'), (107.0, 'Huskies_M2'), (207.0, 'Huskies_M9'),
     (245.5, 'Huskies_M8'), (282.0, 'Huskies_M12'), (302.0, 'Huskies_F5'), (351.5, 'Huskies_F4'), (406.5, 'Huskies_F6'),
     (418.5, 'Huskies_D8'), (488.0, 'Huskies_D6'), (592.0, 'Huskies_F1'), (653.0, 'Huskies_D7'), (732.5, 'Huskies_G1'),
     (757.0, 'Huskies_D2'), (769.5, 'Huskies_M4'), (791.0, 'Huskies_M6'), (893.5, 'Huskies_D5'), (899.5, 'Huskies_D4'),
     (945.5, 'Huskies_D3'), (1103.5, 'Huskies_D1'), (1160.5, 'Huskies_M3'), (1356.5, 'Huskies_F2'),
     (1644.5, 'Huskies_M1')]
b = [(0.4892086330935252, 'Huskies_D9'), (0.5480396380870315, 'Huskies_M3'), (0.5792106725958867, 'Huskies_D4'),
     (0.5862068965517241, 'Huskies_M7'), (0.6068713894800851, 'Huskies_M1'), (0.6162919277552524, 'Huskies_F2'),
     (0.6448598130841121, 'Huskies_M2'), (0.6790058170280275, 'Huskies_D3'), (0.7040951122853368, 'Huskies_D2'),
     (0.775713638423199, 'Huskies_D1'), (0.7912702853945159, 'Huskies_D5'), (0.8085106382978723, 'Huskies_M13'),
     (0.8225806451612904, 'Huskies_M5'), (0.8554360812425329, 'Huskies_D8'), (0.8606060606060606, 'Huskies_M11'),
     (0.9078498293515358, 'Huskies_G1'), (0.9096816114359974, 'Huskies_M4'), (0.92, 'Huskies_D10'),
     (0.9207920792079208, 'Huskies_F3'), (0.9528688524590164, 'Huskies_D6'), (0.9678407350689127, 'Huskies_D7'),
     (0.9898167006109979, 'Huskies_M8'), (1.031605562579014, 'Huskies_M6'), (1.065190651906519, 'Huskies_F6'),
     (1.285024154589372, 'Huskies_M9'), (1.3509933774834437, 'Huskies_F5'), (1.3581560283687943, 'Huskies_M12'),
     (1.3793103448275863, 'Huskies_M10'), (1.5277382645803699, 'Huskies_F4'), (1.6047297297297298, 'Huskies_F1')]

lst = []
for ele in a:
     q = []
     q.append(ele[0])
     for elem in b:
          if ele[1] == elem[1]:
               q.append(elem[0])
               q.append(ele[1])
     lst.append(q)
print(lst)

plt.figure()
x = [i for i in range(len(lst))]
x1 = [i+0.35 for i in range(len(lst))]
y = [j[0] for j in lst]
y1 = [k[1] for k in lst]
print(y1)
plt.bar(x, y,alpha = 0.9 ,label='trust',width=0.35)
plt.legend()
plt.show()

plt.bar(x1, y1,alpha = 0.9,label='loseball_rate',width=0.35)
plt.legend()
plt.show()

