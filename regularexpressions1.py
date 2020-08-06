#used in place of if line.find('From:') >= 0: print (line)
import re
handle = open ('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    if re.search ('From:', line):
        print (line)