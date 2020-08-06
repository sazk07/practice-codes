import urllib.request, urllib.parse, urllib.error
count = dict()
filehandle = urllib.request.urlopen ('http://data.pr4e.org/romeo.txt')
for line in filehandle:
    words = line.decode().split()
    for x in words:
        count[x] = count.get(x,0) + 1
print (count)
