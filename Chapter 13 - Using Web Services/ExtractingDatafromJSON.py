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

#address = raw_input('Enter location: ')
#http://python-data.dr-chuck.net/comments_260259.json
serviceurl = 'http://python-data.dr-chuck.net/comments_260259.json'#address


uh = urllib.urlopen(serviceurl)
data = uh.read()
print 'Retrieved',len(data),'characters'

info = json.loads(input)
print info

#sum = 0
#counter = 0

for k in info
print info['comments'][0]['count']

#for item in info:
   # print item
    #count = item['comments']
   # print 'counter:', counter
#sum = sum + int(count)
#    counter = counter + 1

#print 'count:', counter
#print 'sum:', sum

#for item in info:
#    print 'Name', item['name']
#    print 'Id', item['id']
#    print 'Attribute', item['x']
