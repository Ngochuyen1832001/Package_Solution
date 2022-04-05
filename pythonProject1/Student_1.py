#Write a program in the python programming language using object-oriented programming techniques.
#The program enters a list of students, each with information on name, age and test scores.
#Sort students by name and order in the alphabet table.
#Print the list of students before and after the sorting.
class Student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Score: ", self.scores)


n = int(input("Enter number of students: "))
A = []
for i in range (n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    scores = float(input("Enter score: "))
    S1 = Student(name, age, scores)
    A.append(S1)
for i in range(n):
    A[i].display()
A.sort(key= lambda x: x.name, reverse=True)
print("After reverse: ")
for i in range(n):
    A[i].display()