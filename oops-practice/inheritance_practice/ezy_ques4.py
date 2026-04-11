#Employee → Manager
# What to do:
#Store salary in parent class and print it using child class.

class employee:
    def __init__(self,salary):
       self.salary=salary

class manager(employee):
    def __init__(self,salary,name):
        super().__init__(salary)
        self.name=name

m=manager(32000,"akshat")
print("the salary is:" ,  m.salary)
print("th employee name is:" , m.name)
    