import urllib.request, urllib.parse, urllib.error
filehandle = urllib.request.urlopen ('http://www.dr-chuck.com/page1.htm')
for line in filehandle:
    print (line.decode().strip())