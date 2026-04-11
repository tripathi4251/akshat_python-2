#Shape → Rectangle
# What to do:
#Create parent class and child class that calculates area.

class shape:
    def __init__(self,length,width):
        self.length=length
        self.width=width

class rectangle(shape):
    def show(self):
       return self.length*self.width
   
r=rectangle(32,16)
print(r.show())