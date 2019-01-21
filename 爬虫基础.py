import requests
from bs4 import BeautifulSoup
def gethtml(url):
    try:
    html=requests.get(url)
    except:
        return None
    try:
        soup=BeautifulSoup(html.text)
        title=soup.title
    except AttributeError as e:
        return None
    return title
title=gethtml("http://www.pythonscraping.com/pages/page1.html")
if title==None:
    print("title not found")
else :
    print(title)
