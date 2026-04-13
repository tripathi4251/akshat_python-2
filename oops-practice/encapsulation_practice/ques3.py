#Private variable
# What to do:
#Create a private variable and access it using a method.

class person:
    def __init__(self,name,age):
        self.name=name
        self._age=age

    def get_age(self):
        return self._age
    
    def info(self):
        print("The name of person is:" , self.name ,"\n His age is:" , self._age)
    
p=person("Akshat",25)
print(p.get_age())
p.info()