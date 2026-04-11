#Person → Student
# What to do:
#Create a parent class Person with name. Create child class Student that adds roll number and print both.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

s = Student("Akshat", 101)
print("Name:", s.name)
print("Roll:", s.roll)