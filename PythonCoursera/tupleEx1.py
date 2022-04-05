# addr = 'monty@python.org'
# uname, domain = addr.split('@')
# print(uname)
# print(domain)

fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Not exist.")
    exit()
count = dict()
email = list()
for line in fh:
    line = line.rstrip()
    word = line.split()
    if len(word)<3 or word[0] != 'From':
        continue
    else:
        email.append(word[1])
for i in email:
    count[i] = count.get(i, 0) + 1
lst = list()
for y, x in sorted(count.items()):
    lst.append((x, y))
lst.sort(reverse=True)
for x, y in lst[:1]:
    print(y, x)