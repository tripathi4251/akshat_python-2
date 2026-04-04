#Create a parent class Animal with an __init__ that takes name
#Add a method speak that prints the name
#Create a child class Dog that inherits from Animal
#Create an object d1 = Dog("Rex")
#Call d1.speak()


class animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
       print("the name pf the dog is:" , self.name)

class dog(animal):
    pass

d=dog("rex")
d.speak()
