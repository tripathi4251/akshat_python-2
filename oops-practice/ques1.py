#create a class called dog , add and __init__ method with parameters name and age and store them as properties using self..

class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def bark(self):
    print(self.name + " says Woof!")

# Create an object
d1 = Dog("Buddy", 3)

# Call the bark method
d1.bark()
