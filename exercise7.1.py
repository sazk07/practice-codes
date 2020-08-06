fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    uppercase = line.rstrip().upper()
    print (uppercase)