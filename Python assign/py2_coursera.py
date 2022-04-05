#5.2. Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.


largest = None
smallest = None
while True:
	num = input('Enter a number: ')
	if num == 'done':
		break
#print (num)
	try:
		num = int(num)
		if largest is None or largest < num:
			largest = num
		elif smallest is None or smallest > num:
			smallest = num
	except:
		print("Invalid input")

print ("Maximum is", largest)
print ("Minimum is", smallest)



# 8.4. Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.


fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    line = line.split()
    for c in line:
        if c in lst:
            continue
        else:
            lst.append(c)

lst.sort()
print(lst)







