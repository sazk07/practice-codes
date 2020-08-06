fname = input ('Enter filename: ')
try:
    fhand = open (fname)
except:
    print('file cannot be opened:',fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print ('there were',count,'subject lines in',fname)