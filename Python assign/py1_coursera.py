#2.2 Write a program that uses input to prompt a user for their name and then welcomes them. Note that input will pop up a dialog box.
# Enter Sarah in the pop-up box when you are prompted so your output will match the desired output.

name = input("Enter your name: ")
print("Hello " + name)


#3.3.Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

score = input("Enter Score: ")
scr = float(score)
if scr >= 0.9:
    print("A")
elif scr >= 0.8:
    print("B")
elif scr >= 0.7:
    print("C")
elif scr >= 0.6:
    print("D")
elif scr <0.6:
    print("F")



#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

text = 'X-DSPAM-Confidence:    0.8475';

pos  = text.find(':')

part = text[pos + 1:]
final = part.lstrip()
value = float(final)
print(final)


#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

fname = input("Enter file name: ")
fh = open(fname)

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())



