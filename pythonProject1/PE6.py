#Given a string, the task is to check  if that string contains any special character (defined special character set).
#If any special character is found, don’t accept that string.
#Examples :    Input : Billy$is$goat Father  Output : String is not accepted.
#Input : Billy is a goat Father  Output : String is accepted

import re

ip = input("Enter your string: ")
specialCharacter = re.compile('[~!@#$%^&*()_+{}|/<>?:]')


if (specialCharacter.search(ip) == None):
    print('String is accepted')
else:
    print('String is not accepted')
