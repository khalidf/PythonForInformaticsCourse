'''
The basic outline of this problem is to read the file, look for integers using the re.findall(), 
looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers. 
'''
import re

fhand = raw_input("Enter file:")
if len(fhand) < 1 : fhand = "regex_sum_260253.txt"
handle = open(fhand).read()

numbers = re.findall('[0-9]+', handle)

numbersCount = []

for num in numbers:
	numbersCount.append(int(num))

print sum(numbersCount)