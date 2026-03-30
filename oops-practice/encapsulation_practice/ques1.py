#Write a Python program to demonstrate encapsulation using a class with private variables and getter/setter methods.
class Student:
    def __init__(self, name, marks):
        self.name = name        # public variable
        self.__marks = marks    # private variable

    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        if new_marks >= 0:
            self.__marks = new_marks
        else:
            print("Marks cannot be negative")


# Creating object
s1 = Student("Akshat", 85)

print(s1.name)           # Accessible
print(s1.get_marks())    # Accessing private variable using method

s1.set_marks(90)        
print(s1.get_marks())


