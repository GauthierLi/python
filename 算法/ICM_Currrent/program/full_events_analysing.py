import numpy as np
from pylab import *
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

full_data = pd.read_csv(open('fullevents.csv'))
print(full_data[:3])
# # member staristics
# member_statistics = {}
# for i in range(59271):
#     if full_data['TeamID'][i] not in member_statistics.keys():
#         member_statistics[full_data['TeamID'][i]] = []
#     if full_data['OriginPlayerID'][i] not in member_statistics[full_data['TeamID'][i]]:
#         member_statistics[full_data['TeamID'][i]].append(full_data['OriginPlayerID'][i])
# print(member_statistics)
# result
member_statistics = {
    'Opponent16': ['Opponent16_G1', 'Opponent16_D1', 'Opponent16_M1', 'Opponent16_D2', 'Opponent16_F1', 'Opponent16_D3',
                   'Opponent16_D4', 'Opponent16_F2', 'Opponent16_M2', 'Opponent16_M3', 'Opponent16_F3', 'Opponent16_F4',
                   'Opponent16_F5', 'Opponent16_F6', 'Opponent16_M4', 'Opponent16_D5', 'Opponent13_D1', 'Opponent16_G2',
                   'Opponent16_D6'],
    'Opponent4': ['Opponent4_M1', 'Opponent4_D1', 'Opponent4_D2', 'Opponent4_D3', 'Opponent4_D4', 'Opponent4_M2',
                  'Opponent4_M3', 'Opponent4_G1', 'Opponent4_D5', 'Opponent4_M4', 'Opponent4_F1', 'Opponent4_M5',
                  'Opponent4_M6', 'Opponent4_F2', 'Opponent4_D6', 'Opponent4_M7', 'Opponent4_M8'],
    'Opponent13': ['Opponent13_M1', 'Opponent13_D1', 'Opponent13_M2', 'Opponent13_M3', 'Opponent13_D2', 'Opponent13_D3',
                   'Opponent13_D4', 'Opponent13_G1', 'Opponent13_M4', 'Opponent13_M5', 'Opponent13_F1', 'Opponent13_M6',
                   'Opponent13_F2', 'Opponent13_D5', 'Opponent13_M7', 'Opponent13_D6', 'Opponent13_G2',
                   'Opponent13_M8'],
    'Opponent8': ['Opponent8_D1', 'Opponent8_M1', 'Opponent8_M2', 'Opponent8_M3', 'Opponent8_M4', 'Opponent8_G1',
                  'Opponent8_F1', 'Opponent8_D2', 'Opponent8_D3', 'Opponent8_D4', 'Opponent8_M5', 'Opponent8_F2',
                  'Opponent8_D5', 'Opponent8_F3', 'Opponent8_D6', 'Opponent8_M6', 'Opponent8_D7', 'Opponent8_F4',
                  'Opponent8_F5'],
    'Opponent14': ['Opponent14_D1', 'Opponent14_D2', 'Opponent14_G1', 'Opponent14_M1', 'Opponent14_D3', 'Opponent14_D4',
                   'Opponent14_D5', 'Opponent14_M2', 'Opponent14_F1', 'Opponent14_M3', 'Opponent14_F2', 'Opponent14_F3',
                   'Opponent14_F4', 'Opponent14_D6', 'Opponent14_M4', 'Opponent14_M5', 'Opponent14_G2', 'Opponent14_M6',
                   'Opponent14_D7'],
    'Opponent9': ['Opponent9_M1', 'Opponent9_F1', 'Opponent9_M2', 'Opponent9_M3', 'Opponent9_D1', 'Opponent9_D2',
                  'Opponent9_D3', 'Opponent9_F2', 'Opponent9_G1', 'Opponent9_D4', 'Opponent9_D5', 'Opponent9_M4',
                  'Opponent9_M5', 'Opponent9_M6', 'Opponent9_D6', 'Opponent9_F3', 'Opponent5_M3', 'Opponent9_G2'],
    'Opponent11': ['Opponent11_M1', 'Opponent11_M2', 'Opponent11_D1', 'Opponent11_M3', 'Opponent11_M4', 'Opponent11_D2',
                   'Opponent11_D3', 'Opponent11_D4', 'Opponent11_G1', 'Opponent11_F1', 'Opponent11_F2', 'Opponent11_G2',
                   'Opponent11_D5', 'Opponent11_F3', 'Opponent11_D6', 'Opponent11_M5', 'Opponent11_D7', 'Opponent11_M6',
                   'Opponent11_F4', 'Opponent11_F5'],
    'Opponent3': ['Opponent3_D1', 'Opponent3_M1', 'Opponent3_D2', 'Opponent3_M2', 'Opponent3_F1', 'Opponent3_M3',
                  'Opponent3_M4', 'Opponent3_F2', 'Opponent3_D3', 'Opponent3_D4', 'Opponent3_G1', 'Opponent3_M5',
                  'Opponent3_F3', 'Opponent3_D5', 'Opponent3_F4', 'Opponent3_D6'],
    'Opponent12': ['Opponent12_D1', 'Opponent12_M1', 'Opponent12_M2', 'Opponent12_D2', 'Opponent12_M3', 'Opponent12_M4',
                   'Opponent12_D3', 'Opponent12_M5', 'Opponent12_D4', 'Opponent12_M6', 'Opponent12_G1', 'Opponent12_F1',
                   'Opponent12_M7', 'Opponent12_F2', 'Opponent12_D5', 'Opponent12_D6', 'Opponent12_D7',
                   'Opponent12_G2'],
    'Opponent6': ['Opponent6_F1', 'Opponent6_M1', 'Opponent6_M2', 'Opponent6_F2', 'Opponent6_D1', 'Opponent6_M3',
                  'Opponent6_M4', 'Opponent6_D2', 'Opponent6_D3', 'Opponent6_D4', 'Opponent6_G1', 'Opponent6_F3',
                  'Opponent6_D5', 'Opponent6_F4', 'Opponent6_M5', 'Opponent6_M6', 'Opponent6_F5', 'Opponent6_M7'],
    'Opponent18': ['Opponent18_M1', 'Opponent18_D1', 'Opponent18_M2', 'Opponent18_D2', 'Opponent18_D3', 'Opponent18_M3',
                   'Opponent18_F1', 'Opponent18_D4', 'Opponent18_M4', 'Opponent18_M5', 'Opponent18_F2', 'Opponent18_G1',
                   'Opponent18_F3', 'Opponent18_M6', 'Opponent18_M7', 'Opponent18_M8', 'Opponent14_F2'],
    'Opponent19': ['Opponent19_F1', 'Opponent19_M1', 'Opponent19_M2', 'Opponent19_D1', 'Opponent19_D2', 'Opponent19_M3',
                   'Opponent19_D3', 'Opponent19_D4', 'Opponent19_M4', 'Opponent19_G1', 'Opponent19_F2', 'Opponent19_F3',
                   'Opponent19_M5', 'Opponent19_M6', 'Opponent19_D5'],
    'Opponent2': ['Opponent2_F1', 'Opponent2_M1', 'Opponent2_D1', 'Opponent2_F2', 'Opponent2_D2', 'Opponent2_M2',
                  'Opponent2_M3', 'Opponent2_G1', 'Opponent2_D3', 'Opponent2_M4', 'Opponent2_D4', 'Opponent2_F3',
                  'Opponent2_D5', 'Opponent2_M5', 'Opponent2_D6', 'Opponent2_M6'],
    'Opponent15': ['Opponent15_M1', 'Opponent15_M2', 'Opponent15_D1', 'Opponent15_D2', 'Opponent15_F1', 'Opponent15_G1',
                   'Opponent15_D3', 'Opponent15_M3', 'Opponent15_D4', 'Opponent15_F2', 'Opponent15_F3', 'Opponent15_M4',
                   'Opponent15_F4', 'Opponent15_D5', 'Opponent15_M5', 'Opponent15_M6', 'Opponent15_D6', 'Opponent15_M7',
                   'Opponent15_M8'],
    'Opponent17': ['Opponent17_M1', 'Opponent17_D1', 'Opponent17_M2', 'Opponent17_M3', 'Opponent17_M4', 'Opponent17_D2',
                   'Opponent17_M5', 'Opponent17_D3', 'Opponent17_D4', 'Opponent17_F1', 'Opponent17_G1', 'Opponent17_F2',
                   'Opponent17_M6', 'Opponent17_F3', 'Opponent17_D5', 'Opponent17_F4', 'Opponent17_G2', 'Opponent17_M7',
                   'Opponent17_M8'],
    'Opponent5': ['Opponent5_F1', 'Opponent5_D1', 'Opponent5_M1', 'Opponent5_M2', 'Opponent5_M3', 'Opponent5_D2',
                  'Opponent5_M4', 'Opponent5_D3', 'Opponent5_F2', 'Opponent5_D4', 'Opponent5_G1', 'Opponent5_M5',
                  'Opponent5_M6', 'Opponent5_F3', 'Opponent5_D5', 'Opponent5_D6', 'Opponent5_D7', 'Opponent5_M7',
                  'Opponent5_D8'],
    'Huskies': ['Huskies_G1', 'Huskies_F1', 'Huskies_D1', 'Huskies_M1', 'Huskies_F2', 'Huskies_D2', 'Huskies_M2',
                'Huskies_M3', 'Huskies_D3', 'Huskies_D4', 'Huskies_F3', 'Huskies_D5', 'Huskies_M4', 'Huskies_M5',
                'Huskies_D6', 'Huskies_M6', 'Huskies_M7', 'Huskies_M8', 'Huskies_M9', 'Huskies_F4', 'Huskies_D7',
                'Huskies_M10', 'Huskies_M11', 'Huskies_M12', 'Huskies_M13', 'Huskies_F5', 'Huskies_F6', 'Huskies_D8',
                'Huskies_D9', 'Huskies_D10'],
    'Opponent1': ['Opponent1_D1', 'Opponent1_D2', 'Opponent1_M1', 'Opponent1_G1', 'Opponent1_F1', 'Opponent1_F2',
                  'Opponent1_D3', 'Opponent1_M2', 'Opponent1_F3', 'Opponent1_M3', 'Opponent1_D4', 'Opponent1_F4',
                  'Opponent1_F5', 'Opponent1_M4', 'Opponent1_D5', 'Opponent1_M5', 'Opponent1_D6', 'Opponent1_M6',
                  'Opponent1_F6'],
    'Opponent7': ['Opponent7_D1', 'Opponent7_M1', 'Opponent7_M2', 'Opponent7_G1', 'Opponent7_M3', 'Opponent7_M4',
                  'Opponent7_F1', 'Opponent7_M5', 'Opponent7_D2', 'Opponent7_D3', 'Opponent7_D4', 'Opponent7_F2',
                  'Opponent7_M6', 'Huskies_M8', 'Opponent7_M7'],
    'Opponent10': ['Opponent10_D1', 'Opponent10_M1', 'Opponent10_M2', 'Opponent10_D2', 'Opponent10_G1', 'Opponent10_D3',
                   'Opponent10_D4', 'Opponent10_F1', 'Opponent10_D5', 'Opponent10_M3', 'Opponent10_M4', 'Opponent10_F2',
                   'Opponent10_M5', 'Opponent10_F3', 'Opponent10_M6', 'Opponent10_M7', 'Opponent10_D6',
                   'Opponent10_F4']}

# events_dict = {}
# for i in range(59271):
#     q = full_data[i:i + 1]
#     if q['EventSubType'][i] != nan:
#         if q['EventType'][i] not in events_dict.keys():
#             events_dict[q['EventType'][i]] = []
#             events_dict[q['EventType'][i]].append(q['EventSubType'][i])
#         else:
#             if q['EventSubType'][i] not in events_dict[q['EventType'][i]]:
#                 events_dict[q['EventType'][i]].append(q['EventSubType'][i])
#     else:
#         events_dict[q['EventType'][i]] = []
# print(events_dict)
# result
events_dict = {'Interruption': ['Whistle', 'Ball out of the field'],
               'Goalkeeper leaving line': ['Goalkeeper leaving line'],
               'Offside': [],
               'Free Kick': ['Goal kick', 'Throw in', 'Free kick cross', 'Free Kick', 'Corner', 'Free kick shot',
                             'Penalty'],
               'Duel': ['Air duel', 'Ground loose ball duel', 'Ground defending duel', 'Ground attacking duel'],
               'Shot': ['Shot'],
               'Foul': ['Foul', 'Late card foul', 'Simulation', 'Protest', 'Hand foul', 'Violent Foul',
                        'Out of game foul', 'Time lost foul'],
               'Pass': ['Head pass', 'Simple pass', 'Launch', 'High pass', 'Hand pass', 'Smart pass', 'Cross'],
               'Save attempt': ['Save attempt', 'Reflexes'],
               'Substitution': ['Substitution'],
               'Others on the ball': ['Touch', 'Clearance', 'Acceleration']}


class member():
    def __init__(self, name):
        '''
        loseball: when the next event was not our team member do,the the last one who get the ball lose it
        :param name: name of member
        '''
        self.name = name
        self.events_dict = {'Offside': 0}
        self.press = 5.
        self.foal_counter = 0.
        self.loseball = 0
        for key in events_dict.keys():
            for ele in events_dict[key]:
                self.events_dict[ele] = 0


# create a object dict
member_statistics_object = {}
for key in member_statistics.keys():
    for ele in member_statistics[key]:
        if key not in member_statistics_object.keys():
            member_statistics_object[key] = {}
            member_statistics_object[key][ele] = member(ele)
        else:
            member_statistics_object[key][ele] = member(ele)
print(member_statistics_object['Huskies']['Huskies_F1'].name)

# define the foal_rate of Huskies
foal_rate_of_Huskies_dict = {}
for i in range(38):
    # initial the param
    foal_rate_of_Huskies_dict[i + 1] = {'press': 0, 'events_counter': 0.0000001, 'foal_counter': 0.,
                                        'foal_rate_list': []}
# foal_rate = foal_counter / events_counter

'''
1,positive action：
  Goal kick，Shot，Free kick shot，Penalty，Smart pass
2,negative action：
  Touch，/Foul，Corner，/Late card foul，/Protest，/Hand foul， /Violent Foul，  /Out of game foul，/Time lost foul，/Simulation
3,competitive action：
  EventType：Free Kick，Duel
  EventSubType：Air duel，Head pass，Ground loose ball duel，Simple pass，Launch，High pass，Ground defending duel，Free kick cross， Whistle
4,neutral action：
  EventType：Free Kick，Others on the ball，Goalkeeper leaving line，Save  attempt，Substitution，Interruption，Pass
'''
# define positive action
positive_action_list = ['Goal kick', 'Shot', 'Free kick shot', 'Penalty', 'Smart pass']
negative_action_list = ['Foul', 'Late card foul', 'Simulation', 'Protest', 'Hand foul', 'Violent Foul',
                        'Out of game foul', 'Time lost foul', 'Touch']
negative_counter = 0
positive_counter = 0
for i in range(59271):
    q = full_data[i:i + 1]
    foal_rate_of_Huskies_dict[q['MatchID'][i]]['events_counter'] += 1
    # record the press and the foal rate
    if q['TeamID'][i] == 'Huskies':
        if q['EventSubType'][i] in positive_action_list:
            positive_counter += 1
            foal_rate_of_Huskies_dict[q['MatchID'][i]]['press'] -= 0.01
            foal_rate_of_Huskies_dict[q['MatchID'][i]]['foal_rate_list'].append(
                [foal_rate_of_Huskies_dict[q['MatchID'][i]]['press'],
                 foal_rate_of_Huskies_dict[q['MatchID'][i]]['foal_counter'] / foal_rate_of_Huskies_dict[
                     q['MatchID'][i]]['events_counter'],  foal_rate_of_Huskies_dict[q['MatchID'][i]]['events_counter']])
            member_statistics_object[q['TeamID'][i]][q['OriginPlayerID'][i]].press -= 1
        if q['EventSubType'][i] in negative_action_list:
            negative_counter += 1
            foal_rate_of_Huskies_dict[q['MatchID'][i]]['press'] += 0.01
            foal_rate_of_Huskies_dict[q['MatchID'][i]]['foal_counter'] += 1
            foal_rate_of_Huskies_dict[q['MatchID'][i]]['foal_rate_list'].append(
                [foal_rate_of_Huskies_dict[q['MatchID'][i]]['press'],
                 foal_rate_of_Huskies_dict[q['MatchID'][i]]['foal_counter'] / foal_rate_of_Huskies_dict[
                     q['MatchID'][i]]['events_counter'], foal_rate_of_Huskies_dict[q['MatchID'][i]]['events_counter']])
            member_statistics_object[q['TeamID'][i]][q['OriginPlayerID'][i]].press += 1
            member_statistics_object[q['TeamID'][i]][q['OriginPlayerID'][i]].foal_counter += 1
        # record the loseball
        if full_data[i + 1: i + 2]['TeamID'][i + 1] != 'Huskies':
            member_statistics_object[q['TeamID'][i]][q['OriginPlayerID'][i]].loseball += 1
    else:
        if q['EventSubType'][i] in positive_action_list:
            negative_counter += 1
            foal_rate_of_Huskies_dict[q['MatchID'][i]]['press'] += 0.01
            foal_rate_of_Huskies_dict[q['MatchID'][i]]['foal_rate_list'].append(
                [foal_rate_of_Huskies_dict[q['MatchID'][i]]['press'],
                 foal_rate_of_Huskies_dict[q['MatchID'][i]]['foal_counter'] / foal_rate_of_Huskies_dict[
                     q['MatchID'][i]]['events_counter'], foal_rate_of_Huskies_dict[q['MatchID'][i]]['events_counter']])
            member_statistics_object[q['TeamID'][i]][q['OriginPlayerID'][i]].press -= 1
        if q['EventSubType'][i] in negative_action_list:
            positive_counter += 1
            foal_rate_of_Huskies_dict[q['MatchID'][i]]['press'] -= 0.01
            foal_rate_of_Huskies_dict[q['MatchID'][i]]['foal_rate_list'].append(
                [foal_rate_of_Huskies_dict[q['MatchID'][i]]['press'],
                 foal_rate_of_Huskies_dict[q['MatchID'][i]]['foal_counter'] / foal_rate_of_Huskies_dict[
                     q['MatchID'][i]]['events_counter'], foal_rate_of_Huskies_dict[q['MatchID'][i]]['events_counter']])
            member_statistics_object[q['TeamID'][i]][q['OriginPlayerID'][i]].press += 1
            member_statistics_object[q['TeamID'][i]][q['OriginPlayerID'][i]].foal_counter += 1
print('negative events times:', negative_counter)
print('positive events times:', positive_counter)
win_match = [1, 6, 11, 14, 15, 17, 18, 25, 27, 30, 31, 35, 36]
tie_match = [2, 8, 12, 16, 19, 20, 24, 33, 34, 37]
loss_match = [3, 4, 5, 7, 9, 10, 13, 21, 22, 23, 26, 28, 29, 32, 38]
X_win = []
Y_win = []
X_tie = []
Y_tie = []
X_loss = []
Y_loss = []
for i in range(38):
    q_for_press_foal = foal_rate_of_Huskies_dict[i + 1]['foal_rate_list']
    if i + 1 in win_match:
        for j in range(len(q_for_press_foal)):
            if j > 50:
                X_win.append(q_for_press_foal[j][0])
                Y_win.append(q_for_press_foal[j][1])
    elif i + 1 in tie_match:
        for j in range(len(q_for_press_foal)):
            if j > 50:
                X_tie.append(q_for_press_foal[j][0])
                Y_tie.append(q_for_press_foal[j][1])
    else:
        for j in range(len(q_for_press_foal)):
            if j > 50:
                X_loss.append(q_for_press_foal[j][0])
                Y_loss.append(q_for_press_foal[j][1])
plt.scatter(X_win, Y_win,c='b', marker= '.')
plt.show()
plt.scatter(X_tie, Y_tie,c='g', marker= '.')
plt.show()
plt.scatter(X_loss, Y_loss,c='r', marker= '.')
plt.show()

loseball_list = []
for mem in member_statistics['Huskies']:
    loseball_list.append(( member_statistics_object['Huskies'][mem].name, member_statistics_object['Huskies'][mem].loseball))
    print(member_statistics_object['Huskies'][mem].name, member_statistics_object['Huskies'][mem].loseball)
loseball_dict = dict(loseball_list)
# print(loseball_dict)