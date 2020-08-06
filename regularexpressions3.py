# looking for lines that begin with the letter X, followed by any number of characters, repeated zero or more times
# followed by a :
import re
handle = open ('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    if re.search ('^X.*:',line):
        print (line)