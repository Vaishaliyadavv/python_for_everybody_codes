import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter URL: ')

response = urllib.request.urlopen(url)
data = response.read()
tree = ET.fromstring(data)

counts = tree.findall('.//count')
total = 0
for count in counts:
    total = total + int(count.text)

print('Count:', len(counts))
print('Total:', total)
