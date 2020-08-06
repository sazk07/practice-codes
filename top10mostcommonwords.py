fhand = open ('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for x in words:
        counts[x] = counts.get(x,0) + 1

print (sorted ([(v,k) for k,v in counts.items()]))