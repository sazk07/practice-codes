import urllib.request, urllib.parse, urllib.error
import json
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
result = 0

address = input('Enter location: ')

#url = serviceurl + urllib.parse.urlencode (address)
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read().decode()
num = 0
total = 0
loadup = json.loads (data)
#print (data)

for i in range(len(loadup.get('comments'))):
    x = loadup.get ('comments')[i] 
    value = x.get ('count')
    num = num + 1
    total = total + int(value)
#print (num)
print (total)