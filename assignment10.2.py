name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    words = line.split()
    if len(words) <2 or words[0] != 'From':
        continue
    else:
        colonposition = words [5].find (':')
        hour = words [5] [:colonposition]
        counts[hour] = counts.get (hour,0) + 1
for k,v in sorted(counts.items()):  
    print (k,v)
        