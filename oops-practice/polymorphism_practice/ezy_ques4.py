#Q4: Loop + Polymorphism
#What to do:
#Create different objects (Dog, Cat) and store them in a list.
#Loop through them and call the same method.

class dog:
    def sound(self):
        print("barks")

class cat:
    def sound(self):
        print("meows")

animals=[dog(),cat()]
for a in animals:
    a.sound()