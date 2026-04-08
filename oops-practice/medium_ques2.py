#Rectangle Perimeter + Area
# What to do:
#Create methods for both area and perimeter.

class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)
    
    def area(self):
        return self.length*self.breadth
    
r1=rectangle(20,15)
print(r1.perimeter())
print(r1.area())