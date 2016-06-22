#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of 
#mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who 
#sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the 
#number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary 
#using a maximum loop to find the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle :
	words = line.split()
	if len(words) == 0 or words[0] != 'From' : continue
	if words[1] not in counts :
		counts[words[1]] = 1
	else:
		counts[words[1]] += 1

person = None
numberOfEmails = None
for key,value in counts.items():
	if numberOfEmails is None or value > numberOfEmails:
		person = key
		numberOfEmails = value

print person, numberOfEmails