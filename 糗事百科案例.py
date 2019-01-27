import requests
import re

url="https://www.qiushibaike.com/text/page/1/"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5702.400 QQBrowser/10.2.1893.400"
}
response=requests.get(url,headers=headers)
response.encoding="utf-8"
# print(response.text)
info=response.text
# print(info)
infos=re.findall(r'<div class="content">\s*<span>\s*(.+)\s*</span>',info)
with open("duanzi.txt","w",encoding='utf-8') as f:
    for info in infos:
        info=re.sub(r'<br/>',r' ',info)
        f.write(info+"\n\n\n")