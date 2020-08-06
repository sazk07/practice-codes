fhand = open ('mbox-short.txt')
for line in fhand:
    line = line.rstrip() #removes \n space that print statement automatically produce
    if line.find('@uct.ac.za') ==-1:  #same as if not '@uct.ac.za' in line
        continue
    print (line)