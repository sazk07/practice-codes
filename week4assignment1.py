from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

y =  0
count = []
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    count.append(tag.contents[0])
for i in range (len (count)):
    y = y + int(count[i])
print (y)