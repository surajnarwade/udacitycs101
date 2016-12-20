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
  tocrawl=[url]
  crawled=[]
  withcount={}
  while tocrawl:
      page=tocrawl.pop()
      if page not in crawled:
         le=extract_link(page)
         common(tocrawl, le)
         #if page!='http://localhost:8000/':
         #   page='http://localhost:8000/'+page
         crawled.append(page)
         withcount[page]=le
  return withcount

print('---------------------')
print crawl_web(URL)
#print a
#for i in a:
#    print i
print('---------------------')
b=extract_link(URL)
for i in b:
    print i
print('--------------------')
#print(len(a),len(b))
#a=crawl_web(URL)
#b=list(set(extract_link(URL)))
#print crawl_web(URL)
#print extract_link(URL)
#print(len(a), len(b))
