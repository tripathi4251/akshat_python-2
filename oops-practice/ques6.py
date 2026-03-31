#Create a class Person
#What to do:
#Store name and age. Create method to check if adult.

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def check(self):
        if self.age>=18:
            print("adult")
        else:
            print("not adult")
        
p1=person("akshat",20)
p1.check()