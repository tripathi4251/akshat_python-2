
#Create a class Dog
# What to do:
#Store name and breed. Create method bark().

class dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

    def bark(self):
        print("woof!")
        
d1=dog("tommy","labrador")
print(d1.name)
print(d1.breed)
d1.bark()
