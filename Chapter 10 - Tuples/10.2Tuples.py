#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of 
#the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second 
#time using a colon.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = raw_input("Enter file:")

if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)

 

#Dictionary to store distribtion of number of emails per hour of the day

emailsPerHour = dict()

 

for line in handle:

                # remove whitespace

    line = line.rstrip()

    # split using default of spaces

    words = line.split()

    # return to beginning of for loop if empty line or first word isn't 'From'

    if len(words) == 0 or words[0] != 'From' : continue

    # time ccmponent is always the 6th 'word'

    time = words[5]

    # split this using ':' as the delimiter and take first 'word'

    hour = time.split(':')

    hour = hour[0]

    #Add to Hour to dictionary as Key, increment value by 1

    emailsPerHour[hour] = emailsPerHour.get(hour,0) + 1

 

# Create a tuple by iterating through the dictionary. Then order tuple in ascending order

# Dictionaries have a method called items that returns a list of tuples, where each tuple is a key-value pair

#

lst = list()

for key, val in emailsPerHour.items():

    lst.append( (key, val) )  #val, key

 

lst.sort() #reverse=True

 

for key, val in lst :

    print key, val

'''
Raghu's:

fname = raw_input("Enter file name: ")

if len(fname) < 1 : fname = "mbox-short.txt"

timelist = list()

fh = open(fname)

timecounts = dict()

for line in fh:

                if not line.startswith('From '):continue

                words = line.rstrip().split()

                hour = words[5].split(":")

                timelist.append(hour[0])            

for hours in timelist:

                timecounts[hours] = timecounts.get(hours,0)+1

for k,v in sorted(timecounts.items()):

                print k, v
'''