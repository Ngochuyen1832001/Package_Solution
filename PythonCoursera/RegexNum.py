import re
fhand = open("Regex Document.txt")
sum = 0
Num = list()
for line in fhand:
    line = line.strip()
    Num.append(re.findall("[0-9]+", line))
for i in Num:
    if i is not None:
        for j in i:
            sum += int(j)
print(sum)