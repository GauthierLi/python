import itchat
import time

# 登录
itchat.login()
i = 0
while i < 10:
    itchat.send('辣鸡，看爸爸炸你{}次'.format(i), toUserName='filehelper')
    time.sleep(1)