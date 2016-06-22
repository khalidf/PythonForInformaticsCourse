#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using 
#the split() method. The program should build a list of words. For each word on each line check to see if the word 
#is already in the list and if not append it to the list. When the program completes, sort and print the resulting 
#words in alphabetical order.

#You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

fname = raw_input("Enter file name: ")
#hit enter to set default filename
if len(fname) == 0:
	fname = 'romeo.txt'
fh = open(fname)
finalList = []
for line in fh :
	line.rstrip()
	words = line.split()
	for word in words :
		#print word
		if word not in finalList :
			finalList.append(word)
finalList.sort()
print finalList