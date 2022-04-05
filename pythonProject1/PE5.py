# Write a program in the python programming language:
#Enter a person's name to search
#Read Contact list form URL:  https://api.androidhive.info/contacts/
#print 	the search results yes or no and
#       the person's position in the list in case of yes.



import urllib.request, urllib.error, urllib.parse
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sname = input("Enter search name: ")
link = input('Enter link: ')
url = urllib.request.urlopen(link, context=ctx)

data = url.read()
js = json.loads(data)
count = 0
for elem in js['contacts']:
   if elem['name'] == sname:
       count += 1
if count != 0:
    print('Yes, at position %d' %count)
else:
    print('No')