import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from passing_events_analysing1 import passing_member_statistics
from full_events_analysing import loseball_dict

passing_data = pd.read_csv(open('passingevents.csv'))
Huskie_team_member = passing_member_statistics['Huskies']
relationship_dict = {}
for member in Huskie_team_member:
    relationship_dict[member] = dict(zip(Huskie_team_member, [0 for i in range(len(Huskie_team_member))]))

for i in range(23429):
    q = passing_data[i:i + 1]
    if q['TeamID'][i] == 'Huskies':
        relationship_dict[q['OriginPlayerID'][i]][q['DestinationPlayerID'][i]] += 1
        relationship_dict[q['DestinationPlayerID'][i]][q['OriginPlayerID'][i]] += 0.5
print(relationship_dict)

# define the dict of individule's, whether is the most been trust
dict_of_trust = dict(zip(Huskie_team_member, [0 for i in range(len(Huskie_team_member))]))
for member in Huskie_team_member:
    for key in relationship_dict.keys():
        dict_of_trust[member] += relationship_dict[key][member]


dict2_of_trust = dict(zip(dict_of_trust.keys(),dict_of_trust.values()))
dict_of_trust = list(zip(dict_of_trust.values(),dict_of_trust.keys()))
dict_of_trust = sorted(dict_of_trust)
print(dict_of_trust)
x = [i for i in range(len(dict_of_trust))]
y = [dict_of_trust[i][0] for i in range(len(dict_of_trust))]
plt.bar(x, y)
# show the number on the bar
for a, b in zip(x, y):
    plt.text(a, b + 0.2, '%d' % b, ha='center', va='bottom', fontsize=6)
plt.show()

dict_of_lose_ball_rate = {}
for key in loseball_dict.keys():
    dict_of_lose_ball_rate[key] = loseball_dict[key]/dict2_of_trust[key]
list2_of_lose_ball_rate = list(zip(dict_of_lose_ball_rate.values(), dict_of_lose_ball_rate.keys()))
list2_of_lose_ball_rate.sort()
print(list2_of_lose_ball_rate)

