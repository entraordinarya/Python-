import requests
from bs4 import BeautifulSoup
def gethtml(url):
    html=requests.get(url)
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
