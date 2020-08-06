fhand = open ('mbox-short.txt')
#count = 0
#for line in fhand:
 #   count = count + 1
#print ('lines are:',count)

inp = fhand.read()
print (len(inp))
print (inp[:20])