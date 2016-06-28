'''
Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Daniela.html 
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: P
'''

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL - ')
#url = 'http://python-data.dr-chuck.net/known_by_Daniela.html'
count = raw_input('Enter count: ')
#count = 7
position = raw_input('Enter position: ')
#position = 17

loopCounter = 0

print 'Retrieving: ', url

while loopCounter < count:

	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	
	# Retrieve all of the anchor tags
	tags = soup('a')
	url = tags[position].get('href', None)
	
	print 'Retrieving: ', url
	
	loopCounter = loopCounter + 1