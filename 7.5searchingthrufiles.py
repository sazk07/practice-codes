fhand = open ('mbox-short.txt')
#count = 0
for line in fhand:
        line = line.rstrip()
#to skip lines starting with From:
    if not line.startswith('From:'):
        continue
    print (line)
    
#another way to write this code
#fhand = open ('mbox-short.txt')
#for line in fhand:
#    line = line.rstrip()
#    if line.startswith('From:')
#    print (line)