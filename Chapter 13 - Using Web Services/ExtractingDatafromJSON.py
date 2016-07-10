import json
import urllib

input = '''
{
  "note":"This file contains the actual data for your assignment",
  "comments":[
    {
      "name":"Alana",
      "count":98
    },
    {
      "name":"Skylar",
      "count":96
    }
  ]
}'''

# Note this is a dictionary/list/dictionary! So need to code accordingly..

serviceurl = 'http://python-data.dr-chuck.net/comments_260259.json'

uh = urllib.urlopen(serviceurl)
data = uh.read()
print 'Retrieved',len(data),'characters'

info = json.loads(data)
print type(info) # dict

# extract from the dictionary the value comments which is a list of dictionaries
comments = info['comments']
print type(comments) # list

# now loop round comments like a regular list, with each element a dictionary

sum = 0
counter = 0

for item in info['comments']:
	#print k['count']
	sum = sum + int(item['count'])

print sum