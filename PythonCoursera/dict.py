fname = input("Enter file name: ")
fh = open(fname)
count = dict()
name = list()
for x in fh:
    x = x.rstrip()
    word = x.split()
    if len(word)<3 or word[0] != 'From':
        continue
    else:
        name.append(word[1])
for i in name:
    count[i] = count.get(i, 0) + 1
BigName = None
BigCount = None
for x, y in count.items():
    if BigCount is None or y>BigCount:
        BigName = x
        BigCount = y
print(BigName, BigCount)