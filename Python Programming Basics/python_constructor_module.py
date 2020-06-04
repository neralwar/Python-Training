
#def _init_(self): constructor defination
#
class Employee:
    def __init__(self, name, age,salary):
        self.name = name
        self.age = age
        self.salary = 20000
   # def _init_(self):

E1 = Employee("XYZ", 23, 20000)
E2 = E1
#E2 = Employee()
# E1 is the instance of class Employee.
#__init__ allocates memory for E1. 
print(E1.name)
print(E1.age)
print(E1.salary)
print(E2.age)
print(E2.salary)