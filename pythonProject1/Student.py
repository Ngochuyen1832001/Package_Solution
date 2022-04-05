# Write a program in the python programming language using object-oriented programming techniques.
# The program enters a list of students, each with information on name, age and test scores.
# Sort students by decreasing age. Print the list of students before and after the sorting.

class Student:
    name = ""
    age = 0
    score = 0
    def set_name(self):
        self.name = input("Enter name: ")
    def get_name(self):
        return self.name
    def set_age(self):
        self.age = input("Enter age: ")
    def get_age(self):
        return self.age
    def set_score(self):
        self.score = input("Enter score: ")
    def get_score(self):
        return self.score

lst = []
while(True):
    an = Student()
    an.set_name()
    an.set_age()
    an.set_score()
    lst.append(an)
    con = input("Continue or not?")

    if(con == 'N'):
        break

print("Before sorting: ")
for ele in lst:
    print(ele.get_name() + "\t" + ele.get_age() + "\t" + ele.get_score())

lst.sort(key = lambda x: x.age, reverse=True)

print("After sorting: ")
for ele in lst:
    print(ele.get_name() +"\t"+ ele.get_age() +"\t" + ele.get_score())