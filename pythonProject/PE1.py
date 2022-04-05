# Write a program in the python programming language to read data using webservice, printing the total number of men and women
# Webservice: https://api.androidhive.info/contacts/

import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter link: ')
url = urllib.request.urlopen(address, context=ctx)

data = url.read()
js = json.loads(data)
countF = 0
countM = 0

for elem in js['contacts']:
    if elem['gender'] == 'female':
        countF = countF + 1
    elif elem['gender'] == 'male':
        countM = countM + 1

print(countM)
print(countF)
