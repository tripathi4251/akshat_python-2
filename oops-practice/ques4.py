#Create a class Student
# What to do:
#Create a class with attributes name and marks using a constructor and print them.
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

s1=student("Akshat",95)
print(s1.name)
print(s1.marks)



#Create a class Car
# What to do:
#Add attributes brand and price using constructor. Create a method to display details.
class car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def display(self):
              print("the details are:" , self.brand , self.price)
        
c1=car("ferrari",30000)
c1.display()