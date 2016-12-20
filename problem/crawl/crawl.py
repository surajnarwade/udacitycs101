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
         withcount[page]=[le,len(le)]
  return crawled, withcount

print('---------------------')
crawl, withcount = crawl_web(URL)
print crawl
print('---------------------')
print withcount
print('---------------------')
for i in crawl:
    print i
print('-------------------------')

oc={}
for i in crawl:
 count=0
 for key, value in withcount.iteritems():
   if i in value[0]:
       count=count+1
   oc[i]=count

print oc

