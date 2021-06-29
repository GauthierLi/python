'''
wordcount 单词统计
map 阶段
'''


import sys
def map():
    for line in sys.stdin:
        words = line.split("\t")
        for word in words:
            print("\t".join([word.strip(),"1"]))


if __name__=="__main__":
    map()