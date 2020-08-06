#used in place of if line.startswith('From:'): print (line)
import re
handle = open ('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    if re.search ('^From:',line):
        print(line)