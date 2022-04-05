import re
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    # thay thế cho hàm find()
    if re.search("From: ", line):
        print(line)
    # thay thế cho startwith()
    if re.search("^From: ", line):
        print(line)

