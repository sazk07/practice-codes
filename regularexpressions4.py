# searches for any line that starts with X- 
# followed by no space
# repeats one or more time
import re
handle = open ('mbox-short.txt')
for line in handle:
    line = line.strip()
    if re.search ('^X-\S+:',line):
        print (line)