import urllib
from urlparse import urljoin
from BeautifulSoup import BeautifulSoup as bs

URL = 'http://localhost:8000/index.html'
def extract_link(uri):
 url = urllib.urlopen(uri)
 content=url.read()
 soup=bs(content)
 lis=[]
 for tag in soup.findAll('a', href=True):
       link=tag.get('href')
       if not link.startswith('http'):
              link=urljoin(URL, link)
       lis.append(str(link))
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
         withcount[page]=[le,len(le),0]
  return crawled, withcount

crawl, withcount = crawl_web(URL)

for i in crawl:
 count=0
 for key, value in withcount.iteritems():
   if i in value[0]:
       count=count+1
   withcount[i][2]=count

for i in withcount:
    print '{},outgoing={},incoming={}'.format(i,withcount[i][1],withcount[i][2])
