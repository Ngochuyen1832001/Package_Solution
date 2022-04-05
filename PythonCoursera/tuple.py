import re
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
lst = list()
sum = 0
for line in fh:
    line = line.rstrip()
    y = re.findall('[0-9]+', line)
    if len(y)!=0:
        for x in y:
            sum += int(x)
print(sum)
#print(y)
#     line = line.rstrip()
#     wds = line.split()
#     if len(wds)<3 or wds[0]!= "From":
#         continue
#     lst.append(wds[5][0:2])
# lst.sort(lst)
