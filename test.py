import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
result =0
address = input('Enter location: ')

print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx).read()


print('Retrieved', len(uh), 'characters')
#print(uh.decode())
tree = ET.fromstring(uh)
    
counts = tree.findall ('.//count')
print ('Count:',len(counts))
for count in counts:
    value = int(count.text)
    result = result + value 
print ('Sum:',result)
results = tree.findall('result')
    
