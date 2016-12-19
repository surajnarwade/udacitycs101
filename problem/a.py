
import urllib
import os
from BeautifulSoup import BeautifulSoup as bs
#list=[]
URL = 'http://surajnarwade.github.io'

def extract_link(uri):
 url = urllib.urlopen(URL)
 content=url.read()
 soup=bs(content)
 lis=[]
 for tag in soup.findAll('a', href=True):
       lis.append(tag['href'])
 return lis

def union(p,q):
    for i in q:
        if i not in p:
            p.append(i)


def crawl_web(url):
  tocrawl=[url]
  crawled=[]
  withcount={}
  while tocrawl:
      page=tocrawl.pop()
      if page not in crawled:
         le=extract_link(page)
         union(tocrawl, le)
         crawled.append(page)
        # withcount[page]=le
  return crawled

print('---------------------')
a=crawl_web(URL)
for i in a:
    print i
print('---------------------')
b=extract_link(URL)
for i in b:
    print i
print('--------------------')
print(len(a),len(b))
#a=crawl_web(URL)
#b=list(set(extract_link(URL)))
#print crawl_web(URL)
#print extract_link(URL)
#print(len(a), len(b))
