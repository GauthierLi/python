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
    for key in dict.keys():
        s += dict[key]
    for key in dict.keys():
        dict[key] = dict[key]/s

dict_test = { '排好队': 1, '同年级': 1, '爱意': 2, '敌不过': 6, '土黄': 2, '映': 3, '羞耻之心': 2}
norm(dict_test)
print(dict_test)