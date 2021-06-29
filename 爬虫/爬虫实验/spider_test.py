# _*_ coding:utf-8 _*_
from urllib import request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
response = request.Request(
    'https://mp.weixin.qq.com/s?src=11&timestamp=1582441190&ver=2175&signature=IQKvAMi3sZh2yKP2SbNingAK1Jhnto2Yb22tfiufJsmThLPvXqAKgAzyFMSy5mQuHwIrMPqEBL*27yG0GEKlJgO9RLUf6YSapR8mBcF8iFApgdt7C0uvENtkj*iFwhf-&new=1',headers = headers)
response = request.urlopen(response)
html = response.read()
html = html.decode('utf-8')
print(html)
