import ssl
import urllib.request

from bs4 import BeautifulSoup

# Ignore SSL certification errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter- ')

count = int(input('Enter count- '))
position = int(input('Enter position- '))

for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('a')
    next_url = tags[position - 1].get('href', None)
    url = next_url


last_name = url.split('_')[-1].split('.')[0]
print(last_name)
