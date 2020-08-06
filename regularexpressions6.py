# find all lines beginning with From followed by a space and then non-whitespace with an @ in the middle followed by non-whitespace 
import re
handle = open ('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    if re.findall ('^From (\s@\s+)',line):
        print (line)