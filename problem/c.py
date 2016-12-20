import urllib
import os
from BeautifulSoup import BeautifulSoup as bs
#list=[]
URL = 'http://localhost:8000/index.html'

def extract_link(uri):
 url = urllib.urlopen(uri)
 content=url.read()
 soup=bs(content)
 lis=[]
 for tag in soup.findAll('a', href=True):
       lis.append(str(tag['href']))
 return lis

def common(p,q):
    for i in q:
        if i not in p:
            p.append(i)


def crawl_web(url):
  le=extract_link(url)
  ad={url:le}
  for i in le:
      ad[i]=extract_link(i)
  return ad

print('---------------------')
print crawl_web(URL)
