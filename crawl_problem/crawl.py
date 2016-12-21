import urllib
import argparse
from urlparse import urljoin
from BeautifulSoup import BeautifulSoup as bs

URL = 'http://localhost:8000/index.html'
#URL = 'http://surajnarwade.github.io'


def extract_link(uri):
    url = urllib.urlopen(uri)
    content = url.read()
    soup = bs(content)
    lis = []
    for tag in soup.findAll('a', href=True):
        link = tag.get('href')
        if not link.startswith('http'):
            link = urljoin(URL, link)
        lis.append(str(link))
    return lis


def union(tocrawl, extracted_links):
    for i in extracted_links:
        if i not in tocrawl:
            tocrawl.append(i)


def crawl_web(url):
    tocrawl = [url]
    crawled = []
    withcount = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            links = extract_link(page)
            union(tocrawl, links)
            crawled.append(page)
            withcount[page] = [links, len(links), 0]
    return crawled, withcount

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='basic crawler')
    parser.add_argument('--url',  help='Your URL goes here')
    args = parser.parse_args()
    if args.url:
      crawl, withcount = crawl_web(args.url)

    for i in crawl:
        count = 0
        for key, value in withcount.iteritems():
            if i in value[0]:
                count = count+1
        withcount[i][2] = count

    for i in withcount:
        print '{}, outgoing={}, incoming={}'.format(i, withcount[i][1], withcount[i][2])
