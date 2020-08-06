d = dict()
maxmention = 0
whichaddress = None
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        d[words[1]] = d.get(words[1],0) + 1
for k,v in d.items():
    if v > maxmention:
        maxmention = v
        whichaddress = k
print(whichaddress,maxmention)