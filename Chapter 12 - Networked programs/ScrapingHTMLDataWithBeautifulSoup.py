import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
#url = 'http://python-data.dr-chuck.net/comments_42.html'
url = 'http://python-data.dr-chuck.net/comments_260258.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

sumTotal = []
# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print 'TAG:',tag
    #print 'URL:',tag.get('span', None)
    #print 'Contents:',tag.contents[0]
    #print 'Attrs:',tag.attrs
    num = int(tag.contents[0])
    sumTotal.append(num)
print sum(sumTotal)