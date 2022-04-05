fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Not exits.")
    exit()
count = dict()
Day = list()
for x in fh:
    x = x.rstrip()
    word = x.split()
    if len(word)<3 or word[0] != 'From':
        continue
    else:
        # Bài EX3 thì là word[3]
        word1 = word[1].split("@")
        Day.append(word1[1])
for i in Day:
     count[i] = count.get(i, 0) + 1
print(count)