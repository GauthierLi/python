from jieba import *
import random

random.seed()


class Que():

    def __init__(self, lenth):
        self.lenth = lenth
        self.queue = []

    def enqueue(self, x):
        if len(self.queue) < self.lenth:
            self.queue.append(x)
        else:
            del self.queue[0]
            self.queue.append(x)


def norm(dict):
    s = 0
    count = 0
    for key in dict.keys():
        if dict[key] > s:
            s += dict[key]
            count += 1
        s = s / count
    for key in dict.keys():
        dict[key] = dict[key] / s


def probability_trigger(p):
    num = random.uniform(0, 1)
    if num <= p:
        return True
    else:
        return False


f1 = open('chijinaiba.txt', encoding='utf-8')
f2 = open('chongsheng.txt', encoding='utf-8')
f3 = open('quannengtoushi.txt', encoding='utf-8')
fwrite = open('dictionary.txt', 'w', encoding='utf-8')
fwrite2 = open('fiction.txt', 'w', encoding='utf-8')
f1_readlines = f1.readlines()
f2_readlines = f2.readlines()
f3_readlines = f3.readlines()
total_readlines = f1_readlines + f2_readlines + f3_readlines
dict_of_word = {}
dict_of_word_after = {}
word_queue = Que(2)
word_queue.enqueue(' ')
for line in total_readlines:
    ls_sep = lcut(line)
    for word in ls_sep:
        word_queue.enqueue(word)
        if word not in dict_of_word.keys():
            dict_of_word[word] = 1
        else:
            dict_of_word[word] = dict_of_word[word] + 1

        if word_queue.queue[0] not in dict_of_word_after.keys():
            dict_of_word_after[word_queue.queue[0]] = {}
        if word not in dict_of_word_after[word_queue.queue[0]].keys():
            dict_of_word_after[word_queue.queue[0]][word] = 1
        else:
            dict_of_word_after[word_queue.queue[0]][word] += 1

norm(dict_of_word)
for key in dict_of_word_after.keys():
    norm(dict_of_word_after[key])

count = 0
check_que = Que(2)
check_que.enqueue(0)
check_que.enqueue(1)
while count < 1000:
    lead = random.choice(list(dict_of_word.keys()))
    if probability_trigger(dict_of_word[lead]):
        while lead != '。' and lead != '!' and lead != ',':
            check_que.enqueue(lead)
            if check_que.queue[0] != check_que.queue[1]:
                fwrite2.write(lead)
                count += 1
            if count > 1000:
                break
            key = random.choice(list(dict_of_word_after[lead].keys()))
            if probability_trigger(dict_of_word_after[lead][key]):
                lead = key
fwrite2.close()

# for key in dict_of_word_after.keys():
#     fwrite.write(key)
#     fwrite.write(':{')
#     for ele in dict_of_word_after[key].keys():
#         fwrite.write(ele)
#         fwrite.write(":")
#         fwrite.write(str(dict_of_word_after[key][ele]))
#         fwrite.write('\t')
#     fwrite.write('}\n\n\n')
# fwrite.close()
