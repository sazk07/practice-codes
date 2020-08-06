# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0

for line in fh:
    
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    else:
        colonseek = line.find(':')
        numberonly = line [colonseek+1:].strip()
        floatconvert = float(numberonly)
        count = count +1
        total = total + floatconvert
avg = total /count
print('Average spam confidence:',avg)
