word = 'brontosaurus'
# count = dict()
# Letter = list()
# for i in word:
#     Letter.append(i)
#
# for x in Letter:
#     count[x] = count.get(x, 0) + 1
#
# print(count)


d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
print(d)
