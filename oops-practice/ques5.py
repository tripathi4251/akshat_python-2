#Create a class Employee
#What to do:
#Store name and salary. Create a method to display salary.

class employee:
       def __init__(self,name,salary):
        self.name=name
        self.salary=salary

       def display(self):
           print("the employee name is:" , self.name , "\n his monthly salary is: " , self.salary )

e1 = employee("Akshat" , 300000)
e1.display()

#Create a class Laptop
#What to do:
#Store brand and RAM. Create method to display info.

class laptop:
    def __init__(self,brand,ram):
        self.brand=brand
        self.ram=ram

    def display(self):
        print("the brand name is : " , self.brand , "\n the storage is:" , self.ram)

c1=laptop("lenovo",128)
c1.display()