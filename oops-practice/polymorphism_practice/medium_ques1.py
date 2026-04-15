class shape:
    def area(self):
        pass

class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius
    
class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width
    
c=circle(87)
print(c.area())
r=rectangle(16,3)
print(r.area())
        