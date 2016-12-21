import urllib
import os
from BeautifulSoup import BeautifulSoup as bs

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
         crawled.append(page)
         withcount[page]=le
  return crawled, withcount

print('---------------------')
crawl, withcount = crawl_web(URL)
print crawl
print('---------------------')
print withcount

ic={};oc={}

for i in crawl:
 count=0
 for key, value in withcount.iteritems():
   if i in value:
       count=count+1
   oc[i]=count
   ic[key]=len(value)

print 'outgoing count of each unique URL is', ic
print 'incoming count of each unique URL is', oc
