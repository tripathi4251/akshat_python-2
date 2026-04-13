#Employee → Developer & Designer
# What to do:
#Add role-specific methods in child classes.

class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def role(self):
        print(self.name, "is Developer")

class Designer(Employee):
    def role(self):
        print(self.name, "is Designer")

d1 = Developer("Akshat")
d2 = Designer("Ravi")

d1.role()
d2.role()