'''
Pull out all count and sum up

	<commentinfo>
		<note>This file contains the sample data for testing</note>
		<comments>
			<comment>
				<name>Romina</name>
				<count>97</count>
			</comment>
			<comment>
				<name>Laurie</name>
				<count>97</count>
			</comment>

Source used to pull out elements etc:
https://docs.python.org/2/library/xml.etree.elementtree.html

'''

import urllib
import xml.etree.ElementTree as ET

address = raw_input('Enter location: ')
#http://python-data.dr-chuck.net/comments_42.xml
serviceurl = address

url = serviceurl
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data

tree = ET.fromstring(data)

#print tree.tag

sum = 0
counter = 0
for comment in tree.findall('.//comment'):
	count = comment.find('count').text
	sum = sum + int(count)
	counter = counter + 1

print 'count:', counter
print 'sum:', sum 