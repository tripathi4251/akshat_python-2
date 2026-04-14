#Method Overriding (Basic)
#What to do:
#Create a parent class Animal with method sound().
# #Create a child class Dog that overrides sound().

class animal():
    def sound(self):
        print("animal makes sound")

class dog(animal):
    def sound(self):
        print("dog barks")

d=dog()
d.sound()
    
