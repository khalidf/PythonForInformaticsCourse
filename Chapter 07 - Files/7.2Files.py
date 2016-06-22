# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce 
#an output as shown below. 
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

fname = raw_input("Enter file name: ")
#Set the default file name to save typing in each time, just hit enter to use default
if len(fname) == 0 :
	fname = '7.2Files.txt'
fh = open(fname)
lineCount = 0
lineValueTotal = 0.0
for line in fh:
	if not line.startswith("X-DSPAM-Confidence:") : continue
    #strip white space and new lines
	line = line.strip()
    #find first . and got back one position to get the start of the number (assuming only position here!)
	pos1 = line.find('.') - 1
    #convert the string to float and add to the running total
	lineValueTotal = lineValueTotal + float(line[pos1:])	
	
	lineCount = lineCount + 1
	#print line, lineCount, pos1, lineValueTotal
print "Average spam confidence:", lineValueTotal/lineCount