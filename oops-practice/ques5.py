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