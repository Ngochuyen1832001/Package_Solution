import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

jf = urllib.request.urlopen('https://api.androidhive.info/contacts/', context = ctx).read()
data = json.loads(jf)
# print(json.dumps(data, indent = 4))
name = input('Enter Name: ')
contact = data['contacts']
for idx in range(len(contact)):
    if contact[idx]['name'] == name.strip():
        print("Yes, person's position is", idx + 1)
        break
else:
    print('No')
