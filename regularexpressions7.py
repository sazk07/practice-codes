# [^ ] means matches any non blank character. * means match many of them
import re
handle = open ('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    if re.findall ('@([^ ]*)',line):
        print(line)