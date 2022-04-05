name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = dict()
hour = list()
for line in handle:
    line = line.rstrip()
    word = line.split()
    if len(word) < 3 or word[0] != "From":
        continue
    else:
        time = word[5].split(":")
        hour.append(time[0])
for i in hour:
    count[i] = count.get(i, 0) + 1


for x, y in sorted(count.items()):
    print(x, y)
