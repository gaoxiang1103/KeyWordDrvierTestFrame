import urllib
import urllib.request
import re
import random

url = "http://www.qiushibaike.com/"
# opener = urllib.request.build_opener()
# UA = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36")
# opener.addheaders=[UA]
# urllib.request.install_opener(opener)
# data = urllib.request.urlopen(url).read().decode("utf-8","ignore")

#用户代理池
uapools= [
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
]

def UA():
    opener = urllib.request.build_opener()
    thisua = random.choice(uapools)
    ua = ("User-Agent",thisua)
    opener.addheaders=[ua]
    urllib.request.install_opener(opener)
    print("当前使用的UA: " + str(thisua))
for i in range(0,10):
    UA()
    data = urllib.request.urlopen(url).read().decode("utf-8","ignore")