count = dict()
word = "This Specialization builds on the success of the Python for Everybody course and will introduce fundamental programming concepts including data structures," \
       " networked application program interfaces, and databases, using the Python programming language. In the Capstone Project, you’ll use the technologies learned throughout " \
       "the Specialization to design and create your own  applications for data retrieval, processing, and visualization."
names = word.split()
for name in names:
    count[name] = count.get(name,0)+1
print(count)
for x in count:
    print(x, count[x])
print(list(count))
print(count.keys())
print(count.values())
print(count.items())