import re
handle = open ('mbox-short.txt')
numlist = list()
for line in handle:
    line = line.rstrip()
    stuff = re.findall ('X-DSPAM-Confidence: ([0-9).]+)',line)
    if len (stuff) != 1:
        continue
    else:
        num = float (stuff[0])
        numlist.append(num)
print ('Maximum is:',max(numlist))