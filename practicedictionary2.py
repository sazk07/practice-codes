takein = dict() #initialize dictionary
fileinp = input ('Enter file name: ')
finp = open (fileinp)
count = 0
for linevariable in finp:
    wordvariable = linevariable.split()
    for singlewordvariable in wordvariable:
        count = count + 1
        if singlewordvariable in takein:
            continue
        takein [singlewordvariable] = count
if 'Python' in takein:
    print ('True')
else:
    print ('False')