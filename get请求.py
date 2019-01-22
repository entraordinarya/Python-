from urllib.request import urlopen,Request
# from urllib.parse import quote
from urllib.parse import urlencode
args={
    "wd":"百度百科",
    "ie":"utf-8"
}
url="https://www.baidu.com/s?{}".format(urlencode(args))
# print(urlencode(args))
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5702.400 QQBrowser/10.2.1893.400"
}
request=Request(url,headers=header)
response=urlopen(request)
info=response.read()
print(info.decode())