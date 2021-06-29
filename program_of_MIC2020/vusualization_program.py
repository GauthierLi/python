import numpy as np
from pylab import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read the data of matches
matches_data = pd.read_csv(open('matches.csv'))
print(matches_data)

# get the opponent id
opponentID = []
for ele in matches_data['OpponentID']:
    if ele in opponentID:
        continue
    else:
        opponentID.append(ele)
# process the opponent dict for convenience
opponent_score_dict = dict(zip(opponentID, np.zeros(19)))
opponent_times_dict = dict(zip(opponentID, np.zeros(19)))

coach_dict = {'Coach1': 0, 'Coach2': 1, 'Coach3': 2}
side_dict = {'away': 0, 'home': 1}
# create the coach_side matrix
coach_side_matrix = np.reshape(np.zeros(6), [2, 3])
# define the average score of our team
average_score = 0
for i in range(38):
    q = matches_data[i:i + 1]
    coach_side_matrix[side_dict[q['Side'][i]]][coach_dict[q['CoachID'][i]]] += q['OwnScore'][i]
    opponent_score_dict[q['OpponentID'][i]] += q['OpponentScore'][i]
    opponent_times_dict[q['OpponentID'][i]] += 1
    average_score += q['OwnScore'][i]
average_score = average_score / 38
print('average score:', average_score)
# output
# average score: 1.15789473684
print('opponent_times_dict:', opponent_times_dict)
# output
# opponent_times_dict: {'Opponent19': 2.0, 'Opponent16': 2.0, 'Opponent6': 2.0, 'Opponent18': 2.0,
# 'Opponent13': 2.0, 'Opponent14': 2.0, 'Opponent9': 2.0, 'Opponent3': 2.0, 'Opponent7': 2.0,
# 'Opponent15': 2.0, 'Opponent10': 2.0, 'Opponent4': 2.0, 'Opponent17': 2.0, 'Opponent1': 2.0,
# 'Opponent5': 2.0, 'Opponent2': 2.0, 'Opponent12': 2.0, 'Opponent8': 2.0, 'Opponent11': 2.0}


# times of each coach
times = [9, 5, 24]
for i in range(2):
    for j in range(3):
        coach_side_matrix[i][j] = coach_side_matrix[i][j] / times[j]
print('coach_side_matrix:', '\n', coach_side_matrix)
# output
# coach_side_matrix:
#  [[ 0.22222222  0.6         0.45833333]
#  [ 0.55555556  1.4         0.66666667]]

# plot the average score of situation
coach_side_dataframe = pd.DataFrame(coach_side_matrix, columns=['Coach1', 'Coach2', 'Coach3'])
sns.heatmap(coach_side_dataframe, annot=True)
plt.show()


# get the score of opponent and level
opponent_level_dict = {}
good_team = []
bad_team = []
for key in opponent_score_dict.keys():
    opponent_score_dict[key] = opponent_score_dict[key] / 2
    if opponent_score_dict[key] > average_score:
        opponent_level_dict[key] = 'good'
        good_team.append(key)
    elif opponent_score_dict[key] < average_score:
        opponent_level_dict[key] = 'bad'
        bad_team.append(key)
    else:
        opponent_level_dict[key] = 'same'
        good_team.append(key)
print('opponent_score_dict:', opponent_score_dict)
# output
# opponent_score_dict: {'Opponent19': 0.5, 'Opponent16': 0.5, 'Opponent6': 1.5, 'Opponent18': 1.0,
# 'Opponent13': 2.5, 'Opponent14': 1.5, 'Opponent9': 5.0, 'Opponent3': 1.0, 'Opponent7': 1.5,
# 'Opponent15': 0.0, 'Opponent10': 1.5, 'Opponent4': 3.5, 'Opponent17': 0.0, 'Opponent1': 0.5,
# 'Opponent5': 3.0, 'Opponent2': 2.0, 'Opponent12': 1.5, 'Opponent8': 0.5, 'Opponent11': 1.5}

print('opponent_level_dict', opponent_level_dict)
print('good team:',good_team)
# output
# good team: ['Opponent6', 'Opponent13', 'Opponent14', 'Opponent9', 'Opponent7',
# 'Opponent10', 'Opponent4', 'Opponent5', 'Opponent2', 'Opponent12', 'Opponent11']

print('bad team:',bad_team)
# output
# bad team: ['Opponent19', 'Opponent16', 'Opponent18', 'Opponent3', 'Opponent15',
# 'Opponent17', 'Opponent1', 'Opponent8']


opponent_score_list = list(zip(opponent_score_dict.values(), opponent_score_dict.keys()))
print(sorted(opponent_score_list))
# output
# [(0.0, 'Opponent15'), (0.0, 'Opponent17'), (0.5, 'Opponent1'), (0.5, 'Opponent16'),
# (0.5, 'Opponent19'), (0.5, 'Opponent8'), (1.0, 'Opponent18'), (1.0, 'Opponent3'),
# (1.5, 'Opponent10'), (1.5, 'Opponent11'), (1.5, 'Opponent12'), (1.5, 'Opponent14'),
# (1.5, 'Opponent6'), (1.5, 'Opponent7'), (2.0, 'Opponent2'), (2.5, 'Opponent13'),
# (3.0, 'Opponent5'), (3.5, 'Opponent4'), (5.0, 'Opponent9')]
