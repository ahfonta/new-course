import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
total = 0
suma = 0
url = input('Enter link:')
html = urllib.request.urlopen(url).read()
tree = ET.fromstring(html)
counts = tree.findall('.//count')
for n in counts:
    total = total + int(n.text)
    suma = suma +1
print('Total: ', total)
print ('Number:',suma)
