#Multiple Classes Same Method
#What to do:
#Create classes Cat, Dog, Cow.
#Each class should have a method speak() but with different outputs.

class cat:
    def speak(self):
        print("cat meows")
    
class dog:
    def speak(self):
        print("dog barks")

class Cow:
    def speak(self):
        print("cow murmurs")

d=dog()
c=cat()
C=Cow()
d.speak()
c.speak()
C.speak()