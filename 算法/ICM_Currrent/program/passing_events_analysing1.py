import numpy as np
from pylab import *
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import random

random.seed()

# read the data of passing events
passing_data = pd.read_csv(open('passingevents.csv'))
# read the data of matches
matches_data = pd.read_csv(open('matches.csv'))
# MatchID	TeamID	OriginPlayerID	DestinationPlayerID	MatchPeriod	EventTime	EventSubType
# EventOrigin_x	EventOrigin_y	EventDestination_x	EventDestination_y
# count the data amount of each match
match_times_dict = {}
datalenth = len(passing_data)
for i in range(datalenth):
    q = passing_data[i:i+1]
    if q['MatchID'][i] in match_times_dict.keys():
        match_times_dict[q['MatchID'][i]] += 1
    else:
        match_times_dict[q['MatchID'][i]] = 1
print(match_times_dict)
# check the total number whether is right
s = 0
for key in match_times_dict.keys():
    s += match_times_dict[key]
print(s)
# the result
# 23429

# find how many times of each match period
match_period_dict = {}
# define index finger
index_finger0 = 0
for key in match_times_dict.keys():
    match_period_dict[key] = {'1H_times': 0, '2H_times': 0}
    for i in range(match_times_dict[key]):
        if passing_data[index_finger0 + i:index_finger0 + i + 1]['MatchPeriod'][index_finger0 + i] == '1H':
            match_period_dict[key]['1H_times'] += 1
        else:
            match_period_dict[key]['2H_times'] += 1
    index_finger0 += match_times_dict[key]
print(index_finger0, match_period_dict)
# result

# member staristics
member_statistics = {}
for i in range(23429):
    if passing_data['TeamID'][i] not in member_statistics.keys():
        member_statistics[passing_data['TeamID'][i]] = []
    if passing_data['OriginPlayerID'][i] not in member_statistics[passing_data['TeamID'][i]]:
        member_statistics[passing_data['TeamID'][i]].append(passing_data['OriginPlayerID'][i])
print(member_statistics)

passing_member_statistics = {'Opponent17': ['Opponent17_M1', 'Opponent17_D1', 'Opponent17_M2', 'Opponent17_M3',
                                            'Opponent17_M4', 'Opponent17_D2', 'Opponent17_M5', 'Opponent17_D3',
                                            'Opponent17_D4', 'Opponent17_G1', 'Opponent17_F1', 'Opponent17_F2',
                                            'Opponent17_M6', 'Opponent17_F3', 'Opponent17_D5', 'Opponent17_F4',
                                            'Opponent17_M7', 'Opponent17_G2', 'Opponent17_M8'],
                             'Opponent13': ['Opponent13_M1', 'Opponent13_M2', 'Opponent13_D4', 'Opponent13_D2',
                                            'Opponent13_G1', 'Opponent13_D3', 'Opponent13_M4', 'Opponent13_M3',
                                            'Opponent13_M5', 'Opponent13_D1', 'Opponent13_F1', 'Opponent13_D5',
                                            'Opponent13_M6', 'Opponent13_F2', 'Opponent13_D6', 'Opponent13_M7',
                                            'Opponent13_G2', 'Opponent13_M8'],
                             'Opponent6': ['Opponent6_F1', 'Opponent6_M1', 'Opponent6_M3', 'Opponent6_M4',
                                           'Opponent6_D2',
                                           'Opponent6_D3', 'Opponent6_M2', 'Opponent6_D4', 'Opponent6_F2',
                                           'Opponent6_D1',
                                           'Opponent6_G1', 'Opponent6_D5', 'Opponent6_F4', 'Opponent6_F3',
                                           'Opponent6_M5',
                                           'Opponent6_M6', 'Opponent6_F5', 'Opponent6_M7'],
                             'Opponent10': ['Opponent10_M1', 'Opponent10_M2', 'Opponent10_D2', 'Opponent10_D4',
                                            'Opponent10_M4', 'Opponent10_D5', 'Opponent10_M3', 'Opponent10_D1',
                                            'Opponent10_G1', 'Opponent10_F1', 'Opponent10_D3', 'Opponent10_F2',
                                            'Opponent10_M5', 'Opponent10_F3', 'Opponent10_M7', 'Opponent10_D6',
                                            'Opponent10_M6', 'Opponent10_F4'],
                             'Opponent19': ['Opponent19_F1', 'Opponent19_D3', 'Opponent19_D2', 'Opponent19_M1',
                                            'Opponent19_M2', 'Opponent19_F2', 'Opponent19_M3', 'Opponent19_D1',
                                            'Opponent19_D4', 'Opponent19_M4', 'Opponent19_G1', 'Opponent19_F3',
                                            'Opponent19_M5', 'Opponent19_M6', 'Opponent19_D5'],
                             'Opponent16': ['Opponent16_D1', 'Opponent16_M1', 'Opponent16_D2', 'Opponent16_D4',
                                            'Opponent16_F2', 'Opponent16_M2', 'Opponent16_M3', 'Opponent16_D3',
                                            'Opponent16_F1', 'Opponent16_G1', 'Opponent16_F3', 'Opponent16_F4',
                                            'Opponent16_F5', 'Opponent16_F6', 'Opponent16_M4', 'Opponent13_D1',
                                            'Opponent16_D5', 'Opponent16_G2'],
                             'Opponent9': ['Opponent9_M1', 'Opponent9_F1', 'Opponent9_M2', 'Opponent9_M3',
                                           'Opponent9_D1', 'Opponent9_D2', 'Opponent9_G1', 'Opponent9_D3',
                                           'Opponent9_D4', 'Opponent9_F2', 'Opponent9_D5', 'Opponent9_M4',
                                           'Opponent9_M5', 'Opponent9_D6', 'Opponent9_F3', 'Opponent9_M6',
                                           'Opponent5_M3', 'Opponent9_G2'],
                             'Opponent14': ['Opponent14_D2', 'Opponent14_G1', 'Opponent14_F1', 'Opponent14_M2',
                                            'Opponent14_M1', 'Opponent14_D4', 'Opponent14_D3', 'Opponent14_D1',
                                            'Opponent14_M3', 'Opponent14_D5', 'Opponent14_F2', 'Opponent14_F3',
                                            'Opponent14_F4', 'Opponent14_D6', 'Opponent14_M4', 'Opponent14_M5',
                                            'Opponent14_G2', 'Opponent14_M6', 'Opponent14_D7'],
                             'Opponent1': ['Opponent1_D2', 'Opponent1_G1', 'Opponent1_D1', 'Opponent1_F2',
                                           'Opponent1_D3', 'Opponent1_M1', 'Opponent1_D4', 'Opponent1_M3',
                                           'Opponent1_F3', 'Opponent1_M2', 'Opponent1_F1', 'Opponent1_F5',
                                           'Opponent1_F4', 'Opponent1_M4', 'Opponent1_D6', 'Opponent1_M5',
                                           'Opponent1_M6', 'Opponent1_D5', 'Opponent1_F6'],
                             'Opponent8': ['Opponent8_M1', 'Opponent8_G1', 'Opponent8_D3', 'Opponent8_D4',
                                           'Opponent8_M4', 'Opponent8_M3', 'Opponent8_F1', 'Opponent8_M5',
                                           'Opponent8_M2', 'Opponent8_D1', 'Opponent8_D2', 'Opponent8_F2',
                                           'Opponent8_D5', 'Opponent8_F3', 'Opponent8_D6', 'Opponent8_D7',
                                           'Opponent8_M6', 'Opponent8_F5'],
                             'Opponent3': ['Opponent3_M1', 'Opponent3_M3', 'Opponent3_F1', 'Opponent3_M4',
                                           'Opponent3_D1', 'Opponent3_F2', 'Opponent3_D3', 'Opponent3_D4',
                                           'Opponent3_G1', 'Opponent3_D2', 'Opponent3_M2', 'Opponent3_M5',
                                           'Opponent3_F3', 'Opponent3_D5', 'Opponent3_F4', 'Opponent3_D6'],
                             'Opponent7': ['Opponent7_D1', 'Opponent7_M4', 'Opponent7_M3', 'Opponent7_G1',
                                           'Opponent7_D3', 'Opponent7_F1', 'Opponent7_M5', 'Opponent7_D2',
                                           'Opponent7_M2', 'Opponent7_M1', 'Opponent7_D4', 'Opponent7_F2',
                                           'Opponent7_M7', 'Opponent7_M6', 'Huskies_M8'],
                             'Opponent15': ['Opponent15_M1', 'Opponent15_M2', 'Opponent15_D1', 'Opponent15_D2',
                                            'Opponent15_G1', 'Opponent15_D3', 'Opponent15_M3', 'Opponent15_F2',
                                            'Opponent15_D4', 'Opponent15_F1', 'Opponent15_F3', 'Opponent15_M4',
                                            'Opponent15_F4', 'Opponent15_D5', 'Opponent15_M6', 'Opponent15_M5',
                                            'Opponent15_D6', 'Opponent15_M7', 'Opponent15_M8'],
                             'Opponent2': ['Opponent2_F1', 'Opponent2_M1', 'Opponent2_D1', 'Opponent2_D2',
                                           'Opponent2_M2', 'Opponent2_G1', 'Opponent2_D3', 'Opponent2_M3',
                                           'Opponent2_D4', 'Opponent2_F2', 'Opponent2_M4', 'Opponent2_F3',
                                           'Opponent2_D5', 'Opponent2_M5', 'Opponent2_D6', 'Opponent2_M6'],
                             'Opponent12': ['Opponent12_M1', 'Opponent12_M2', 'Opponent12_D2', 'Opponent12_M3',
                                            'Opponent12_M4', 'Opponent12_M5', 'Opponent12_D4', 'Opponent12_D3',
                                            'Opponent12_G1', 'Opponent12_D1', 'Opponent12_M6', 'Opponent12_M7',
                                            'Opponent12_F1', 'Opponent12_D5', 'Opponent12_F2', 'Opponent12_G2',
                                            'Opponent12_D6', 'Opponent12_D7'],
                             'Opponent11': ['Opponent11_M1', 'Opponent11_M2', 'Opponent11_D1', 'Opponent11_M3',
                                            'Opponent11_D3', 'Opponent11_D4', 'Opponent11_M4', 'Opponent11_G1',
                                            'Opponent11_F2', 'Opponent11_F1', 'Opponent11_D2', 'Opponent11_G2',
                                            'Opponent11_D5', 'Opponent11_F3', 'Opponent11_M5', 'Opponent11_D7',
                                            'Opponent11_D6', 'Opponent11_F5', 'Opponent11_F4', 'Opponent11_M6'],
                             'Opponent4': ['Opponent4_M1', 'Opponent4_D1', 'Opponent4_D2', 'Opponent4_D3',
                                           'Opponent4_D4', 'Opponent4_M3', 'Opponent4_M2', 'Opponent4_G1',
                                           'Opponent4_D5', 'Opponent4_M4', 'Opponent4_F1', 'Opponent4_M6',
                                           'Opponent4_F2', 'Opponent4_M5', 'Opponent4_D6', 'Opponent4_M7',
                                           'Opponent4_M8'],
                             'Opponent5': ['Opponent5_F1', 'Opponent5_M1', 'Opponent5_M2', 'Opponent5_D3',
                                           'Opponent5_F2', 'Opponent5_D4', 'Opponent5_D2', 'Opponent5_D1',
                                           'Opponent5_M4', 'Opponent5_M3', 'Opponent5_G1', 'Opponent5_M5',
                                           'Opponent5_M6', 'Opponent5_F3', 'Opponent5_D5', 'Opponent5_D6',
                                           'Opponent5_D7', 'Opponent5_M7'],
                             'Opponent18': ['Opponent18_M1', 'Opponent18_D2', 'Opponent18_D3', 'Opponent18_F1',
                                            'Opponent18_M2', 'Opponent18_M3', 'Opponent18_D1', 'Opponent18_M5',
                                            'Opponent18_M4', 'Opponent18_D4', 'Opponent18_F2', 'Opponent18_G1',
                                            'Opponent18_F3', 'Opponent18_M6', 'Opponent18_M7', 'Opponent18_M8',
                                            'Opponent14_F2'],
                             'Huskies': ['Huskies_D1', 'Huskies_M1', 'Huskies_M2', 'Huskies_G1', 'Huskies_D2',
                                         'Huskies_D3', 'Huskies_D4', 'Huskies_M3', 'Huskies_F2', 'Huskies_F3',
                                         'Huskies_F1', 'Huskies_D5', 'Huskies_M4', 'Huskies_M5', 'Huskies_D6',
                                         'Huskies_M6', 'Huskies_M7', 'Huskies_M8', 'Huskies_M9', 'Huskies_F4',
                                         'Huskies_D7', 'Huskies_M10', 'Huskies_M11', 'Huskies_M12', 'Huskies_M13',
                                         'Huskies_F5', 'Huskies_F6', 'Huskies_D8', 'Huskies_D9', 'Huskies_D10']}
# get envents subtype keys
events_subtype = []
for i in range(23429):
    if passing_data['EventSubType'][i] not in events_subtype:
        events_subtype.append(passing_data['EventSubType'][i])
print(events_subtype)


# ----------------------------------------------------------------------------------------------------------------------
# 创建了传球类，统计每个对象传球类型的次数
# define a class passer to count the individual's record
class passer():
    def __init__(self, name):
        self.name = name
        self.test = 'is passer class'
        self.pass_dict = {'Head pass': 0, 'Simple pass': 0, 'Launch': 0, 'High pass': 0,
                          'Hand pass': 0, 'Smart pass': 0, 'Cross': 0}
        self.pass_longist_distance = 0
        self.pass_total_distance = 0


# define function to calculate the distance of pass
def distance(ori_x, ori_y, desti_x, desti_y):
    return np.sqrt((ori_x - desti_x) ** 2 + (ori_y - desti_y) ** 2)


# create the passer object of each member
for key in passing_member_statistics:
    q_list = []
    for i in range(len(passing_member_statistics[key])):
        q_list.append(passer(passing_member_statistics[key][i]))
    passing_member_statistics[key] = dict(zip(passing_member_statistics[key], q_list))
# # for check
# print(passing_member_statistics['Huskies']['Huskies_F5'].name)

for i in range(23429):
    q = passing_data[i:i + 1]
    passing_member_statistics[q['TeamID'][i]][q['OriginPlayerID'][i]].pass_dict[q['EventSubType'][i]] += 1
# for check
print(passing_member_statistics['Huskies']['Huskies_D1'].pass_dict)
dict_of_total_pass = {}
for team in passing_member_statistics.keys():
    dict_of_total_pass[team] = passer(team)
    for member in passing_member_statistics[team]:
        # print('team:', team, '\t', 'member:', member, passing_member_statistics[team][member].pass_dict)
        for key in passing_member_statistics[team][member].pass_dict:
            dict_of_total_pass[team].pass_dict[key] += passing_member_statistics[team][member].pass_dict[key]

for ele in dict_of_total_pass.keys():
    print(dict_of_total_pass[ele].name, ':',dict_of_total_pass[ele].pass_dict )

# ----------------------------------------------------------------------------------------------------------------------


# labels for  simple learning model
# # define winner/loss dict (just change the phase after if and after loss
# winner_dict = {}
# for i in range(38):
#     if matches_data['Outcome'][i] == 'win':
#         winner_dict[i + 1] = 'Huskies'
#     elif matches_data['Outcome'][i] == 'loss':
#         winner_dict[i + 1] = matches_data['OpponentID'][i]
#     else:
#         winner_dict[i + 1] = 'tie'
# print(winner_dict)
# result
winner_dict = {1: 'Huskies', 2: 'tie', 3: 'Opponent3', 4: 'Opponent4', 5: 'Opponent5', 6: 'Huskies',
               7: 'Opponent7', 8: 'tie', 9: 'Opponent9', 10: 'Opponent10', 11: 'Huskies', 12: 'tie',
               13: 'Opponent13', 14: 'Huskies', 15: 'Huskies', 16: 'tie', 17: 'Huskies', 18: 'Huskies',
               19: 'tie', 20: 'tie', 21: 'Opponent6', 22: 'Opponent5', 23: 'Opponent4', 24: 'tie',
               25: 'Huskies', 26: 'Opponent9', 27: 'Huskies', 28: 'Opponent11', 29: 'Opponent7',
               30: 'Huskies', 31: 'Huskies', 32: 'Opponent2', 33: 'tie', 34: 'tie', 35: 'Huskies',
               36: 'Huskies', 37: 'tie', 38: 'Opponent14'}
losser_dict = {1: 'Opponent1', 2: 'tie', 3: 'Huskies', 4: 'Huskies', 5: 'Huskies',
               6: 'Opponent6', 7: 'Huskies', 8: 'tie', 9: 'Huskies', 10: 'Huskies',
               11: 'Opponent11', 12: 'tie', 13: 'Huskies', 14: 'Opponent14', 15: 'Opponent15',
               16: 'tie', 17: 'Opponent17', 18: 'Opponent18', 19: 'tie', 20: 'tie',
               21: 'Huskies', 22: 'Huskies', 23: 'Huskies', 24: 'tie', 25: 'Opponent10',
               26: 'Huskies', 27: 'Opponent12', 28: 'Huskies', 29: 'Huskies', 30: 'Opponent8',
               31: 'Opponent1', 32: 'Huskies', 33: 'tie', 34: 'tie', 35: 'Opponent17',
               36: 'Opponent15', 37: 'tie', 38: 'Huskies'}

# the total times of pass in 1H of winner/losser (just change the dict in winner_dict or losser_dict,
# and the condition of tie)
dict_of_pass_time_in_1H = {i+1:0 for i in range(38)}
for i_0 in range(23429):
    q = passing_data[i_0:i_0+1]
    if q['TeamID'][i_0] == winner_dict[q['MatchID'][i_0]] and q['MatchPeriod'][i_0] == '1H':
        dict_of_pass_time_in_1H[q['MatchID'][i_0]] += 1
    elif winner_dict[q['MatchID'][i_0]] == 'tie' and q['TeamID'][i_0] == 'Huskies' and q['MatchPeriod'][i_0] == '1H':
        dict_of_pass_time_in_1H[q['MatchID'][i_0]] += 1
print(dict_of_pass_time_in_1H)
# result
dict_of_pass_time_in_1H = {1: 222, 2: 104, 3: 210, 4: 165, 5: 234, 6: 192, 7: 115, 8: 186,
                           9: 286, 10: 133, 11: 115, 12: 69, 13: 284, 14: 200, 15: 119,
                           16: 44, 17: 211, 18: 177, 19: 135, 20: 136, 21: 104, 22: 234,
                           23: 198, 24: 167, 25: 139, 26: 238, 27: 174, 28: 145, 29: 164,
                           30: 180, 31: 158, 32: 375, 33: 99, 34: 209, 35: 243, 36: 192,
                           37: 138, 38: 227}
dict_of_pass_time_in_1H_losser = {1: 97, 2: 186, 3: 209, 4: 176, 5: 196, 6: 176, 7: 170, 8: 159,
                                  9: 80, 10: 195, 11: 165, 12: 225, 13: 114, 14: 168, 15: 130,
                                  16: 312, 17: 197, 18: 162, 19: 312, 20: 132, 21: 232, 22: 145,
                                  23: 115, 24: 82, 25: 137, 26: 106, 27: 78, 28: 113, 29: 96, 30: 65,
                                  31: 123, 32: 40, 33: 266, 34: 182, 35: 106, 36: 157, 37: 177, 38: 108}

# the total times of pass in 2H of winner下半场获胜方传球总次数
dict_of_pass_time_in_2H = {i+1:0 for i in range(38)}
for i_0 in range(23429):
    q = passing_data[i_0:i_0+1]
    if q['TeamID'][i_0] == winner_dict[q['MatchID'][i_0]] and q['MatchPeriod'][i_0] == '2H':
        dict_of_pass_time_in_2H[q['MatchID'][i_0]] += 1
    elif winner_dict[q['MatchID'][i_0]] == 'tie' and q['TeamID'][i_0] == 'Huskies' and q['MatchPeriod'][i_0] == '2H':
        dict_of_pass_time_in_2H[q['MatchID'][i_0]] += 1
print(dict_of_pass_time_in_2H)
# result
dict_of_pass_time_in_2H = {1: 147, 2: 76, 3: 261, 4: 180, 5: 139, 6: 126, 7: 64,
                           8: 109, 9: 215, 10: 81, 11: 68, 12: 63, 13: 220,
                           14: 147, 15: 152, 16: 36, 17: 93, 18: 135, 19: 113,
                           20: 94, 21: 100, 22: 242, 23: 275, 24: 153, 25: 110,
                           26: 185, 27: 109, 28: 115, 29: 91, 30: 132, 31: 171,
                           32: 502, 33: 108, 34: 127, 35: 104, 36: 110, 37: 155,
                           38: 128}
dict_of_pass_time_in_2H_losser = {1: 100, 2: 230, 3: 115, 4: 178, 5: 186, 6: 118, 7: 214,
                                  8: 118, 9: 88, 10: 164, 11: 152, 12: 201, 13: 133, 14: 179,
                                  15: 94, 16: 293, 17: 165, 18: 140, 19: 186, 20: 98, 21: 134,
                                  22: 94, 23: 121, 24: 104, 25: 136, 26: 181, 27: 142, 28: 125,
                                  29: 124, 30: 107, 31: 92, 32: 69, 33: 180, 34: 111, 35: 134,
                                  36: 141, 37: 69, 38: 167}

# 上半场胜方传球总距离
dict_of_pass_distance_total_in_1H = {i + 1: 0 for i in range(38)}
for i in range(23429):
    q = passing_data[i:i + 1]
    if q['TeamID'][i] == winner_dict[q['MatchID'][i]] and q['MatchPeriod'][i] == '1H':
        dict_of_pass_distance_total_in_1H[q['MatchID'][i]] += \
            distance(q['EventOrigin_x'][i], q['EventOrigin_y'][i], q['EventDestination_x'][i],
                     q['EventDestination_y'][i])
    elif winner_dict[q['MatchID'][i]] == 'tie' and q['TeamID'][i] == 'Huskies' and q['MatchPeriod'][i] == '1H':
        dict_of_pass_distance_total_in_1H[q['MatchID'][i]] += \
            distance(q['EventOrigin_x'][i], q['EventOrigin_y'][i], q['EventDestination_x'][i],
                     q['EventDestination_y'][i])
print(dict_of_pass_distance_total_in_1H)
# result
dict_of_pass_distance_total_in_1H = {1: 5597.194401219097, 2: 2430.9166831688362, 3: 4917.3160412761499,
                                     4: 3954.0718646354649, 5: 5455.5508827183321, 6: 4550.401485633126,
                                     7: 2904.9352973349269, 8: 4563.1658154723555, 9: 6179.981661406202,
                                     10: 3448.6967840619118, 11: 2731.2398248812897, 12: 1724.8835206341985,
                                     13: 6289.4269221480799, 14: 5175.7038018265976, 15: 2786.0334470778648,
                                     16: 1030.6865043805801, 17: 5293.2127208535167, 18: 4069.2767090371235,
                                     19: 3349.0722248159454, 20: 3261.4859213216605, 21: 2027.0879429770077,
                                     22: 5429.493836745718, 23: 4373.5773579503366, 24: 3614.562040900074,
                                     25: 3485.0335115213879, 26: 4991.7629059409937, 27: 4513.0215668757919,
                                     28: 3448.7446848139298, 29: 4140.9033640578509, 30: 4254.9475673593815,
                                     31: 3526.6179136022029, 32: 7625.9421321936215, 33: 2651.9692334448237,
                                     34: 5175.7880606766985, 35: 5756.9852090698114, 36: 4583.7091315501484,
                                     37: 3767.3357496750814, 38: 5063.7879824979736}
dict_of_pass_distance_total_in_1H_losser = {1: 2477.5289002272739, 2: 4320.2165626848737, 3: 4753.8814212369525,
                                            4: 4728.283765154024, 5: 4317.2243776998748, 6: 4193.7028407062553,
                                            7: 4246.4067239157339, 8: 3857.1562261446988, 9: 1865.4184364674381,
                                            10: 4538.6643680802626, 11: 3785.6058076832755, 12: 5031.6512614874691,
                                            13: 2767.0507722476891, 14: 3941.8647454509323, 15: 3309.7854180584595,
                                            16: 7744.1838596432935, 17: 4443.1471088748594, 18: 3546.4971044233616,
                                            19: 7320.2380683947895, 20: 3122.5790887913763, 21: 5435.3954180562869,
                                            22: 3257.0240315493083, 23: 2509.570270588189, 24: 1858.0764383470428,
                                            25: 3302.9583601988529, 26: 2574.1000893367336, 27: 1825.8070615365523,
                                            28: 2639.3077038907095, 29: 2285.113909924069, 30: 1471.9460690018743,
                                            31: 2666.1684237569038, 32: 979.45079678528327, 33: 6388.9725411566169,
                                            34: 4324.1046422834543, 35: 2040.8095880115372, 36: 3592.6603256099338,
                                            37: 4353.736158707954, 38: 2355.2240130720938}

# 下半场胜方/败方传球总距离
dict_of_pass_distance_total_in_2H = {i + 1: 0 for i in range(38)}
for i in range(23429):
    q = passing_data[i:i + 1]
    if q['TeamID'][i] == winner_dict[q['MatchID'][i]] and q['MatchPeriod'][i] == '2H':
        dict_of_pass_distance_total_in_2H[q['MatchID'][i]] += \
            distance(q['EventOrigin_x'][i], q['EventOrigin_y'][i], q['EventDestination_x'][i],
                     q['EventDestination_y'][i])
    elif winner_dict[q['MatchID'][i]] == 'tie' and q['TeamID'][i] == 'Huskies' and q['MatchPeriod'][i] == '2H':
        dict_of_pass_distance_total_in_2H[q['MatchID'][i]] += \
            distance(q['EventOrigin_x'][i], q['EventOrigin_y'][i], q['EventDestination_x'][i],
                     q['EventDestination_y'][i])
print(dict_of_pass_distance_total_in_2H)
# result
dict_of_pass_distance_total_in_2H = {1: 3447.080364039, 2: 1782.6317114995959, 3: 5887.5032300429266,
                                     4: 4200.4644316714312, 5: 2711.6990620699216, 6: 3263.3278539713288,
                                     7: 1526.9423504405368, 8: 2887.0855584679312, 9: 4701.622398992552,
                                     10: 2030.4733793535081, 11: 1608.1822962726662, 12: 1554.3007212746597,
                                     13: 4524.0944479895697, 14: 3227.1970118478739, 15: 3521.4797783414665,
                                     16: 816.33180898626483, 17: 2187.5540577554707, 18: 3035.5656180775663,
                                     19: 2584.3983253722895, 20: 2155.0632052387446, 21: 1794.3901733117475,
                                     22: 5302.8582303550311, 23: 6313.1669489860333, 24: 3532.2985695083216,
                                     25: 2374.489944560798, 26: 4004.5112708014685, 27: 2784.2880139598565,
                                     28: 2656.7678631344729, 29: 2465.9793438459405, 30: 3103.7977396435699,
                                     31: 3878.012630127751, 32: 10097.310680269864, 33: 2714.6924948581063,
                                     34: 3098.6661892562897, 35: 2351.7144171182154, 36: 2669.2114606556029,
                                     37: 3624.6262902350445, 38: 2831.8040422375407}
dict_of_pass_distance_total_in_2H_losser = {1: 2471.2273276109527, 2: 5911.4483536973239, 3: 2522.5313746149436,
                                            4: 5001.2350313182587, 5: 4380.2161367383305, 6: 2791.5907830366505,
                                            7: 5273.3149904354705, 8: 2611.4603658884935, 9: 1861.0302977485378,
                                            10: 3828.0710307341005, 11: 3536.3078541687369, 12: 4122.4255228751126,
                                            13: 3377.5575788365995, 14: 4343.5556107341345, 15: 2207.3470342935902,
                                            16: 7599.6572957547496, 17: 3935.8976642682555, 18: 2923.9905788549372,
                                            19: 4115.062438805483, 20: 2405.4123050669182, 21: 3309.7222430111688,
                                            22: 2155.3674842924493, 23: 2600.0086253723657, 24: 2446.4914081957145,
                                            25: 3223.1205733957272, 26: 4520.1631058681533, 27: 3142.7691337258102,
                                            28: 3216.354748959563, 29: 2887.929187926763, 30: 2452.1965479904384,
                                            31: 2045.7225384462001, 32: 1754.0120692209036, 33: 4318.4807663921874,
                                            34: 2661.2459520388825, 35: 3301.6940490506322, 36: 3289.3581319081995,
                                            37: 1516.6536788779117, 38: 3837.8267365243455}

# 胜方不同传球类型的次数
# 'Head pass'
dict_of_head_pass_time = {i + 1: 0 for i in range(38)}
for i in range(23429):
    q = passing_data[i:i + 1]
    if q['TeamID'][i] == winner_dict[q['MatchID'][i]] and q['EventSubType'][i] == 'Head pass':
        dict_of_head_pass_time[q['MatchID'][i]] += 1
    elif winner_dict[q['MatchID'][i]] == 'tie' and q['TeamID'][i] == 'Huskies' and q['EventSubType'][i] == 'Head pass':
        dict_of_head_pass_time[q['MatchID'][i]] += 1
print(dict_of_head_pass_time)
# result
dict_of_head_pass_time = {1: 13, 2: 10, 3: 12, 4: 22, 5: 14, 6: 14, 7: 16, 8: 11, 9: 27, 10: 16,
                          11: 11, 12: 6, 13: 12, 14: 11, 15: 20, 16: 6, 17: 18, 18: 18, 19: 18,
                          20: 13, 21: 14, 22: 13, 23: 19, 24: 23, 25: 27, 26: 12, 27: 11, 28: 14,
                          29: 20, 30: 20, 31: 17, 32: 19, 33: 11, 34: 15, 35: 14, 36: 25, 37: 14, 38: 11}
dict_of_head_pass_time_losser = {1: 14, 2: 14, 3: 4, 4: 17, 5: 16, 6: 17, 7: 28, 8: 12, 9: 11, 10: 13,
                                 11: 22, 12: 16, 13: 18, 14: 14, 15: 12, 16: 25, 17: 19, 18: 13, 19: 13,
                                 20: 16, 21: 19, 22: 11, 23: 11, 24: 16, 25: 11, 26: 9, 27: 14, 28: 22,
                                 29: 24, 30: 12, 31: 15, 32: 4, 33: 23, 34: 17, 35: 22, 36: 12, 37: 11, 38: 19}

# 'Simple pass'
dict_of_simple_pass_time = {i + 1: 0 for i in range(38)}
for i in range(23429):
    q = passing_data[i:i + 1]
    if q['TeamID'][i] == winner_dict[q['MatchID'][i]] and q['EventSubType'][i] == 'Simple pass':
        dict_of_simple_pass_time[q['MatchID'][i]] += 1
    elif winner_dict[q['MatchID'][i]] == 'tie' and q['TeamID'][i] == 'Huskies' and q['EventSubType'][i] == 'Simple pass':
        dict_of_simple_pass_time[q['MatchID'][i]] += 1
print(dict_of_simple_pass_time)
# result
dict_of_simple_pass_time = {1: 329, 2: 150, 3: 430, 4: 281, 5: 338, 6: 267, 7: 140, 8: 261, 9: 437, 10: 168,
                            11: 145, 12: 114, 13: 463, 14: 297, 15: 215, 16: 62, 17: 267, 18: 275, 19: 192,
                            20: 179, 21: 177, 22: 438, 23: 418, 24: 272, 25: 179, 26: 391, 27: 241, 28: 228,
                            29: 202, 30: 265, 31: 282, 32: 825, 33: 177, 34: 274, 35: 301, 36: 232, 37: 255, 38: 319}
dict_of_simple_pass_time_losser = {1: 149, 2: 374, 3: 294, 4: 296, 5: 342, 6: 246, 7: 326, 8: 231, 9: 139, 10: 313,
                                   11: 255, 12: 377, 13: 199, 14: 310, 15: 200, 16: 535, 17: 305, 18: 275, 19: 461,
                                   20: 184, 21: 300, 22: 205, 23: 185, 24: 140, 25: 242, 26: 241, 27: 182, 28: 180,
                                   29: 168, 30: 147, 31: 180, 32: 87, 33: 387, 34: 258, 35: 182, 36: 267, 37: 210,
                                   38: 229}

# 'Launch'
dict_of_launch_pass_time = {i + 1: 0 for i in range(38)}
for i in range(23429):
    q = passing_data[i:i + 1]
    if q['TeamID'][i] == winner_dict[q['MatchID'][i]] and q['EventSubType'][i] == 'Launch':
        dict_of_launch_pass_time[q['MatchID'][i]] += 1
    elif winner_dict[q['MatchID'][i]] == 'tie' and q['TeamID'][i] == 'Huskies' and q['EventSubType'][i] == 'Launch':
        dict_of_launch_pass_time[q['MatchID'][i]] += 1
print(dict_of_launch_pass_time)
# result
dict_of_launch_pass_time = {1: 1, 2: 4, 3: 5, 4: 1, 5: 1, 6: 1, 7: 5, 8: 1, 9: 7, 10: 7, 11: 9, 12: 2,
                            13: 2, 14: 8, 15: 12, 16: 4, 17: 6, 18: 3, 19: 17, 20: 2, 21: 2, 22: 1, 23: 4,
                            24: 4, 25: 7, 26: 2, 27: 2, 28: 1, 29: 6, 30: 6, 31: 4, 32: 0, 33: 4, 34: 11,
                            35: 1, 36: 10, 37: 3, 38: 3}
dict_of_launch_pass_time_losser = {1: 5, 2: 3, 3: 6, 4: 6, 5: 8, 6: 1, 7: 5, 8: 12, 9: 2, 10: 5, 11: 14,
                                   12: 7, 13: 11, 14: 2, 15: 1, 16: 3, 17: 13, 18: 3, 19: 1, 20: 3, 21: 17,
                                   22: 2, 23: 2, 24: 15, 25: 0, 26: 5, 27: 2, 28: 5, 29: 11, 30: 1, 31: 8,
                                   32: 2, 33: 10, 34: 1, 35: 4, 36: 2, 37: 5, 38: 3}

# 'High pass'
dict_of_high_pass_time = {i + 1: 0 for i in range(38)}
for i in range(23429):
    q = passing_data[i:i + 1]
    if q['TeamID'][i] == winner_dict[q['MatchID'][i]] and q['EventSubType'][i] == 'High pass':
        dict_of_high_pass_time[q['MatchID'][i]] += 1
    elif winner_dict[q['MatchID'][i]] == 'tie' and q['TeamID'][i] == 'Huskies' and q['EventSubType'][i] == 'High pass':
        dict_of_high_pass_time[q['MatchID'][i]] += 1
print(dict_of_high_pass_time)
# result
dict_of_high_pass_time = {1: 15, 2: 14, 3: 11, 4: 19, 5: 12, 6: 22, 7: 14, 8: 14, 9: 17, 10: 16, 11: 12,
                          12: 6, 13: 14, 14: 24, 15: 12, 16: 5, 17: 9, 18: 14, 19: 12, 20: 24, 21: 1,
                          22: 11, 23: 14, 24: 14, 25: 22, 26: 7, 27: 22, 28: 9, 29: 13, 30: 14, 31: 10,
                          32: 17, 33: 12, 34: 26, 35: 19, 36: 24, 37: 14, 38: 12}
dict_of_high_pass_time_losser = {1: 18, 2: 9, 3: 13, 4: 16, 5: 8, 6: 19, 7: 10, 8: 13, 9: 8, 10: 18,
                                 11: 13, 12: 14, 13: 15, 14: 14, 15: 9, 16: 25, 17: 17, 18: 10, 19: 13,
                                 20: 13, 21: 19, 22: 10, 23: 28, 24: 10, 25: 11, 26: 21, 27: 10, 28: 22,
                                 29: 9, 30: 4, 31: 10, 32: 13, 33: 15, 34: 8, 35: 21, 36: 12, 37: 15, 38: 16}

# 'Hand pass'
dict_of_hand_pass_time = {i + 1: 0 for i in range(38)}
for i in range(23429):
    q = passing_data[i:i + 1]
    if q['TeamID'][i] == winner_dict[q['MatchID'][i]] and q['EventSubType'][i] == 'Hand pass':
        dict_of_hand_pass_time[q['MatchID'][i]] += 1
    elif winner_dict[q['MatchID'][i]] == 'tie' and q['TeamID'][i] == 'Huskies' and q['EventSubType'][i] == 'Hand pass':
        dict_of_hand_pass_time[q['MatchID'][i]] += 1
print(dict_of_hand_pass_time)
# result
dict_of_hand_pass_time = {1: 4, 2: 1, 3: 5, 4: 7, 5: 1, 6: 1, 7: 1, 8: 6, 9: 4, 10: 1, 11: 1, 12: 0,
                          13: 3, 14: 1, 15: 4, 16: 2, 17: 2, 18: 1, 19: 4, 20: 10, 21: 5, 22: 2, 23: 4,
                          24: 4, 25: 8, 26: 4, 27: 1, 28: 1, 29: 5, 30: 0, 31: 5, 32: 3, 33: 0, 34: 4,
                          35: 9, 36: 6, 37: 4, 38: 3}
dict_of_hand_pass_time_losser = {1: 3, 2: 4, 3: 7, 4: 6, 5: 4, 6: 4, 7: 3, 8: 3, 9: 3, 10: 1, 11: 5,
                                 12: 1, 13: 3, 14: 2, 15: 2, 16: 5, 17: 2, 18: 1, 19: 6, 20: 4, 21: 5,
                                 22: 5, 23: 4, 24: 2, 25: 5, 26: 3, 27: 1, 28: 2, 29: 0, 30: 4, 31: 0,
                                 32: 1, 33: 3, 34: 4, 35: 4, 36: 5, 37: 1, 38: 2}

# 'Smart pass'
dict_of_smart_pass_time = {i + 1: 0 for i in range(38)}
for i in range(23429):
    q = passing_data[i:i + 1]
    if q['TeamID'][i] == winner_dict[q['MatchID'][i]] and q['EventSubType'][i] == 'Smart pass':
        dict_of_smart_pass_time[q['MatchID'][i]] += 1
    elif winner_dict[q['MatchID'][i]] == 'tie' and q['TeamID'][i] == 'Huskies' and q['EventSubType'][i] == 'Smart pass':
        dict_of_smart_pass_time[q['MatchID'][i]] += 1
print(dict_of_smart_pass_time)
# result
dict_of_smart_pass_time = {1: 2, 2: 0, 3: 5, 4: 5, 5: 4, 6: 7, 7: 0, 8: 1, 9: 2, 10: 1, 11: 3, 12: 1, 13: 7,
                           14: 1, 15: 6, 16: 1, 17: 0, 18: 1, 19: 0, 20: 1, 21: 0, 22: 7, 23: 8, 24: 1, 25: 2,
                           26: 5, 27: 2, 28: 2, 29: 4, 30: 3, 31: 5, 32: 5, 33: 0, 34: 2, 35: 1, 36: 4, 37: 0, 38: 2}
dict_of_smart_pass_time_losser = {1: 3, 2: 5, 3: 0, 4: 3, 5: 2, 6: 4, 7: 0, 8: 1, 9: 1, 10: 2, 11: 4, 12: 8, 13: 0,
                                  14: 2, 15: 0, 16: 4, 17: 1, 18: 0, 19: 2, 20: 2, 21: 3, 22: 1, 23: 5, 24: 1,
                                  25: 0, 26: 3, 27: 6, 28: 1, 29: 1, 30: 1, 31: 2, 32: 2, 33: 5, 34: 1, 35: 5,
                                  36: 0, 37: 3, 38: 5}

# 'Cross'
dict_of_cross_pass_time = {i + 1: 0 for i in range(38)}
for i in range(23429):
    q = passing_data[i:i + 1]
    if q['TeamID'][i] == losser_dict[q['MatchID'][i]] and q['EventSubType'][i] == 'Cross':
        dict_of_cross_pass_time[q['MatchID'][i]] += 1
    elif losser_dict[q['MatchID'][i]] == 'tie' and q['TeamID'][i] != 'Huskies' and q['EventSubType'][i] == 'Cross':
        dict_of_cross_pass_time[q['MatchID'][i]] += 1
print(dict_of_cross_pass_time)
# result
dict_of_cross_pass_time = {1: 5, 2: 1, 3: 3, 4: 10, 5: 3, 6: 6, 7: 3, 8: 1, 9: 7, 10: 5, 11: 2,
                           12: 3, 13: 3, 14: 5, 15: 2, 16: 0, 17: 2, 18: 0, 19: 5, 20: 1, 21: 5,
                           22: 4, 23: 6, 24: 2, 25: 4, 26: 2, 27: 4, 28: 5, 29: 5, 30: 4, 31: 6,
                           32: 8, 33: 3, 34: 4, 35: 2, 36: 1, 37: 3, 38: 5}
dict_of_cross_pass_time_losser = {1: 5, 2: 7, 3: 0, 4: 10, 5: 2, 6: 3, 7: 12, 8: 5, 9: 4, 10: 7,
                                  11: 4, 12: 3, 13: 1, 14: 3, 15: 0, 16: 8, 17: 5, 18: 0, 19: 2,
                                  20: 8, 21: 3, 22: 5, 23: 1, 24: 2, 25: 4, 26: 5, 27: 5, 28: 6,
                                  29: 7, 30: 3, 31: 0, 32: 0, 33: 3, 34: 4, 35: 2, 36: 0, 37: 1, 38: 1}

# creat a training set of winner data and losser data
# [pass_time_in_1H, pass_time_in_2H, pass_distance_total_in_1H,pass_distance_total_in_2H,head_pass_time,
# simple_pass_time,launch_pass_time, high_pass_time,hand_pass_time,smart_pass_time,cross_pass_time]
# 1 or -1 is a indicator to identified whether the match is win or loss
winner_learning_data = [[[], 1] for i in range(38)]
losser_learning_data = [[[], -1] for i in range(38)]
for i in range(38):
    winner_learning_data[i][0].append(dict_of_pass_time_in_1H[i + 1])
    winner_learning_data[i][0].append(dict_of_pass_time_in_2H[i + 1])
    winner_learning_data[i][0].append(dict_of_pass_distance_total_in_1H[i + 1])
    winner_learning_data[i][0].append(dict_of_pass_distance_total_in_2H[i + 1])
    winner_learning_data[i][0].append(dict_of_head_pass_time[i + 1])
    winner_learning_data[i][0].append(dict_of_simple_pass_time[i + 1])
    winner_learning_data[i][0].append(dict_of_launch_pass_time[i + 1])
    winner_learning_data[i][0].append(dict_of_high_pass_time[i + 1])
    winner_learning_data[i][0].append(dict_of_hand_pass_time[i + 1])
    winner_learning_data[i][0].append(dict_of_smart_pass_time[i + 1])
    winner_learning_data[i][0].append(dict_of_cross_pass_time[i + 1])

    losser_learning_data[i][0].append(dict_of_pass_time_in_1H_losser[i + 1])
    losser_learning_data[i][0].append(dict_of_pass_time_in_2H_losser[i + 1])
    losser_learning_data[i][0].append(dict_of_pass_distance_total_in_1H_losser[i + 1])
    losser_learning_data[i][0].append(dict_of_pass_distance_total_in_2H_losser[i + 1])
    losser_learning_data[i][0].append(dict_of_head_pass_time_losser[i + 1])
    losser_learning_data[i][0].append(dict_of_simple_pass_time_losser[i + 1])
    losser_learning_data[i][0].append(dict_of_launch_pass_time_losser[i + 1])
    losser_learning_data[i][0].append(dict_of_high_pass_time_losser[i + 1])
    losser_learning_data[i][0].append(dict_of_hand_pass_time_losser[i + 1])
    losser_learning_data[i][0].append(dict_of_smart_pass_time_losser[i + 1])
    losser_learning_data[i][0].append(dict_of_cross_pass_time_losser[i + 1])
print(winner_learning_data, '\n', losser_learning_data)
# result
winner_learning_data = [[[222, 147, 5597.194401219097, 3447.080364039, 13, 329, 1, 15, 4, 2, 5], 1],
                        [[104, 76, 2430.9166831688362, 1782.631711499596, 10, 150, 4, 14, 1, 0, 1], 1],
                        [[210, 261, 4917.31604127615, 5887.503230042927, 12, 430, 5, 11, 5, 5, 3], 1],
                        [[165, 180, 3954.071864635465, 4200.464431671431, 22, 281, 1, 19, 7, 5, 10], 1],
                        [[234, 139, 5455.550882718332, 2711.6990620699216, 14, 338, 1, 12, 1, 4, 3], 1],
                        [[192, 126, 4550.401485633126, 3263.3278539713288, 14, 267, 1, 22, 1, 7, 6], 1],
                        [[115, 64, 2904.935297334927, 1526.9423504405368, 16, 140, 5, 14, 1, 0, 3], 1],
                        [[186, 109, 4563.1658154723555, 2887.085558467931, 11, 261, 1, 14, 6, 1, 1], 1],
                        [[286, 215, 6179.981661406202, 4701.622398992552, 27, 437, 7, 17, 4, 2, 7], 1],
                        [[133, 81, 3448.696784061912, 2030.473379353508, 16, 168, 7, 16, 1, 1, 5], 1],
                        [[115, 68, 2731.2398248812897, 1608.1822962726662, 11, 145, 9, 12, 1, 3, 2], 1],
                        [[69, 63, 1724.8835206341985, 1554.3007212746597, 6, 114, 2, 6, 0, 1, 3], 1],
                        [[284, 220, 6289.42692214808, 4524.09444798957, 12, 463, 2, 14, 3, 7, 3], 1],
                        [[200, 147, 5175.703801826598, 3227.197011847874, 11, 297, 8, 24, 1, 1, 5], 1],
                        [[119, 152, 2786.033447077865, 3521.4797783414665, 20, 215, 12, 12, 4, 6, 2], 1],
                        [[44, 36, 1030.6865043805801, 816.3318089862648, 6, 62, 4, 5, 2, 1, 0], 1],
                        [[211, 93, 5293.212720853517, 2187.5540577554707, 18, 267, 6, 9, 2, 0, 2], 1],
                        [[177, 135, 4069.2767090371235, 3035.5656180775663, 18, 275, 3, 14, 1, 1, 0], 1],
                        [[135, 113, 3349.0722248159454, 2584.3983253722895, 18, 192, 17, 12, 4, 0, 5], 1],
                        [[136, 94, 3261.4859213216605, 2155.0632052387446, 13, 179, 2, 24, 10, 1, 1], 1],
                        [[104, 100, 2027.0879429770077, 1794.3901733117475, 14, 177, 2, 1, 5, 0, 5], 1],
                        [[234, 242, 5429.493836745718, 5302.858230355031, 13, 438, 1, 11, 2, 7, 4], 1],
                        [[198, 275, 4373.577357950337, 6313.166948986033, 19, 418, 4, 14, 4, 8, 6], 1],
                        [[167, 153, 3614.562040900074, 3532.2985695083216, 23, 272, 4, 14, 4, 1, 2], 1],
                        [[139, 110, 3485.033511521388, 2374.489944560798, 27, 179, 7, 22, 8, 2, 4], 1],
                        [[238, 185, 4991.762905940994, 4004.5112708014685, 12, 391, 2, 7, 4, 5, 2], 1],
                        [[174, 109, 4513.021566875792, 2784.2880139598565, 11, 241, 2, 22, 1, 2, 4], 1],
                        [[145, 115, 3448.74468481393, 2656.767863134473, 14, 228, 1, 9, 1, 2, 5], 1],
                        [[164, 91, 4140.903364057851, 2465.9793438459405, 20, 202, 6, 13, 5, 4, 5], 1],
                        [[180, 132, 4254.9475673593815, 3103.79773964357, 20, 265, 6, 14, 0, 3, 4], 1],
                        [[158, 171, 3526.617913602203, 3878.012630127751, 17, 282, 4, 10, 5, 5, 6], 1],
                        [[375, 502, 7625.942132193622, 10097.310680269864, 19, 825, 0, 17, 3, 5, 8], 1],
                        [[99, 108, 2651.9692334448237, 2714.6924948581063, 11, 177, 4, 12, 0, 0, 3], 1],
                        [[209, 127, 5175.7880606766985, 3098.6661892562897, 15, 274, 11, 26, 4, 2, 4], 1],
                        [[243, 104, 5756.985209069811, 2351.7144171182154, 14, 301, 1, 19, 9, 1, 2], 1],
                        [[192, 110, 4583.709131550148, 2669.211460655603, 25, 232, 10, 24, 6, 4, 1], 1],
                        [[138, 155, 3767.3357496750814, 3624.6262902350445, 14, 255, 3, 14, 4, 0, 3], 1],
                        [[227, 128, 5063.787982497974, 2831.8040422375407, 11, 319, 3, 12, 3, 2, 5], 1]]
losser_learning_data = [[[97, 100, 2477.528900227274, 2471.2273276109527, 14, 149, 5, 18, 3, 3, 5], -1],
                        [[186, 230, 4320.216562684874, 5911.448353697324, 14, 374, 3, 9, 4, 5, 7], -1],
                        [[209, 115, 4753.8814212369525, 2522.5313746149436, 4, 294, 6, 13, 7, 0, 0], -1],
                        [[176, 178, 4728.283765154024, 5001.235031318259, 17, 296, 6, 16, 6, 3, 10], -1],
                        [[196, 186, 4317.224377699875, 4380.2161367383305, 16, 342, 8, 8, 4, 2, 2], -1],
                        [[176, 118, 4193.702840706255, 2791.5907830366505, 17, 246, 1, 19, 4, 4, 3], -1],
                        [[170, 214, 4246.406723915734, 5273.3149904354705, 28, 326, 5, 10, 3, 0, 12], -1],
                        [[159, 118, 3857.156226144699, 2611.4603658884935, 12, 231, 12, 13, 3, 1, 5], -1],
                        [[80, 88, 1865.4184364674381, 1861.0302977485378, 11, 139, 2, 8, 3, 1, 4], -1],
                        [[195, 164, 4538.664368080263, 3828.0710307341005, 13, 313, 5, 18, 1, 2, 7], -1],
                        [[165, 152, 3785.6058076832755, 3536.307854168737, 22, 255, 14, 13, 5, 4, 4], -1],
                        [[225, 201, 5031.651261487469, 4122.425522875113, 16, 377, 7, 14, 1, 8, 3], -1],
                        [[114, 133, 2767.050772247689, 3377.5575788365995, 18, 199, 11, 15, 3, 0, 1], -1],
                        [[168, 179, 3941.8647454509323, 4343.5556107341345, 14, 310, 2, 14, 2, 2, 3], -1],
                        [[130, 94, 3309.7854180584595, 2207.3470342935902, 12, 200, 1, 9, 2, 0, 0], -1],
                        [[312, 293, 7744.1838596432935, 7599.65729575475, 25, 535, 3, 25, 5, 4, 8], -1],
                        [[197, 165, 4443.147108874859, 3935.8976642682555, 19, 305, 13, 17, 2, 1, 5], -1],
                        [[162, 140, 3546.4971044233616, 2923.990578854937, 13, 275, 3, 10, 1, 0, 0], -1],
                        [[312, 186, 7320.2380683947895, 4115.062438805483, 13, 461, 1, 13, 6, 2, 2], -1],
                        [[132, 98, 3122.5790887913763, 2405.412305066918, 16, 184, 3, 13, 4, 2, 8], -1],
                        [[232, 134, 5435.395418056287, 3309.7222430111688, 19, 300, 17, 19, 5, 3, 3], -1],
                        [[145, 94, 3257.0240315493083, 2155.3674842924493, 11, 205, 2, 10, 5, 1, 5], -1],
                        [[115, 121, 2509.570270588189, 2600.0086253723657, 11, 185, 2, 28, 4, 5, 1], -1],
                        [[82, 104, 1858.0764383470428, 2446.4914081957145, 16, 140, 15, 10, 2, 1, 2], -1],
                        [[137, 136, 3302.958360198853, 3223.120573395727, 11, 242, 0, 11, 5, 0, 4], -1],
                        [[106, 181, 2574.1000893367336, 4520.163105868153, 9, 241, 5, 21, 3, 3, 5], -1],
                        [[78, 142, 1825.8070615365523, 3142.76913372581, 14, 182, 2, 10, 1, 6, 5], -1],
                        [[113, 125, 2639.3077038907095, 3216.354748959563, 22, 180, 5, 22, 2, 1, 6], -1],
                        [[96, 124, 2285.113909924069, 2887.929187926763, 24, 168, 11, 9, 0, 1, 7], -1],
                        [[65, 107, 1471.9460690018743, 2452.1965479904384, 12, 147, 1, 4, 4, 1, 3], -1],
                        [[123, 92, 2666.168423756904, 2045.7225384462001, 15, 180, 8, 10, 0, 2, 0], -1],
                        [[40, 69, 979.4507967852833, 1754.0120692209036, 4, 87, 2, 13, 1, 2, 0], -1],
                        [[266, 180, 6388.972541156617, 4318.480766392187, 23, 387, 10, 15, 3, 5, 3], -1],
                        [[182, 111, 4324.104642283454, 2661.2459520388825, 17, 258, 1, 8, 4, 1, 4], -1],
                        [[106, 134, 2040.8095880115372, 3301.694049050632, 22, 182, 4, 21, 4, 5, 2], -1],
                        [[157, 141, 3592.660325609934, 3289.3581319081995, 12, 267, 2, 12, 5, 0, 0], -1],
                        [[177, 69, 4353.736158707954, 1516.6536788779117, 11, 210, 5, 15, 1, 3, 1], -1],
                        [[108, 167, 2355.224013072094, 3837.8267365243455, 19, 229, 3, 16, 2, 5, 1], -1]]
# random learning set
learning_set = winner_learning_data + losser_learning_data
random.shuffle(learning_set)
print(learning_set)
learning_set = [[[170, 214, 4246.406723915734, 5273.3149904354705, 28, 326, 5, 10, 3, 0, 12], -1],
                [[176, 118, 4193.702840706255, 2791.5907830366505, 17, 246, 1, 19, 4, 4, 3], -1],
                [[115, 64, 2904.935297334927, 1526.9423504405368, 16, 140, 5, 14, 1, 0, 3], 1],
                [[99, 108, 2651.9692334448237, 2714.6924948581063, 11, 177, 4, 12, 0, 0, 3], 1],
                [[106, 181, 2574.1000893367336, 4520.163105868153, 9, 241, 5, 21, 3, 3, 5], -1],
                [[123, 92, 2666.168423756904, 2045.7225384462001, 15, 180, 8, 10, 0, 2, 0], -1],
                [[198, 275, 4373.577357950337, 6313.166948986033, 19, 418, 4, 14, 4, 8, 6], 1],
                [[284, 220, 6289.42692214808, 4524.09444798957, 12, 463, 2, 14, 3, 7, 3], 1],
                [[195, 164, 4538.664368080263, 3828.0710307341005, 13, 313, 5, 18, 1, 2, 7], -1],
                [[164, 91, 4140.903364057851, 2465.9793438459405, 20, 202, 6, 13, 5, 4, 5], 1],
                [[210, 261, 4917.31604127615, 5887.503230042927, 12, 430, 5, 11, 5, 5, 3], 1],
                [[97, 100, 2477.528900227274, 2471.2273276109527, 14, 149, 5, 18, 3, 3, 5], -1],
                [[192, 126, 4550.401485633126, 3263.3278539713288, 14, 267, 1, 22, 1, 7, 6], 1],
                [[104, 76, 2430.9166831688362, 1782.631711499596, 10, 150, 4, 14, 1, 0, 1], 1],
                [[69, 63, 1724.8835206341985, 1554.3007212746597, 6, 114, 2, 6, 0, 1, 3], 1],
                [[234, 242, 5429.493836745718, 5302.858230355031, 13, 438, 1, 11, 2, 7, 4], 1],
                [[130, 94, 3309.7854180584595, 2207.3470342935902, 12, 200, 1, 9, 2, 0, 0], -1],
                [[232, 134, 5435.395418056287, 3309.7222430111688, 19, 300, 17, 19, 5, 3, 3], -1],
                [[225, 201, 5031.651261487469, 4122.425522875113, 16, 377, 7, 14, 1, 8, 3], -1],
                [[145, 94, 3257.0240315493083, 2155.3674842924493, 11, 205, 2, 10, 5, 1, 5], -1],
                [[139, 110, 3485.033511521388, 2374.489944560798, 27, 179, 7, 22, 8, 2, 4], 1],
                [[177, 135, 4069.2767090371235, 3035.5656180775663, 18, 275, 3, 14, 1, 1, 0], 1],
                [[159, 118, 3857.156226144699, 2611.4603658884935, 12, 231, 12, 13, 3, 1, 5], -1],
                [[82, 104, 1858.0764383470428, 2446.4914081957145, 16, 140, 15, 10, 2, 1, 2], -1],
                [[266, 180, 6388.972541156617, 4318.480766392187, 23, 387, 10, 15, 3, 5, 3], -1],
                [[243, 104, 5756.985209069811, 2351.7144171182154, 14, 301, 1, 19, 9, 1, 2], 1],
                [[167, 153, 3614.562040900074, 3532.2985695083216, 23, 272, 4, 14, 4, 1, 2], 1],
                [[162, 140, 3546.4971044233616, 2923.990578854937, 13, 275, 3, 10, 1, 0, 0], -1],
                [[186, 230, 4320.216562684874, 5911.448353697324, 14, 374, 3, 9, 4, 5, 7], -1],
                [[200, 147, 5175.703801826598, 3227.197011847874, 11, 297, 8, 24, 1, 1, 5], 1],
                [[312, 293, 7744.1838596432935, 7599.65729575475, 25, 535, 3, 25, 5, 4, 8], -1],
                [[40, 69, 979.4507967852833, 1754.0120692209036, 4, 87, 2, 13, 1, 2, 0], -1],
                [[135, 113, 3349.0722248159454, 2584.3983253722895, 18, 192, 17, 12, 4, 0, 5], 1],
                [[222, 147, 5597.194401219097, 3447.080364039, 13, 329, 1, 15, 4, 2, 5], 1],
                [[197, 165, 4443.147108874859, 3935.8976642682555, 19, 305, 13, 17, 2, 1, 5], -1],
                [[80, 88, 1865.4184364674381, 1861.0302977485378, 11, 139, 2, 8, 3, 1, 4], -1],
                [[234, 139, 5455.550882718332, 2711.6990620699216, 14, 338, 1, 12, 1, 4, 3], 1],
                [[168, 179, 3941.8647454509323, 4343.5556107341345, 14, 310, 2, 14, 2, 2, 3], -1],
                [[192, 110, 4583.709131550148, 2669.211460655603, 25, 232, 10, 24, 6, 4, 1], 1],
                [[158, 171, 3526.617913602203, 3878.012630127751, 17, 282, 4, 10, 5, 5, 6], 1],
                [[177, 69, 4353.736158707954, 1516.6536788779117, 11, 210, 5, 15, 1, 3, 1], -1],
                [[145, 115, 3448.74468481393, 2656.767863134473, 14, 228, 1, 9, 1, 2, 5], 1],
                [[186, 109, 4563.1658154723555, 2887.085558467931, 11, 261, 1, 14, 6, 1, 1], 1],
                [[176, 178, 4728.283765154024, 5001.235031318259, 17, 296, 6, 16, 6, 3, 10], -1],
                [[65, 107, 1471.9460690018743, 2452.1965479904384, 12, 147, 1, 4, 4, 1, 3], -1],
                [[209, 127, 5175.7880606766985, 3098.6661892562897, 15, 274, 11, 26, 4, 2, 4], 1],
                [[138, 155, 3767.3357496750814, 3624.6262902350445, 14, 255, 3, 14, 4, 0, 3], 1],
                [[108, 167, 2355.224013072094, 3837.8267365243455, 19, 229, 3, 16, 2, 5, 1], -1],
                [[157, 141, 3592.660325609934, 3289.3581319081995, 12, 267, 2, 12, 5, 0, 0], -1],
                [[132, 98, 3122.5790887913763, 2405.412305066918, 16, 184, 3, 13, 4, 2, 8], -1],
                [[115, 68, 2731.2398248812897, 1608.1822962726662, 11, 145, 9, 12, 1, 3, 2], 1],
                [[44, 36, 1030.6865043805801, 816.3318089862648, 6, 62, 4, 5, 2, 1, 0], 1],
                [[133, 81, 3448.696784061912, 2030.473379353508, 16, 168, 7, 16, 1, 1, 5], 1],
                [[227, 128, 5063.787982497974, 2831.8040422375407, 11, 319, 3, 12, 3, 2, 5], 1],
                [[286, 215, 6179.981661406202, 4701.622398992552, 27, 437, 7, 17, 4, 2, 7], 1],
                [[180, 132, 4254.9475673593815, 3103.79773964357, 20, 265, 6, 14, 0, 3, 4], 1],
                [[182, 111, 4324.104642283454, 2661.2459520388825, 17, 258, 1, 8, 4, 1, 4], -1],
                [[119, 152, 2786.033447077865, 3521.4797783414665, 20, 215, 12, 12, 4, 6, 2], 1],
                [[375, 502, 7625.942132193622, 10097.310680269864, 19, 825, 0, 17, 3, 5, 8], 1],
                [[238, 185, 4991.762905940994, 4004.5112708014685, 12, 391, 2, 7, 4, 5, 2], 1],
                [[165, 152, 3785.6058076832755, 3536.307854168737, 22, 255, 14, 13, 5, 4, 4], -1],
                [[165, 180, 3954.071864635465, 4200.464431671431, 22, 281, 1, 19, 7, 5, 10], 1],
                [[211, 93, 5293.212720853517, 2187.5540577554707, 18, 267, 6, 9, 2, 0, 2], 1],
                [[113, 125, 2639.3077038907095, 3216.354748959563, 22, 180, 5, 22, 2, 1, 6], -1],
                [[106, 134, 2040.8095880115372, 3301.694049050632, 22, 182, 4, 21, 4, 5, 2], -1],
                [[78, 142, 1825.8070615365523, 3142.76913372581, 14, 182, 2, 10, 1, 6, 5], -1],
                [[136, 94, 3261.4859213216605, 2155.0632052387446, 13, 179, 2, 24, 10, 1, 1], 1],
                [[174, 109, 4513.021566875792, 2784.2880139598565, 11, 241, 2, 22, 1, 2, 4], 1],
                [[115, 121, 2509.570270588189, 2600.0086253723657, 11, 185, 2, 28, 4, 5, 1], -1],
                [[312, 186, 7320.2380683947895, 4115.062438805483, 13, 461, 1, 13, 6, 2, 2], -1],
                [[137, 136, 3302.958360198853, 3223.120573395727, 11, 242, 0, 11, 5, 0, 4], -1],
                [[96, 124, 2285.113909924069, 2887.929187926763, 24, 168, 11, 9, 0, 1, 7], -1],
                [[104, 100, 2027.0879429770077, 1794.3901733117475, 14, 177, 2, 1, 5, 0, 5], 1],
                [[114, 133, 2767.050772247689, 3377.5575788365995, 18, 199, 11, 15, 3, 0, 1], -1],
                [[196, 186, 4317.224377699875, 4380.2161367383305, 16, 342, 8, 8, 4, 2, 2], -1],
                [[209, 115, 4753.8814212369525, 2522.5313746149436, 4, 294, 6, 13, 7, 0, 0], -1]]

# pass_time_learning_set
pass_time_learning_set = []
for i in range(76):
    q = []
    q_1 = []
    q.append(learning_set[i][0][2])
    q.append(learning_set[i][0][3])
    q_1.append(q)
    q_1.append(learning_set[i][1])
    pass_time_learning_set.append(q_1)
print(pass_time_learning_set)
# result
pass_time_learning_set = [[[170, 214], -1], [[176, 118], -1], [[115, 64], 1], [[99, 108], 1], [[106, 181], -1],
                          [[123, 92], -1], [[198, 275], 1], [[284, 220], 1], [[195, 164], -1], [[164, 91], 1],
                          [[210, 261], 1], [[97, 100], -1], [[192, 126], 1], [[104, 76], 1], [[69, 63], 1],
                          [[234, 242], 1], [[130, 94], -1], [[232, 134], -1], [[225, 201], -1], [[145, 94], -1],
                          [[139, 110], 1], [[177, 135], 1], [[159, 118], -1], [[82, 104], -1], [[266, 180], -1],
                          [[243, 104], 1], [[167, 153], 1], [[162, 140], -1], [[186, 230], -1], [[200, 147], 1],
                          [[312, 293], -1], [[40, 69], -1], [[135, 113], 1], [[222, 147], 1], [[197, 165], -1],
                          [[80, 88], -1], [[234, 139], 1], [[168, 179], -1], [[192, 110], 1], [[158, 171], 1],
                          [[177, 69], -1], [[145, 115], 1], [[186, 109], 1], [[176, 178], -1], [[65, 107], -1],
                          [[209, 127], 1], [[138, 155], 1], [[108, 167], -1], [[157, 141], -1], [[132, 98], -1],
                          [[115, 68], 1], [[44, 36], 1], [[133, 81], 1], [[227, 128], 1], [[286, 215], 1],
                          [[180, 132], 1], [[182, 111], -1], [[119, 152], 1], [[375, 502], 1], [[238, 185], 1],
                          [[165, 152], -1], [[165, 180], 1], [[211, 93], 1], [[113, 125], -1], [[106, 134], -1],
                          [[78, 142], -1], [[136, 94], 1], [[174, 109], 1], [[115, 121], -1], [[312, 186], -1],
                          [[137, 136], -1], [[96, 124], -1], [[104, 100], 1], [[114, 133], -1], [[196, 186], -1],
                          [[209, 115], -1]]
pass_distance_learning_set = [[[4246.406723915734, 5273.3149904354705], -1],
                              [[4193.702840706255, 2791.5907830366505], -1],
                              [[2904.935297334927, 1526.9423504405368], 1],
                              [[2651.9692334448237, 2714.6924948581063], 1],
                              [[2574.1000893367336, 4520.163105868153], -1],
                              [[2666.168423756904, 2045.7225384462001], -1],
                              [[4373.577357950337, 6313.166948986033], 1], [[6289.42692214808, 4524.09444798957], 1],
                              [[4538.664368080263, 3828.0710307341005], -1],
                              [[4140.903364057851, 2465.9793438459405], 1], [[4917.31604127615, 5887.503230042927], 1],
                              [[2477.528900227274, 2471.2273276109527], -1],
                              [[4550.401485633126, 3263.3278539713288], 1],
                              [[2430.9166831688362, 1782.631711499596], 1],
                              [[1724.8835206341985, 1554.3007212746597], 1],
                              [[5429.493836745718, 5302.858230355031], 1],
                              [[3309.7854180584595, 2207.3470342935902], -1],
                              [[5435.395418056287, 3309.7222430111688], -1],
                              [[5031.651261487469, 4122.425522875113], -1],
                              [[3257.0240315493083, 2155.3674842924493], -1],
                              [[3485.033511521388, 2374.489944560798], 1],
                              [[4069.2767090371235, 3035.5656180775663], 1],
                              [[3857.156226144699, 2611.4603658884935], -1],
                              [[1858.0764383470428, 2446.4914081957145], -1],
                              [[6388.972541156617, 4318.480766392187], -1],
                              [[5756.985209069811, 2351.7144171182154], 1],
                              [[3614.562040900074, 3532.2985695083216], 1],
                              [[3546.4971044233616, 2923.990578854937], -1],
                              [[4320.216562684874, 5911.448353697324], -1], [[5175.703801826598, 3227.197011847874], 1],
                              [[7744.1838596432935, 7599.65729575475], -1],
                              [[979.4507967852833, 1754.0120692209036], -1],
                              [[3349.0722248159454, 2584.3983253722895], 1], [[5597.194401219097, 3447.080364039], 1],
                              [[4443.147108874859, 3935.8976642682555], -1],
                              [[1865.4184364674381, 1861.0302977485378], -1],
                              [[5455.550882718332, 2711.6990620699216], 1],
                              [[3941.8647454509323, 4343.5556107341345], -1],
                              [[4583.709131550148, 2669.211460655603], 1], [[3526.617913602203, 3878.012630127751], 1],
                              [[4353.736158707954, 1516.6536788779117], -1], [[3448.74468481393, 2656.767863134473], 1],
                              [[4563.1658154723555, 2887.085558467931], 1],
                              [[4728.283765154024, 5001.235031318259], -1],
                              [[1471.9460690018743, 2452.1965479904384], -1],
                              [[5175.7880606766985, 3098.6661892562897], 1],
                              [[3767.3357496750814, 3624.6262902350445], 1],
                              [[2355.224013072094, 3837.8267365243455], -1],
                              [[3592.660325609934, 3289.3581319081995], -1],
                              [[3122.5790887913763, 2405.412305066918], -1],
                              [[2731.2398248812897, 1608.1822962726662], 1],
                              [[1030.6865043805801, 816.3318089862648], 1], [[3448.696784061912, 2030.473379353508], 1],
                              [[5063.787982497974, 2831.8040422375407], 1], [[6179.981661406202, 4701.622398992552], 1],
                              [[4254.9475673593815, 3103.79773964357], 1],
                              [[4324.104642283454, 2661.2459520388825], -1],
                              [[2786.033447077865, 3521.4797783414665], 1],
                              [[7625.942132193622, 10097.310680269864], 1],
                              [[4991.762905940994, 4004.5112708014685], 1],
                              [[3785.6058076832755, 3536.307854168737], -1],
                              [[3954.071864635465, 4200.464431671431], 1], [[5293.212720853517, 2187.5540577554707], 1],
                              [[2639.3077038907095, 3216.354748959563], -1],
                              [[2040.8095880115372, 3301.694049050632], -1],
                              [[1825.8070615365523, 3142.76913372581], -1],
                              [[3261.4859213216605, 2155.0632052387446], 1],
                              [[4513.021566875792, 2784.2880139598565], 1],
                              [[2509.570270588189, 2600.0086253723657], -1],
                              [[7320.2380683947895, 4115.062438805483], -1],
                              [[3302.958360198853, 3223.120573395727], -1],
                              [[2285.113909924069, 2887.929187926763], -1],
                              [[2027.0879429770077, 1794.3901733117475], 1],
                              [[2767.050772247689, 3377.5575788365995], -1],
                              [[4317.224377699875, 4380.2161367383305], -1],
                              [[4753.8814212369525, 2522.5313746149436], -1]]
X_1 = []
X_2 = []
Y_1 = []
Y_2 = []
for ele in pass_distance_learning_set:
    if ele[1] == 1:
        X_1.append(ele[0][0])
        Y_1.append(ele[0][1])
    else:
        X_2.append(ele[0][0])
        Y_2.append(ele[0][1])
plt.plot(X_1, Y_1, 'd')
plt.plot(X_2, Y_2, 'o')
plt.xlabel('pass distance in 1H')
plt.ylabel('pass distance in 2H')
plt.show()

# find the win rate
print(matches_data[:3])
win_rate = []
for i in range(38):
    q = matches_data[i: i + 1]
    if q['OwnScore'][i] + q['OpponentScore'][i] != 0:
        q_rate = np.abs((q['OwnScore'][i] - q['OpponentScore'][i]) / (q['OwnScore'][i] + q['OpponentScore'][i]))
    else:
        q_rate = 0
    win_rate.append(q_rate)
print(win_rate)
# result
win_rate = [1.0, 0.0, 1.0, 1.0, 1.0, 0.33333333333333331, 1.0, 0.0, 0.42857142857142855, 1.0, 0.20000000000000001, 0.0,
            0.59999999999999998, 1.0, 1.0, 0.0, 1.0, 0.5, 0, 0, 0.33333333333333331, 1.0, 1.0, 0.0, 0.33333333333333331,
            0.66666666666666663, 0.5, 1.0, 0.33333333333333331, 1.0, 0.33333333333333331, 0.5, 0, 0.0, 1.0, 1.0, 0.0,
            0.5]

winner_learning_data_rate = []
for i in range(len(winner_learning_data)):
    q = []
    q.append(winner_learning_data[i][0])
    q.append(winner_learning_data[i][1] * win_rate[i])
    winner_learning_data_rate.append(q)
print(winner_learning_data_rate)
# result
winner_learning_data_rate = [[[222, 147, 5597.194401219097, 3447.080364039, 13, 329, 1, 15, 4, 2, 5], 1.0],
                             [[104, 76, 2430.9166831688362, 1782.631711499596, 10, 150, 4, 14, 1, 0, 1], 0.0],
                             [[210, 261, 4917.31604127615, 5887.503230042927, 12, 430, 5, 11, 5, 5, 3], 1.0],
                             [[165, 180, 3954.071864635465, 4200.464431671431, 22, 281, 1, 19, 7, 5, 10], 1.0],
                             [[234, 139, 5455.550882718332, 2711.6990620699216, 14, 338, 1, 12, 1, 4, 3], 1.0],
                             [[192, 126, 4550.401485633126, 3263.3278539713288, 14, 267, 1, 22, 1, 7, 6],
                              0.3333333333333333],
                             [[115, 64, 2904.935297334927, 1526.9423504405368, 16, 140, 5, 14, 1, 0, 3], 1.0],
                             [[186, 109, 4563.1658154723555, 2887.085558467931, 11, 261, 1, 14, 6, 1, 1], 0.0],
                             [[286, 215, 6179.981661406202, 4701.622398992552, 27, 437, 7, 17, 4, 2, 7],
                              0.42857142857142855],
                             [[133, 81, 3448.696784061912, 2030.473379353508, 16, 168, 7, 16, 1, 1, 5], 1.0],
                             [[115, 68, 2731.2398248812897, 1608.1822962726662, 11, 145, 9, 12, 1, 3, 2], 0.2],
                             [[69, 63, 1724.8835206341985, 1554.3007212746597, 6, 114, 2, 6, 0, 1, 3], 0.0],
                             [[284, 220, 6289.42692214808, 4524.09444798957, 12, 463, 2, 14, 3, 7, 3], 0.6],
                             [[200, 147, 5175.703801826598, 3227.197011847874, 11, 297, 8, 24, 1, 1, 5], 1.0],
                             [[119, 152, 2786.033447077865, 3521.4797783414665, 20, 215, 12, 12, 4, 6, 2], 1.0],
                             [[44, 36, 1030.6865043805801, 816.3318089862648, 6, 62, 4, 5, 2, 1, 0], 0.0],
                             [[211, 93, 5293.212720853517, 2187.5540577554707, 18, 267, 6, 9, 2, 0, 2], 1.0],
                             [[177, 135, 4069.2767090371235, 3035.5656180775663, 18, 275, 3, 14, 1, 1, 0], 0.5],
                             [[135, 113, 3349.0722248159454, 2584.3983253722895, 18, 192, 17, 12, 4, 0, 5], 0],
                             [[136, 94, 3261.4859213216605, 2155.0632052387446, 13, 179, 2, 24, 10, 1, 1], 0],
                             [[104, 100, 2027.0879429770077, 1794.3901733117475, 14, 177, 2, 1, 5, 0, 5],
                              0.3333333333333333],
                             [[234, 242, 5429.493836745718, 5302.858230355031, 13, 438, 1, 11, 2, 7, 4], 1.0],
                             [[198, 275, 4373.577357950337, 6313.166948986033, 19, 418, 4, 14, 4, 8, 6], 1.0],
                             [[167, 153, 3614.562040900074, 3532.2985695083216, 23, 272, 4, 14, 4, 1, 2], 0.0],
                             [[139, 110, 3485.033511521388, 2374.489944560798, 27, 179, 7, 22, 8, 2, 4],
                              0.3333333333333333],
                             [[238, 185, 4991.762905940994, 4004.5112708014685, 12, 391, 2, 7, 4, 5, 2],
                              0.6666666666666666],
                             [[174, 109, 4513.021566875792, 2784.2880139598565, 11, 241, 2, 22, 1, 2, 4], 0.5],
                             [[145, 115, 3448.74468481393, 2656.767863134473, 14, 228, 1, 9, 1, 2, 5], 1.0],
                             [[164, 91, 4140.903364057851, 2465.9793438459405, 20, 202, 6, 13, 5, 4, 5],
                              0.3333333333333333],
                             [[180, 132, 4254.9475673593815, 3103.79773964357, 20, 265, 6, 14, 0, 3, 4], 1.0],
                             [[158, 171, 3526.617913602203, 3878.012630127751, 17, 282, 4, 10, 5, 5, 6],
                              0.3333333333333333],
                             [[375, 502, 7625.942132193622, 10097.310680269864, 19, 825, 0, 17, 3, 5, 8], 0.5],
                             [[99, 108, 2651.9692334448237, 2714.6924948581063, 11, 177, 4, 12, 0, 0, 3], 0],
                             [[209, 127, 5175.7880606766985, 3098.6661892562897, 15, 274, 11, 26, 4, 2, 4], 0.0],
                             [[243, 104, 5756.985209069811, 2351.7144171182154, 14, 301, 1, 19, 9, 1, 2], 1.0],
                             [[192, 110, 4583.709131550148, 2669.211460655603, 25, 232, 10, 24, 6, 4, 1], 1.0],
                             [[138, 155, 3767.3357496750814, 3624.6262902350445, 14, 255, 3, 14, 4, 0, 3], 0.0],
                             [[227, 128, 5063.787982497974, 2831.8040422375407, 11, 319, 3, 12, 3, 2, 5], 0.5]]
losser_learning_data_rate = [[[97, 100, 2477.528900227274, 2471.2273276109527, 14, 149, 5, 18, 3, 3, 5], -1.0],
                             [[186, 230, 4320.216562684874, 5911.448353697324, 14, 374, 3, 9, 4, 5, 7], -0.0],
                             [[209, 115, 4753.8814212369525, 2522.5313746149436, 4, 294, 6, 13, 7, 0, 0], -1.0],
                             [[176, 178, 4728.283765154024, 5001.235031318259, 17, 296, 6, 16, 6, 3, 10], -1.0],
                             [[196, 186, 4317.224377699875, 4380.2161367383305, 16, 342, 8, 8, 4, 2, 2], -1.0],
                             [[176, 118, 4193.702840706255, 2791.5907830366505, 17, 246, 1, 19, 4, 4, 3],
                              -0.3333333333333333],
                             [[170, 214, 4246.406723915734, 5273.3149904354705, 28, 326, 5, 10, 3, 0, 12], -1.0],
                             [[159, 118, 3857.156226144699, 2611.4603658884935, 12, 231, 12, 13, 3, 1, 5], -0.0],
                             [[80, 88, 1865.4184364674381, 1861.0302977485378, 11, 139, 2, 8, 3, 1, 4],
                              -0.42857142857142855],
                             [[195, 164, 4538.664368080263, 3828.0710307341005, 13, 313, 5, 18, 1, 2, 7], -1.0],
                             [[165, 152, 3785.6058076832755, 3536.307854168737, 22, 255, 14, 13, 5, 4, 4], -0.2],
                             [[225, 201, 5031.651261487469, 4122.425522875113, 16, 377, 7, 14, 1, 8, 3], -0.0],
                             [[114, 133, 2767.050772247689, 3377.5575788365995, 18, 199, 11, 15, 3, 0, 1], -0.6],
                             [[168, 179, 3941.8647454509323, 4343.5556107341345, 14, 310, 2, 14, 2, 2, 3], -1.0],
                             [[130, 94, 3309.7854180584595, 2207.3470342935902, 12, 200, 1, 9, 2, 0, 0], -1.0],
                             [[312, 293, 7744.1838596432935, 7599.65729575475, 25, 535, 3, 25, 5, 4, 8], -0.0],
                             [[197, 165, 4443.147108874859, 3935.8976642682555, 19, 305, 13, 17, 2, 1, 5], -1.0],
                             [[162, 140, 3546.4971044233616, 2923.990578854937, 13, 275, 3, 10, 1, 0, 0], -0.5],
                             [[312, 186, 7320.2380683947895, 4115.062438805483, 13, 461, 1, 13, 6, 2, 2], 0],
                             [[132, 98, 3122.5790887913763, 2405.412305066918, 16, 184, 3, 13, 4, 2, 8], 0],
                             [[232, 134, 5435.395418056287, 3309.7222430111688, 19, 300, 17, 19, 5, 3, 3],
                              -0.3333333333333333],
                             [[145, 94, 3257.0240315493083, 2155.3674842924493, 11, 205, 2, 10, 5, 1, 5], -1.0],
                             [[115, 121, 2509.570270588189, 2600.0086253723657, 11, 185, 2, 28, 4, 5, 1], -1.0],
                             [[82, 104, 1858.0764383470428, 2446.4914081957145, 16, 140, 15, 10, 2, 1, 2], -0.0],
                             [[137, 136, 3302.958360198853, 3223.120573395727, 11, 242, 0, 11, 5, 0, 4],
                              -0.3333333333333333],
                             [[106, 181, 2574.1000893367336, 4520.163105868153, 9, 241, 5, 21, 3, 3, 5],
                              -0.6666666666666666],
                             [[78, 142, 1825.8070615365523, 3142.76913372581, 14, 182, 2, 10, 1, 6, 5], -0.5],
                             [[113, 125, 2639.3077038907095, 3216.354748959563, 22, 180, 5, 22, 2, 1, 6], -1.0],
                             [[96, 124, 2285.113909924069, 2887.929187926763, 24, 168, 11, 9, 0, 1, 7],
                              -0.3333333333333333],
                             [[65, 107, 1471.9460690018743, 2452.1965479904384, 12, 147, 1, 4, 4, 1, 3], -1.0],
                             [[123, 92, 2666.168423756904, 2045.7225384462001, 15, 180, 8, 10, 0, 2, 0],
                              -0.3333333333333333],
                             [[40, 69, 979.4507967852833, 1754.0120692209036, 4, 87, 2, 13, 1, 2, 0], -0.5],
                             [[266, 180, 6388.972541156617, 4318.480766392187, 23, 387, 10, 15, 3, 5, 3], 0],
                             [[182, 111, 4324.104642283454, 2661.2459520388825, 17, 258, 1, 8, 4, 1, 4], -0.0],
                             [[106, 134, 2040.8095880115372, 3301.694049050632, 22, 182, 4, 21, 4, 5, 2], -1.0],
                             [[157, 141, 3592.660325609934, 3289.3581319081995, 12, 267, 2, 12, 5, 0, 0], -1.0],
                             [[177, 69, 4353.736158707954, 1516.6536788779117, 11, 210, 5, 15, 1, 3, 1], -0.0],
                             [[108, 167, 2355.224013072094, 3837.8267365243455, 19, 229, 3, 16, 2, 5, 1], -0.5]]
# random learning set rate
learning_set_rate = winner_learning_data_rate + losser_learning_data_rate
random.shuffle(learning_set_rate)
print(learning_set_rate)
# result
learning_set_rate = [[[284, 220, 6289.42692214808, 4524.09444798957, 12, 463, 2, 14, 3, 7, 3], 0.6],
                     [[65, 107, 1471.9460690018743, 2452.1965479904384, 12, 147, 1, 4, 4, 1, 3], -1.0],
                     [[192, 126, 4550.401485633126, 3263.3278539713288, 14, 267, 1, 22, 1, 7, 6], 0.3333333333333333],
                     [[104, 76, 2430.9166831688362, 1782.631711499596, 10, 150, 4, 14, 1, 0, 1], 0.0],
                     [[312, 186, 7320.2380683947895, 4115.062438805483, 13, 461, 1, 13, 6, 2, 2], 0],
                     [[132, 98, 3122.5790887913763, 2405.412305066918, 16, 184, 3, 13, 4, 2, 8], 0],
                     [[115, 121, 2509.570270588189, 2600.0086253723657, 11, 185, 2, 28, 4, 5, 1], -1.0],
                     [[168, 179, 3941.8647454509323, 4343.5556107341345, 14, 310, 2, 14, 2, 2, 3], -1.0],
                     [[266, 180, 6388.972541156617, 4318.480766392187, 23, 387, 10, 15, 3, 5, 3], 0],
                     [[174, 109, 4513.021566875792, 2784.2880139598565, 11, 241, 2, 22, 1, 2, 4], 0.5],
                     [[96, 124, 2285.113909924069, 2887.929187926763, 24, 168, 11, 9, 0, 1, 7], -0.3333333333333333],
                     [[195, 164, 4538.664368080263, 3828.0710307341005, 13, 313, 5, 18, 1, 2, 7], -1.0],
                     [[182, 111, 4324.104642283454, 2661.2459520388825, 17, 258, 1, 8, 4, 1, 4], -0.0],
                     [[209, 115, 4753.8814212369525, 2522.5313746149436, 4, 294, 6, 13, 7, 0, 0], -1.0],
                     [[196, 186, 4317.224377699875, 4380.2161367383305, 16, 342, 8, 8, 4, 2, 2], -1.0],
                     [[133, 81, 3448.696784061912, 2030.473379353508, 16, 168, 7, 16, 1, 1, 5], 1.0],
                     [[136, 94, 3261.4859213216605, 2155.0632052387446, 13, 179, 2, 24, 10, 1, 1], 0],
                     [[97, 100, 2477.528900227274, 2471.2273276109527, 14, 149, 5, 18, 3, 3, 5], -1.0],
                     [[159, 118, 3857.156226144699, 2611.4603658884935, 12, 231, 12, 13, 3, 1, 5], -0.0],
                     [[139, 110, 3485.033511521388, 2374.489944560798, 27, 179, 7, 22, 8, 2, 4], 0.3333333333333333],
                     [[137, 136, 3302.958360198853, 3223.120573395727, 11, 242, 0, 11, 5, 0, 4], -0.3333333333333333],
                     [[78, 142, 1825.8070615365523, 3142.76913372581, 14, 182, 2, 10, 1, 6, 5], -0.5],
                     [[165, 152, 3785.6058076832755, 3536.307854168737, 22, 255, 14, 13, 5, 4, 4], -0.2],
                     [[186, 109, 4563.1658154723555, 2887.085558467931, 11, 261, 1, 14, 6, 1, 1], 0.0],
                     [[164, 91, 4140.903364057851, 2465.9793438459405, 20, 202, 6, 13, 5, 4, 5], 0.3333333333333333],
                     [[162, 140, 3546.4971044233616, 2923.990578854937, 13, 275, 3, 10, 1, 0, 0], -0.5],
                     [[80, 88, 1865.4184364674381, 1861.0302977485378, 11, 139, 2, 8, 3, 1, 4], -0.42857142857142855],
                     [[119, 152, 2786.033447077865, 3521.4797783414665, 20, 215, 12, 12, 4, 6, 2], 1.0],
                     [[243, 104, 5756.985209069811, 2351.7144171182154, 14, 301, 1, 19, 9, 1, 2], 1.0],
                     [[82, 104, 1858.0764383470428, 2446.4914081957145, 16, 140, 15, 10, 2, 1, 2], -0.0],
                     [[104, 100, 2027.0879429770077, 1794.3901733117475, 14, 177, 2, 1, 5, 0, 5], 0.3333333333333333],
                     [[238, 185, 4991.762905940994, 4004.5112708014685, 12, 391, 2, 7, 4, 5, 2], 0.6666666666666666],
                     [[375, 502, 7625.942132193622, 10097.310680269864, 19, 825, 0, 17, 3, 5, 8], 0.5],
                     [[200, 147, 5175.703801826598, 3227.197011847874, 11, 297, 8, 24, 1, 1, 5], 1.0],
                     [[209, 127, 5175.7880606766985, 3098.6661892562897, 15, 274, 11, 26, 4, 2, 4], 0.0],
                     [[108, 167, 2355.224013072094, 3837.8267365243455, 19, 229, 3, 16, 2, 5, 1], -0.5],
                     [[145, 94, 3257.0240315493083, 2155.3674842924493, 11, 205, 2, 10, 5, 1, 5], -1.0],
                     [[176, 178, 4728.283765154024, 5001.235031318259, 17, 296, 6, 16, 6, 3, 10], -1.0],
                     [[115, 64, 2904.935297334927, 1526.9423504405368, 16, 140, 5, 14, 1, 0, 3], 1.0],
                     [[135, 113, 3349.0722248159454, 2584.3983253722895, 18, 192, 17, 12, 4, 0, 5], 0],
                     [[130, 94, 3309.7854180584595, 2207.3470342935902, 12, 200, 1, 9, 2, 0, 0], -1.0],
                     [[312, 293, 7744.1838596432935, 7599.65729575475, 25, 535, 3, 25, 5, 4, 8], -0.0],
                     [[177, 69, 4353.736158707954, 1516.6536788779117, 11, 210, 5, 15, 1, 3, 1], -0.0],
                     [[115, 68, 2731.2398248812897, 1608.1822962726662, 11, 145, 9, 12, 1, 3, 2], 0.2],
                     [[197, 165, 4443.147108874859, 3935.8976642682555, 19, 305, 13, 17, 2, 1, 5], -1.0],
                     [[222, 147, 5597.194401219097, 3447.080364039, 13, 329, 1, 15, 4, 2, 5], 1.0],
                     [[170, 214, 4246.406723915734, 5273.3149904354705, 28, 326, 5, 10, 3, 0, 12], -1.0],
                     [[232, 134, 5435.395418056287, 3309.7222430111688, 19, 300, 17, 19, 5, 3, 3], -0.3333333333333333],
                     [[99, 108, 2651.9692334448237, 2714.6924948581063, 11, 177, 4, 12, 0, 0, 3], 0],
                     [[167, 153, 3614.562040900074, 3532.2985695083216, 23, 272, 4, 14, 4, 1, 2], 0.0],
                     [[192, 110, 4583.709131550148, 2669.211460655603, 25, 232, 10, 24, 6, 4, 1], 1.0],
                     [[44, 36, 1030.6865043805801, 816.3318089862648, 6, 62, 4, 5, 2, 1, 0], 0.0],
                     [[186, 230, 4320.216562684874, 5911.448353697324, 14, 374, 3, 9, 4, 5, 7], -0.0],
                     [[138, 155, 3767.3357496750814, 3624.6262902350445, 14, 255, 3, 14, 4, 0, 3], 0.0],
                     [[286, 215, 6179.981661406202, 4701.622398992552, 27, 437, 7, 17, 4, 2, 7], 0.42857142857142855],
                     [[114, 133, 2767.050772247689, 3377.5575788365995, 18, 199, 11, 15, 3, 0, 1], -0.6],
                     [[225, 201, 5031.651261487469, 4122.425522875113, 16, 377, 7, 14, 1, 8, 3], -0.0],
                     [[177, 135, 4069.2767090371235, 3035.5656180775663, 18, 275, 3, 14, 1, 1, 0], 0.5],
                     [[210, 261, 4917.31604127615, 5887.503230042927, 12, 430, 5, 11, 5, 5, 3], 1.0],
                     [[69, 63, 1724.8835206341985, 1554.3007212746597, 6, 114, 2, 6, 0, 1, 3], 0.0],
                     [[227, 128, 5063.787982497974, 2831.8040422375407, 11, 319, 3, 12, 3, 2, 5], 0.5],
                     [[157, 141, 3592.660325609934, 3289.3581319081995, 12, 267, 2, 12, 5, 0, 0], -1.0],
                     [[106, 181, 2574.1000893367336, 4520.163105868153, 9, 241, 5, 21, 3, 3, 5], -0.6666666666666666],
                     [[180, 132, 4254.9475673593815, 3103.79773964357, 20, 265, 6, 14, 0, 3, 4], 1.0],
                     [[198, 275, 4373.577357950337, 6313.166948986033, 19, 418, 4, 14, 4, 8, 6], 1.0],
                     [[40, 69, 979.4507967852833, 1754.0120692209036, 4, 87, 2, 13, 1, 2, 0], -0.5],
                     [[106, 134, 2040.8095880115372, 3301.694049050632, 22, 182, 4, 21, 4, 5, 2], -1.0],
                     [[211, 93, 5293.212720853517, 2187.5540577554707, 18, 267, 6, 9, 2, 0, 2], 1.0],
                     [[234, 139, 5455.550882718332, 2711.6990620699216, 14, 338, 1, 12, 1, 4, 3], 1.0],
                     [[123, 92, 2666.168423756904, 2045.7225384462001, 15, 180, 8, 10, 0, 2, 0], -0.3333333333333333],
                     [[113, 125, 2639.3077038907095, 3216.354748959563, 22, 180, 5, 22, 2, 1, 6], -1.0],
                     [[234, 242, 5429.493836745718, 5302.858230355031, 13, 438, 1, 11, 2, 7, 4], 1.0],
                     [[158, 171, 3526.617913602203, 3878.012630127751, 17, 282, 4, 10, 5, 5, 6], 0.3333333333333333],
                     [[176, 118, 4193.702840706255, 2791.5907830366505, 17, 246, 1, 19, 4, 4, 3], -0.3333333333333333],
                     [[165, 180, 3954.071864635465, 4200.464431671431, 22, 281, 1, 19, 7, 5, 10], 1.0],
                     [[145, 115, 3448.74468481393, 2656.767863134473, 14, 228, 1, 9, 1, 2, 5], 1.0]]

# total pass time learning set
total_pass_time_learning_set = []
for ele in learning_set_rate:
    q = []
    q.append(ele[0][2] + ele[0][3])
    q.append(ele[1])
    total_pass_time_learning_set.append(q)
print(total_pass_time_learning_set)
X = []
Y = []
for ele in total_pass_time_learning_set:
    X.append(ele[0])
    Y.append(ele[1])
plt.plot(X,Y,'o')
plt.show()

# 数据归一化处理
current_list = []
current_list2 = []
for ele in learning_set_rate:
    current_list.append(ele[0])
    current_list2.append(ele[1])
current_list = np.array(current_list).T
current_list = current_list.tolist()
print(current_list2)

# 定义归一化函数
def normalization(lst):
    s = 0
    for ele in lst:
        s += ele
    mean = s / len(lst)
    s = 0
    for ele in lst:
        s += (ele - mean) ** 2
    derta = np.sqrt(s / len(lst))
    q = []
    for ele in lst:
        q.append((ele - mean) / derta)
    return [q, mean, derta]

mean_list = []
derta_list = []
for i in range(len(current_list)):
    q_0 = normalization(current_list[i])
    current_list[i] = q_0[0]
    mean_list.append(q_0[1])
    derta_list.append(q_0[2])
print(mean_list,'\n',derta_list)
# result
mean_list = [165.92105263157896, 142.35526315789474, 3898.895202696612, 3304.605795674342, 15.43421052631579,
             264.30263157894734, 4.934210526315789, 14.157894736842104, 3.25, 2.5, 3.6973684210526314]
derta_list = [63.511242924692752, 65.3421569302634, 1446.5967847051918, 1437.4550772500425, 5.1281871381707322,
              113.89642336892184, 4.0824899726430797, 5.328801167585115, 2.1406159959472562, 2.1612618146765441,
              2.5547671479129743]


# current_list = np.array(current_list).T
# current_list = current_list.tolist()


# for check
def mean(lst):
    s = 0
    for ele in lst:
        s += ele
    return s / len(lst)


def derta(lst):
    s = 0
    for ele in lst:
        s += (ele - mean(lst)) ** 2
    derta1 = np.sqrt(s / len(lst))
    return derta1


for ele in current_list:
    print(mean(ele), derta(ele))

# 定义归一化后的训练集
learning_set_rate_after_normalization = []
for i in range(len(current_list)):
    q = []
    q.append(current_list[i])
    q.append(current_list2[i])
    learning_set_rate_after_normalization.append(q)

# result
learning_set_rate_after_normalization = [[[1.8591818067303596, 1.1882793664888018, 1.6525211065906278,
                                           0.8483664440131231, -0.669673401883848, 1.7445444074872494,
                                           -0.7187306143990666, -0.029630442547297846, -0.11678881241348991,
                                           2.0821170158292337, -0.2729675076737704], 0.6], [
                                             [-1.5890265720550325, -0.5410789116684309, -1.6776956504775697,
                                              -0.5929988777907588, -0.669673401883848, -1.029906191162759,
                                              -0.9636791645978516, -1.9062251372095047, 0.3503664372404698,
                                              -0.6940390052764112, -0.2729675076737704], -1.0], [
                                             [0.41061938276572, -0.2503018560490732, 0.45037172059613495,
                                              -0.0287159872724378, -0.2796720337369327, 0.023682643767623975,
                                              -0.9636791645978516, 1.4716453131824676, -1.0510993117214094,
                                              2.0821170158292337, 0.9013078083567895], 0.3333333333333333], [
                                             [-0.9749620662439352, -1.0155046339947513, -1.0147807150193144,
                                              -1.0587976683670663, -1.0596747700307634, -1.0035664702894993,
                                              -0.22883351400149654, -0.029630442547297846, -1.0510993117214094,
                                              -1.1567316754606853, -1.0558177183608104], 0.0], [
                                             [2.3000486314152497, 0.6679414774857406, 2.365097794957029,
                                              0.5638135451729067, -0.4746727178103904, 1.726984593571743,
                                              -0.9636791645978516, -0.21728991201351852, 1.2846769365483892,
                                              -0.23134633509213706, -0.6643926130172904], 0], [
                                             [-0.534095241559045, -0.678815411698653, -0.5366499650166474,
                                              -0.6255454551857351, 0.11032933440998265, -0.7050496337258908,
                                              -0.47378206420028157, -0.21728991201351852, 0.3503664372404698,
                                              -0.23134633509213706, 1.6841580190438292], 0], [
                                             [-0.8017643851177283, -0.326822133843641, -0.9604092493483315,
                                              -0.4901698713603786, -0.8646740859573058, -0.6962697267681377,
                                              -0.7187306143990666, 2.5976021299797916, 0.3503664372404698,
                                              1.1567316754606853, -1.0558177183608104], -1.0], [
                                             [0.032733533035814034, 0.5608130885733457, 0.029703883769572406,
                                              0.7227702844442138, -0.2796720337369327, 0.4012186429510112,
                                              -0.7187306143990666, -0.029630442547297846, -0.5839440620674496,
                                              -0.23134633509213706, -0.2729675076737704], -1.0], [
                                             [1.57576741943293, 0.5761171441322592, 1.7213347663892868,
                                              0.7053263693342424, 1.4753341229241863, 1.0772714786980069,
                                              1.2408577871912136, 0.15802902691892284, -0.11678881241348991,
                                              1.1567316754606853, -0.2729675076737704], 0], [
                                             [0.12720499546829053, -0.5104708005506038, 0.42453181886778163,
                                              -0.361971507805233, -0.8646740859573058, -0.204594937133959,
                                              -0.7187306143990666, 1.4716453131824676, -1.0510993117214094,
                                              -0.23134633509213706, 0.11845759766974952], 0.5], [
                                             [-1.100924016153904, -0.2809099671669003, -1.1155709108681744,
                                              -0.2898710466449582, 1.670334806997644, -0.8455281450499419,
                                              1.4858063373899988, -0.9679277898784012, -1.518254561375369,
                                              -0.6940390052764112, 1.2927329137003094], -0.3333333333333333], [
                                             [0.4578551139819583, 0.3312522551896422, 0.4422581137659806,
                                              0.3641611089935319, -0.4746727178103904, 0.42755836382427076,
                                              0.016115036197288515, 0.7210074353175848, -1.0510993117214094,
                                              -0.23134633509213706, 1.2927329137003094], -1.0], [
                                             [0.2531669453782592, -0.47986268943277666, 0.29393777456341946,
                                              -0.44756866062642764, 0.3053300184834403, -0.055336518852154744,
                                              -0.9636791645978516, -1.155587259344622, 0.3503664372404698,
                                              -0.6940390052764112, 0.11845759766974952], -0.0], [
                                             [0.6782885263244034, -0.4186464671971224, 0.591032848669425,
                                              -0.5440687736520883, -2.2296788744715093, 0.26074013162696014,
                                              0.2610635863960736, -0.21728991201351852, 1.7518321862023487,
                                              -1.1567316754606853, -1.4472428237043302], -1.0], [
                                             [0.47360035772070436, 0.6679414774857406, 0.28918160155354955,
                                              0.7482740560642148, 0.11032933440998265, 0.6821756655991132,
                                              0.7509606867936437, -1.155587259344622, 0.3503664372404698,
                                              -0.23134633509213706, -0.6643926130172904], -1.0], [
                                             [-0.5183499978202989, -0.9389843562001835, -0.3112120968293513,
                                              -0.8863806852025896, 0.11032933440998265, -0.8455281450499419,
                                              0.5060121365948587, 0.34568849638514354, -1.0510993117214094,
                                              -0.6940390052764112, 0.5098827030132694], 1.0], [
                                             [-0.47111426660406064, -0.7400316339343073, -0.44062677873630973,
                                              -0.7997067933662019, -0.4746727178103904, -0.7489491685146568,
                                              -0.7187306143990666, 1.846964252114909, 3.153297935164228,
                                              -0.6940390052764112, -1.0558177183608104], 0], [
                                             [-1.0851787724151578, -0.6482073005808259, -0.9825587319821153,
                                              -0.5797596608429001, -0.2796720337369327, -1.0123463772472525,
                                              0.016115036197288515, 0.7210074353175848, -0.11678881241348991,
                                              0.23134633509213706, 0.5098827030132694], -1.0], [
                                             [-0.1089736606129007, -0.3727343005203817, -0.028853220878974562,
                                              -0.4822031942117363, -0.669673401883848, -0.2923940067114909,
                                              1.730754887588784, -0.21728991201351852, -0.11678881241348991,
                                              -0.6940390052764112, 0.5098827030132694], -0.0], [
                                             [-0.4238785353878224, -0.4951667449916902, -0.28609332991125574,
                                              -0.6470573347536706, 2.255336859218017, -0.7489491685146568,
                                              0.5060121365948587, 1.4716453131824676, 2.2189874358563086,
                                              -0.23134633509213706, 0.11845759766974952], 0.3333333333333333], [
                                             [-0.45536902286531455, -0.09726130045993756, -0.41195780938999377,
                                              -0.05668714352764477, -0.8646740859573058, -0.1958150301762058,
                                              -1.2086277147966367, -0.5926088509459598, 0.8175216868944295,
                                              -1.1567316754606853, 0.11845759766974952], -0.3333333333333333], [
                                             [-1.3843384034513335, -0.00543696710645618, -1.4330794614496143,
                                              -0.11258554407010571, -0.2796720337369327, -0.7226094476413972,
                                              -0.7187306143990666, -0.7802683204121805, -1.0510993117214094,
                                              1.6194243456449595, 0.5098827030132694], -0.5], [
                                             [-0.014502198180424211, 0.14760358848267946, -0.07831442473199217,
                                              0.16118907794854914, 1.2803334388507288, -0.08167623972541431,
                                              2.2206519879863538, -0.21728991201351852, 0.8175216868944295,
                                              0.6940390052764112, 0.11845759766974952], -0.2], [
                                             [0.3161479203332435, -0.5104708005506038, 0.459195416303319,
                                              -0.29045793765267286, -0.8646740859573058, -0.02899679797889517,
                                              -0.9636791645978516, -0.029630442547297846, 1.2846769365483892,
                                              -0.6940390052764112, -1.0558177183608104], 0.0], [
                                             [-0.030247441919170295, -0.785943800611048, 0.16729482874563326,
                                              -0.5834105462500823, 0.8903320707038134, -0.5470113084863334,
                                              0.2610635863960736, -0.21728991201351852, 0.8175216868944295,
                                              0.6940390052764112, 0.5098827030132694], 0.3333333333333333], [
                                             [-0.061737929396662464, -0.03604507822428331, -0.24360492294683708,
                                              -0.2647840776683956, -0.4746727178103904, 0.0939218994296495,
                                              -0.47378206420028157, -0.7802683204121805, -1.0510993117214094,
                                              -1.1567316754606853, -1.4472428237043302], -0.5], [
                                             [-1.3528479159738414, -0.8318559672877885, -1.405697003981372,
                                              -1.0042578170077292, -0.8646740859573058, -1.1001454468247844,
                                              -0.7187306143990666, -1.155587259344622, -0.11678881241348991,
                                              -0.6940390052764112, 0.11845759766974952], -0.42857142857142855], [
                                             [-0.7387834101627441, 0.14760358848267946, -0.769296439329182,
                                              0.1508735723985339, 0.8903320707038134, -0.43287251803554194,
                                              1.730754887588784, -0.4049493814797392, 0.3503664372404698,
                                              1.6194243456449595, -0.6643926130172904], 1.0], [
                                             [1.2136268134417703, -0.5869910783451716, 1.2844560599184986,
                                              -0.6629016750763983, -0.2796720337369327, 0.32219948033123247,
                                              -0.9636791645978516, 0.9086669047838055, 2.6861426855102684,
                                              -0.6940390052764112, -0.6643926130172904], 1.0], [
                                             [-1.3213574284963492, -0.5869910783451716, -1.4107723630572542,
                                              -0.5969677947225062, 0.11032933440998265, -1.0913655398670312,
                                              2.465600538185139, -0.7802683204121805, -0.5839440620674496,
                                              -0.6940390052764112, -0.6643926130172904], -0.0], [
                                             [-0.9749620662439352, -0.6482073005808259, -1.2939384903313387,
                                              -1.0506176132138672, -0.2796720337369327, -0.7665089824301632,
                                              -0.7187306143990666, -2.4692035456081665, 0.8175216868944295,
                                              -1.1567316754606853, 0.5098827030132694], 0.3333333333333333], [
                                             [1.1349005947480397, 0.652637421926827, 0.7554749981468415,
                                              0.48690598141410946, -0.669673401883848, 1.1123911065290195,
                                              -0.7187306143990666, -1.3432467288108425, 0.3503664372404698,
                                              1.1567316754606853, -0.6643926130172904], 0.6666666666666666], [
                                             [3.291998986956253, 5.504023034102427, 2.5764241763170794,
                                              4.7255075947072145, 0.6953313866303557, 4.922870726193905,
                                              -1.2086277147966367, 0.5333479658513642, -0.11678881241348991,
                                              1.1567316754606853, 1.6841580190438292], 0.5], [
                                             [0.5365813326756886, 0.07108331068811163, 0.8826292251093256,
                                              -0.05385127163386341, -0.8646740859573058, 0.28707985250021967,
                                              0.7509606867936437, 1.846964252114909, -1.0510993117214094,
                                              -0.6940390052764112, 0.5098827030132694], 1.0], [
                                             [0.6782885263244034, -0.23499780049015964, 0.8826874713677106,
                                              -0.14326681207459366, -0.08467134966347503, 0.08514199247189631,
                                              1.4858063373899988, 2.2222831910473504, 0.3503664372404698,
                                              -0.23134633509213706, 0.11845759766974952], 0.0], [
                                             [-0.9119810912889509, 0.3771644218663829, -1.0671053647745454,
                                              0.37094789902589126, 0.6953313866303557, -0.3099538206269973,
                                              -0.47378206420028157, 0.34568849638514354, -0.5839440620674496,
                                              1.1567316754606853, -1.0558177183608104], -0.5], [
                                             [-0.3294070729553459, -0.7400316339343073, -0.44371118333303466,
                                              -0.7994951143659185, -0.8646740859573058, -0.5206715876130739,
                                              -0.7187306143990666, -0.7802683204121805, 0.8175216868944295,
                                              -0.6940390052764112, 0.5098827030132694], -1.0], [
                                             [0.1586954829457827, 0.5455090330144321, 0.5733377615839486,
                                              1.180300701215438, 0.3053300184834403, 0.2782999455424665,
                                              0.2610635863960736, 0.34568849638514354, 1.2846769365483892,
                                              0.23134633509213706, 2.467008229730869], -1.0], [
                                             [-0.8017643851177283, -1.199153300701714, -0.6871022498257859,
                                              -1.236674086980587, 0.11032933440998265, -1.0913655398670312,
                                              0.016115036197288515, -0.029630442547297846, -1.0510993117214094,
                                              -1.1567316754606853, -0.2729675076737704], 1.0], [
                                             [-0.48685951034280667, -0.4492545783149495, -0.3800803262484214,
                                              -0.5010295498624295, 0.500330702556898, -0.6348103780638653,
                                              2.955497638582709, -0.4049493814797392, 0.3503664372404698,
                                              -1.1567316754606853, 0.5098827030132694], 0], [
                                             [-0.5655857290365371, -0.7400316339343073, -0.407238416998286,
                                              -0.7633342973610617, -0.669673401883848, -0.5645711224018398,
                                              -0.9636791645978516, -0.9679277898784012, -0.5839440620674496,
                                              -1.1567316754606853, -1.4472428237043302], -1.0], [
                                             [2.3000486314152497, 2.3054754222894918, 2.658162037689258,
                                              2.9879552885208476, 1.8653354910711017, 2.3766977084454792,
                                              -0.47378206420028157, 2.03462372158113, 0.8175216868944295,
                                              0.6940390052764112, 1.6841580190438292], -0.0], [
                                             [0.17444072668452879, -1.1226330229071464, 0.314421379074222,
                                              -1.243831647397924, -0.8646740859573058, -0.4767720528243079,
                                              0.016115036197288515, 0.15802902691892284, -1.0510993117214094,
                                              0.23134633509213706, -1.0558177183608104], -0.0], [
                                             [-0.8017643851177283, -1.1379370784660598, -0.8071740447378942,
                                              -1.1801575758785166, -0.8646740859573058, -1.0474660050782654,
                                              0.9959092369924287, -0.4049493814797392, -1.0510993117214094,
                                              0.23134633509213706, -0.6643926130172904], 0.2], [
                                             [0.48934560145945044, 0.34655631074855575, 0.37622916899346126,
                                              0.4391732851934555, 0.6953313866303557, 0.3573191081622452,
                                              1.9757034377875689, 0.5333479658513642, -0.5839440620674496,
                                              -0.6940390052764112, 0.5098827030132694], -1.0], [
                                             [0.8829766949281025, 0.07108331068811163, 1.173996248628873,
                                              0.09911584064054527, -0.4746727178103904, 0.5680368751483218,
                                              -0.9636791645978516, 0.15802902691892284, 0.3503664372404698,
                                              -0.23134633509213706, 0.5098827030132694], 1.0], [
                                             [0.0642240205133062, 1.0964550331353204, 0.2402269415315634,
                                              1.3695796313352722, 2.4503375432914747, 0.5416971542750623,
                                              0.016115036197288515, -0.7802683204121805, -0.11678881241348991,
                                              -1.1567316754606853, 3.249858440417909], -1.0], [
                                             [1.0404291323155634, -0.12786941157776469, 1.0621482306645695,
                                              0.0035593789453336076, 0.6953313866303557, 0.31341957337347925,
                                              2.955497638582709, 0.9086669047838055, 0.8175216868944295,
                                              0.23134633509213706, -0.2729675076737704], -0.3333333333333333], [
                                             [-1.0536882849376656, -0.5257748561095174, -0.8619720314848515,
                                              -0.4103872949857907, -0.8646740859573058, -0.7665089824301632,
                                              -0.22883351400149654, -0.4049493814797392, -1.518254561375369,
                                              -1.1567316754606853, -0.2729675076737704], 0], [
                                             [0.016988289297067954, 0.16290764404159302, -0.19655315482709557,
                                              0.15839992319591137, 1.4753341229241863, 0.06758217855638993,
                                              -0.22883351400149654, -0.029630442547297846, 0.3503664372404698,
                                              -0.6940390052764112, -0.6643926130172904], 0.0], [
                                             [0.41061938276572, -0.4951667449916902, 0.47339655119798807,
                                              -0.4420272640688677, 1.8653354910711017, -0.2836140997537377,
                                              1.2408577871912136, 1.846964252114909, 1.2846769365483892,
                                              0.6940390052764112, -1.0558177183608104], 1.0], [
                                             [-1.9196766905687002, -1.627666856351294, -1.9827285174704412,
                                              -1.7310273037876975, -1.839677506324594, -1.7761982825717801,
                                              -0.22883351400149654, -1.718565667743284, -0.5839440620674496,
                                              -0.6940390052764112, -1.4472428237043302], 0.0], [
                                             [0.3161479203332435, 1.3413199220779375, 0.29125003210492023,
                                              1.8135123659029846, -0.2796720337369327, 0.9631326882472153,
                                              -0.47378206420028157, -0.9679277898784012, 0.3503664372404698,
                                              1.1567316754606853, 1.2927329137003094], -0.0], [
                                             [-0.43962377912656847, 0.19351575515942016, -0.09094410717105378,
                                              0.22262991005807656, -0.2796720337369327, -0.08167623972541431,
                                              -0.47378206420028157, -0.029630442547297846, 0.3503664372404698,
                                              -1.1567316754606853, -0.2729675076737704], 0.0], [
                                             [1.8906722942078518, 1.111759088694234, 1.5768640458954581,
                                              0.9718680085577392, 2.255336859218017, 1.5162668265856665,
                                              0.5060121365948587, 0.5333479658513642, 0.3503664372404698,
                                              -0.23134633509213706, 1.2927329137003094], 0.42857142857142855], [
                                             [-0.8175096288564744, -0.14317346713667825, -0.7824187378375699,
                                              0.05075065253643934, 0.500330702556898, -0.573351029359593,
                                              1.4858063373899988, 0.15802902691892284, -0.11678881241348991,
                                              -1.1567316754606853, -1.0558177183608104], -0.6], [
                                             [0.9302124261443407, 0.8975023108694441, 0.7830489261191785,
                                              0.5689358506878142, 0.11032933440998265, 0.989472409120475,
                                              0.5060121365948587, -0.029630442547297846, -1.0510993117214094,
                                              2.5448096860135077, -0.2729675076737704], -0.0], [
                                             [0.17444072668452879, -0.11256535601885112, 0.11778092426441701,
                                              -0.18716423341136296, 0.500330702556898, 0.0939218994296495,
                                              -0.47378206420028157, -0.029630442547297846, -1.0510993117214094,
                                              -0.6940390052764112, -1.4472428237043302], 0.5], [
                                             [0.6940337700631495, 1.815745644404258, 0.7040115458206871,
                                              1.7968543680056128, -0.669673401883848, 1.454807477881394,
                                              0.016115036197288515, -0.5926088509459598, 0.8175216868944295,
                                              1.1567316754606853, -0.2729675076737704], 1.0], [
                                             [-1.5260455971000482, -1.2144573562606278, -1.502845647832312,
                                              -1.2176415820577469, -1.839677506324594, -1.3196431207686141,
                                              -0.7187306143990666, -1.5309061982770633, -1.518254561375369,
                                              -0.6940390052764112, -0.2729675076737704], 0.0], [
                                             [0.9617029136218329, -0.21969374493124608, 0.805264322524234,
                                              -0.3289158464286105, -0.8646740859573058, 0.4802378055707899,
                                              -0.47378206420028157, -0.4049493814797392, -0.11678881241348991,
                                              -0.23134633509213706, 0.5098827030132694], 0.5], [
                                             [-0.14046414809039287, -0.020741022665369743, -0.21169332071278402,
                                              -0.010607401933778987, -0.669673401883848, 0.023682643767623975,
                                              -0.7187306143990666, -0.4049493814797392, 0.8175216868944295,
                                              -1.1567316754606853, -1.4472428237043302], -1.0], [
                                             [-0.943471578766443, 0.5914211996911728, -0.9158012290410726,
                                              0.8456315118516691, -1.254675454104221, -0.204594937133959,
                                              0.016115036197288515, 1.283985843716247, -0.11678881241348991,
                                              0.23134633509213706, 0.5098827030132694], -0.6666666666666666], [
                                             [0.22167645790076704, -0.15847752269559182, 0.2461310355638118,
                                              -0.13969692633103553, 0.8903320707038134, 0.006122829852117593,
                                              0.2610635863960736, -0.029630442547297846, -1.518254561375369,
                                              0.23134633509213706, 0.11845759766974952], 1.0], [
                                             [0.5050908451981965, 2.030002422229048, 0.32813715630541923,
                                              2.0929775134728317, 0.6953313866303557, 1.3494485943883558,
                                              -0.22883351400149654, -0.029630442547297846, 0.3503664372404698,
                                              2.5448096860135077, 0.9013078083567895], 1.0], [
                                             [-1.9826576655236845, -1.1226330229071464, -2.018146616098207,
                                              -1.078707606932551, -2.2296788744715093, -1.5567006086279502,
                                              -0.7187306143990666, -0.21728991201351852, -1.0510993117214094,
                                              -0.23134633509213706, -1.4472428237043302], -0.5], [
                                             [-0.943471578766443, -0.12786941157776469, -1.284453024042731,
                                              -0.0020256261707184936, 1.2803334388507288, -0.7226094476413972,
                                              -0.22883351400149654, 1.283985843716247, 0.3503664372404698,
                                              1.1567316754606853, -0.6643926130172904], -1.0], [
                                             [0.7097790138018956, -0.7553356894932208, 0.9638605124102073,
                                              -0.777103754821941, 0.500330702556898, 0.023682643767623975,
                                              0.2610635863960736, -0.9679277898784012, -0.5839440620674496,
                                              -1.1567316754606853, -0.6643926130172904], 1.0], [
                                             [1.0719196197930554, -0.05134913378319687, 1.0760812525509362,
                                              -0.412469748090281, -0.2796720337369327, 0.6470560377681005,
                                              -0.9636791645978516, -0.4049493814797392, -1.0510993117214094,
                                              0.6940390052764112, -0.2729675076737704], 1.0], [
                                             [-0.6758024352077597, -0.7706397450521344, -0.8521564488275363,
                                              -0.8757722430091369, -0.08467134966347503, -0.7401692615569037,
                                              0.7509606867936437, -0.7802683204121805, -1.518254561375369,
                                              -0.23134633509213706, -1.4472428237043302], -0.3333333333333333], [
                                             [-0.8332548725952205, -0.26560591160798674, -0.8707246636543572,
                                              -0.061393951095577735, 1.2803334388507288, -0.7401692615569037,
                                              0.016115036197288515, 1.4716453131824676, -0.5839440620674496,
                                              -0.6940390052764112, 0.9013078083567895], -1.0], [
                                             [1.0719196197930554, 1.5249685887849, 1.0580685995102865,
                                              1.390132092686676, -0.4746727178103904, 1.5250467335434195,
                                              -0.9636791645978516, -0.5926088509459598, -0.5839440620674496,
                                              2.0821170158292337, 0.11845759766974952], 1.0], [
                                             [-0.12471890435164679, 0.43838064410203714, -0.25734696290665215,
                                              0.39890417692243885, 0.3053300184834403, 0.15538124813392185,
                                              -0.22883351400149654, -0.7802683204121805, 0.8175216868944295,
                                              1.1567316754606853, 0.9013078083567895], 0.3333333333333333], [
                                             [0.1586954829457827, -0.3727343005203817, 0.20379392594165296,
                                              -0.3568911618574732, 0.3053300184834403, -0.16069540234519303,
                                              -0.9636791645978516, 0.9086669047838055, 0.3503664372404698,
                                              0.6940390052764112, -0.2729675076737704], -0.3333333333333333], [
                                             [-0.014502198180424211, 0.5761171441322592, 0.03814239221477144,
                                              0.6232254838258547, 1.2803334388507288, 0.14660134117616863,
                                              -0.9636791645978516, 0.9086669047838055, 1.7518321862023487,
                                              1.1567316754606853, 2.467008229730869], 1.0], [
                                             [-0.3294070729553459, -0.4186464671971224, -0.3111789841109183,
                                              -0.45068395026245334, -0.2796720337369327, -0.31873372758475044,
                                              -0.9636791645978516, -0.9679277898784012, -1.0510993117214094,
                                              -0.23134633509213706, 0.5098827030132694], 1.0]]

Huskies_win_match_list = [1, 6, 11, 14, 15, 17, 18, 25, 27, 30, 31, 35, 36]
Huskies_tie_match_list = [2, 8, 12, 16, 19, 20, 24, 33, 34, 37]
Huskies_loss_match_list = [3, 4, 5, 7, 9, 10, 13, 21, 22, 23, 26, 28, 29, 32, 38]
Huskies_data = []
for i in range(38):
    if i + 1 in Huskies_win_match_list:
        Huskies_data.append(winner_learning_data[i][0])
    elif i + 1 in Huskies_loss_match_list:
        Huskies_data.append(losser_learning_data[i][0])
    else:
        Huskies_data.append(winner_learning_data[i][0])
print(Huskies_data)
# result
Huskies_data = [[222, 147, 5597.194401219097, 3447.080364039, 13, 329, 1, 15, 4, 2, 5],
                [104, 76, 2430.9166831688362, 1782.631711499596, 10, 150, 4, 14, 1, 0, 1],
                [209, 115, 4753.8814212369525, 2522.5313746149436, 4, 294, 6, 13, 7, 0, 0],
                [176, 178, 4728.283765154024, 5001.235031318259, 17, 296, 6, 16, 6, 3, 10],
                [196, 186, 4317.224377699875, 4380.2161367383305, 16, 342, 8, 8, 4, 2, 2],
                [192, 126, 4550.401485633126, 3263.3278539713288, 14, 267, 1, 22, 1, 7, 6],
                [170, 214, 4246.406723915734, 5273.3149904354705, 28, 326, 5, 10, 3, 0, 12],
                [186, 109, 4563.1658154723555, 2887.085558467931, 11, 261, 1, 14, 6, 1, 1],
                [80, 88, 1865.4184364674381, 1861.0302977485378, 11, 139, 2, 8, 3, 1, 4],
                [195, 164, 4538.664368080263, 3828.0710307341005, 13, 313, 5, 18, 1, 2, 7],
                [115, 68, 2731.2398248812897, 1608.1822962726662, 11, 145, 9, 12, 1, 3, 2],
                [69, 63, 1724.8835206341985, 1554.3007212746597, 6, 114, 2, 6, 0, 1, 3],
                [114, 133, 2767.050772247689, 3377.5575788365995, 18, 199, 11, 15, 3, 0, 1],
                [200, 147, 5175.703801826598, 3227.197011847874, 11, 297, 8, 24, 1, 1, 5],
                [119, 152, 2786.033447077865, 3521.4797783414665, 20, 215, 12, 12, 4, 6, 2],
                [44, 36, 1030.6865043805801, 816.3318089862648, 6, 62, 4, 5, 2, 1, 0],
                [211, 93, 5293.212720853517, 2187.5540577554707, 18, 267, 6, 9, 2, 0, 2],
                [177, 135, 4069.2767090371235, 3035.5656180775663, 18, 275, 3, 14, 1, 1, 0],
                [135, 113, 3349.0722248159454, 2584.3983253722895, 18, 192, 17, 12, 4, 0, 5],
                [136, 94, 3261.4859213216605, 2155.0632052387446, 13, 179, 2, 24, 10, 1, 1],
                [232, 134, 5435.395418056287, 3309.7222430111688, 19, 300, 17, 19, 5, 3, 3],
                [145, 94, 3257.0240315493083, 2155.3674842924493, 11, 205, 2, 10, 5, 1, 5],
                [115, 121, 2509.570270588189, 2600.0086253723657, 11, 185, 2, 28, 4, 5, 1],
                [167, 153, 3614.562040900074, 3532.2985695083216, 23, 272, 4, 14, 4, 1, 2],
                [139, 110, 3485.033511521388, 2374.489944560798, 27, 179, 7, 22, 8, 2, 4],
                [106, 181, 2574.1000893367336, 4520.163105868153, 9, 241, 5, 21, 3, 3, 5],
                [174, 109, 4513.021566875792, 2784.2880139598565, 11, 241, 2, 22, 1, 2, 4],
                [113, 125, 2639.3077038907095, 3216.354748959563, 22, 180, 5, 22, 2, 1, 6],
                [96, 124, 2285.113909924069, 2887.929187926763, 24, 168, 11, 9, 0, 1, 7],
                [180, 132, 4254.9475673593815, 3103.79773964357, 20, 265, 6, 14, 0, 3, 4],
                [158, 171, 3526.617913602203, 3878.012630127751, 17, 282, 4, 10, 5, 5, 6],
                [40, 69, 979.4507967852833, 1754.0120692209036, 4, 87, 2, 13, 1, 2, 0],
                [99, 108, 2651.9692334448237, 2714.6924948581063, 11, 177, 4, 12, 0, 0, 3],
                [209, 127, 5175.7880606766985, 3098.6661892562897, 15, 274, 11, 26, 4, 2, 4],
                [243, 104, 5756.985209069811, 2351.7144171182154, 14, 301, 1, 19, 9, 1, 2],
                [192, 110, 4583.709131550148, 2669.211460655603, 25, 232, 10, 24, 6, 4, 1],
                [138, 155, 3767.3357496750814, 3624.6262902350445, 14, 255, 3, 14, 4, 0, 3],
                [108, 167, 2355.224013072094, 3837.8267365243455, 19, 229, 3, 16, 2, 5, 1]]

# calculate the average data of Huskie
Huskies_mean_data = []
Huskies_data = np.transpose(np.array(Huskies_data)).tolist()
for i in range(len(Huskies_data)):
    Huskies_mean_data.append(mean(Huskies_data[i]))
print('Huskies_mean_data', Huskies_mean_data)
# result
Huskies_mean_data = [150.10526315789474, 124.5, 3609.088398500058, 2966.508860596589, 15.052631578947368,
                     229.8684210526316, 5.578947368421052, 15.421052631578947, 3.3421052631578947, 1.9210526315789473,
                     3.4210526315789473]

Training_result_list = [129.0776809068127, 77.9958890234888, 5314.844617894659, 1868.8745314494613, 13.726945784017213,
                        186.53819822598442, 0.9711863561572205, 10.432631199340484, 1.14508868180727,
                        2.4371190073318174, 1.7708923457618795]

# define the fonction to get Euclidean distance
def Euclidean_distance(lst1, lst2):
    q_1 = np.array(lst1)
    q_2 = np.array(lst2)
    q = q_1 - q_2
    s = 0
    for ele in q:
        s += ele ** 2
    return np.sqrt(s)


Euclidean_distance_list_of_huskie = []
for ele in Huskies_data:
    q = Euclidean_distance(ele, Training_result_list)
    Euclidean_distance_list_of_huskie.append(q)
print(Euclidean_distance_list_of_huskie)
# result
Euclidean_distance_list_of_huskie = [1613.7492676097716, 2885.5655277777055, 872.59483507480024, 3190.6235989305692,
                                     2709.6980535598191, 1594.2972405748437, 3573.7557099082414, 1269.4751181959066,
                                     3450.1298499797763, 2113.9402380694833, 2597.127727678198, 3604.9907983428761,
                                     2961.57656900045, 1373.5526590665863, 3022.0130081902962, 4414.3485225601025,
                                     339.83436261895179, 1710.5611180313199, 2092.3259186119872, 2073.3580244964605,
                                     1455.1812545746602, 2077.8812050265878, 2899.3971007705395, 2381.6855309258126,
                                     1898.7979474754768, 3815.1388728401903, 1219.4239977817886, 2996.1559541200932,
                                     3197.11332564027, 1631.0017878812034, 2693.1485763175083, 4338.9932234334619,
                                     2794.3222897862643, 1244.3956949949959, 674.91922689171054, 1087.4593501288221,
                                     2342.6857903742052, 3556.173044954483]
# normalization
max = 0
for i in range(len(Euclidean_distance_list_of_huskie)):
    if Euclidean_distance_list_of_huskie[i] > max:
        max = Euclidean_distance_list_of_huskie[i]
for i in range(len(Euclidean_distance_list_of_huskie)):
    Euclidean_distance_list_of_huskie[i] = Euclidean_distance_list_of_huskie[i] / max
    if Euclidean_distance_list_of_huskie[i] < 0.4:
        Euclidean_distance_list_of_huskie[i] = 1
    elif Euclidean_distance_list_of_huskie[i] < 0.6:
        Euclidean_distance_list_of_huskie[i] = 0
    else:
        Euclidean_distance_list_of_huskie[i] = -1
print(Euclidean_distance_list_of_huskie)
# result
Euclidean_distance_list_of_huskie = [1, -1, 1, -1, -1, 1, -1, 1, -1, 0, 0, -1, -1, 1, -1, -1, 1, 1, 0, 0, 1, 0, -1, 0,
                                     0, -1, 1, -1, -1, 1, -1, -1, -1, 1, 1, 1, 0, -1]

win_loss_dict = {'win': 1, 'tie': 0, 'loss': -1}
win_loss_list = []
for i in range(38):
    q = matches_data[i:i + 1]
    q_value = win_loss_dict[q['Outcome'][i]]
    win_loss_list.append(q_value)
print(win_loss_list)

error = []
for i in range(38):
    q = Euclidean_distance_list_of_huskie[i] - win_loss_list[i]
    error.append(q)
print(error)
