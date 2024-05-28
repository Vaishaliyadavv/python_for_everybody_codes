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

total = 0
tags = soup.find_all('span', class_='comments')

for tag in tags:
    total = total + int(tag.text)
print(total)
