fname = input('Enter the file name: ')
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for x in fh:
    x = x.rstrip()
    word = x.split()
    if len(word)<3 or  word[0] != "From":
        continue
    else:
        count +=1
print("There are: ",count," email")