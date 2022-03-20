# employee.py
# This program defines the class Employee for storing the data of the
# employee in a company.

class Employee:
    count = 0

    def __init__(self, lastname, firstname, staffnum, salary):
        self.lastname = lastname
        self.firstname = firstname
        self.staffnum = staffnum
        self.salary = salary
        Employee.count += 1

    def display(self):
        print("Last name =", self.lastname)
        print("First name =", self.firstname)
        print("Staff number =", self.staffnum)
        print("Salary =", self.salary)

    @staticmethod
    def getcount():
        return Employee.count
