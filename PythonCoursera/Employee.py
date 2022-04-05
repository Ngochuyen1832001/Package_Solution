from queue import Empty


class Employee:
    numberOfEmployee = 0
    raiseAmount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        Employee.numberOfEmployee +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def display(self):
        print("Name: ", self.fullname())
        print("Pay: ", self.pay)

    def apply_rise(self):
        self.pay = self.pay * self.raiseAmount

    @classmethod
    def from_string(cls, str):
        first, last, pay = str.split("-")
        return cls(first, last, pay)


class Developer(Employee):
    raiseAmount = 1.2

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def display(self):
        super(Developer, self).display()
        print("Program languague: "+self.prog_lang)
    pass


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
    pass

# print(Employee.numberOfEmployee)


emp1 = Employee('Tony', 'Thanh', 300)
# print(emp1.fullname())
# emp1.display()
# emp1.apply_rise()
# Employee.display(emp1)
# print(Employee.numberOfEmployee)
# emp2_str = 'Tony-Tung-3721'
# emp2 = Employee.from_string(emp2_str)
# emp2.display()


dev1 = Developer('Tony', 'Tung', 300, 'Python')
# dev1.apply_rise()
dev1.display()

man1 = Manager("Nguyen Thanh", "Tung", 15000, None)
man1.add_emp(dev1)
man1.print_emps()

man2 = Manager("Nguyen", "Tam", 30000, [emp1])
man2.print_emps()
# hàm isinstance

print(isinstance(man1, Manager)) # trả về true vì man1 là đối tượng của lớp Manager

#hàm issubclass
print(issubclass(Developer, Employee)) # trả về true vì Dev là subclass của Employees
