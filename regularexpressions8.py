import re
handle = open ('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    if re.findall ('From .*@([^ ]*)',line):
        print (line)