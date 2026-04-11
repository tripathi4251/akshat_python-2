#Animal → Dog
# What to do:
#Create a method sound() in parent class. Override it in child class.

class animal:
    def sound(self):
        print("animal has a sound")

class dog(animal):
    def sound(self):
     print("dog says:" "woof!")

d=dog()
d.sound()      
