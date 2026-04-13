#setter method
# What to do:
#Update private variable using method.

class player:
    def __init__(self,name,playernumber):
        self.name=name
        self._number=playernumber

    def get_number(self):
        return self._number
    
    def  set_number(self,value):
        self._number=value
        print("the number is:" , self._number)

p1=player("Akshat", 7)
p1.set_number(18)
print(p1.get_number())