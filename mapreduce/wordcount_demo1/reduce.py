'''
wordcount 单词统计
reduce 阶段
'''

import sys
from operator import itemgetter


def reduce():
    word_count_dict = {}
    for line in sys.stdin:
        kv = line.split("\t")
        word = kv[0].strip()
        count = int(kv[1].strip())
        word_count_dict[word] = word_count_dict.get(word, 0) + count

    sorted_word_count = sorted(word_count_dict.items(), key=itemgetter(0))

    for word, count in sorted_word_count:
        print("\t".join([word, str(count)]))


if __name__ == "__main__":
    reduce()
