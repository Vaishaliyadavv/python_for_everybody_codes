import urllib.request
import json

url = input('Enter URL: ')
response = urllib.request.urlopen(url)
data = response.read()

info = json.loads(data)
total = 0

for comment in info['comments']:
    total = total + comment['count']

print(total)
