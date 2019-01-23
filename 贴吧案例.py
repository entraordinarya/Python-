from urllib.request import urlopen,Request
from urllib.parse import urlencode
def get_html(url):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5702.400 QQBrowser/10.2.1893.400"
    }
    request=Request(url,headers=headers)
    response=urlopen(request)
    info=response.read()
    # print(info.decode())
    return info
def save_html(filename,html_bytes):
    with open(filename,"wb") as f:
        f.write(html_bytes)
def main():
    base_html="https://tieba.baidu.com/f?ie=utf-8&"
    content=input("请输入需要爬取的内容:")
    num=input("请输入需要爬取得页数:")
    for pn in range(int(num)):
        args={
            "kw":content,
            "pn":pn
        }
        args=urlencode(args)
        url=base_html+args
        html_bytes=get_html(url)
        filename="第"+str(pn+1)+"页.html"
        print("正在爬取"+filename)
        save_html(filename,html_bytes)
        # print(url)
if __name__ == '__main__':
    main()
