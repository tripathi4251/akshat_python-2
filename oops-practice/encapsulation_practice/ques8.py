#Laptop brand
# What to do:
#Store brand privately.

class laptop:
    def __init__(self,name,brand):
        self.name=name
        self._brand=brand

    def display(self):
        print("the name of laptop is:" , self.name, "\n the brand is:", self._brand)

l=laptop("lenovo","xy1")
l.display()

