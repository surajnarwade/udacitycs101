import urllib
from BeautifulSoup import BeautifulSoup as bs
URL = 'http://localhost:8000/'

def extract_link(uri):
 url = urllib.urlopen(uri)
 content=url.read()
 soup=bs(content)
 lis=[]
 for tag in soup.findAll('a', href=True):
       lis.append(str(tag['href']))
 return lis

def union(p,q):
    for i in q:
        if i not in p:
            p.append(i)


def crawl_web(url):
  tocrawl=[url]
  crawled=[]
  while tocrawl:
      page=tocrawl.pop()
      if page not in crawled:
         le=extract_link(page)
         union(tocrawl, le)
         crawled.append(page)
  return crawled

print('---------------------')
print crawl_web(URL)
print('---------------------')
b=extract_link(URL)
for i in b:
    print i
print('--------------------')
