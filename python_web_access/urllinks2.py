import ssl
import urllib.request

from bs4 import BeautifulSoup

# Ignore SSL certification errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter- ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
