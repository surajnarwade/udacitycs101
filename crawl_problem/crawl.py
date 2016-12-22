import urllib
import argparse
from urlparse import urljoin
from BeautifulSoup import BeautifulSoup as bs

# URL = 'http://localhost:8000/index.html'


def extract_link(uri):
    url = urllib.urlopen(uri)
    content = url.read()
    soup = bs(content)
    lis = []
    for tag in soup.findAll('a', href=True):
        link = tag.get('href')
        if link.startswith('mailto') or link.startswith('javascript'):
            pass
        elif not link.startswith('http'):
            link = urljoin(uri, link)
            lis.append(link.encode('utf-8'))
        else:
            lis.append(link.encode('utf-8'))
    return lis


def union(tocrawl, extracted_links):
    for i in extracted_links:
        if i not in tocrawl:
            tocrawl.append(i)


def crawl_web(url, max_depth):
    tocrawl = [url]
    crawled = []
    next_depth = []
    depth = 0
    withcount = {}
    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()
        if page not in crawled:
            links = list(set(extract_link(page)))
            union(next_depth, links)
            crawled.append(page)
            withcount[page] = [links, len(links), 0]
        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            print "Depth level %d completed" % depth
            depth += 1
    return crawled, withcount

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--depth',  help='Your depth goes here')
    parser.add_argument('--url', help='Your URL goes here')
    args = parser.parse_args()
    try:
        dep = int(args.depth)
        if dep < 0:
            print "depth must be 0 or positive"
    except ValueError:
        print "That is not a valid depth. Try again with integer value"
    else:
        crawl, withcount = crawl_web(args.url, dep)
        for i in crawl:
            count = 0
            for key, value in withcount.iteritems():
                if i in value[0]:
                    count = count+1
            withcount[i][2] = count
        for i in withcount:
            print '{}, outgoing={}, incoming={}'.format(i, withcount[i][1], withcount[i][2])
