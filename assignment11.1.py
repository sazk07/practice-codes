x=0
import re
fname = input ('Enter filename:')
handle = open (fname)
for line in handle:
    line = line.rstrip()
    findnumbers = re.findall ('[0-9]+',line)
    for numbers in findnumbers:
        x = x + int(numbers)
print (x)