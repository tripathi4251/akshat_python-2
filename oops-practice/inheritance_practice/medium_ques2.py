#Shape → Circle & Rectangle
# What to do:
#Use same method name area() but different logic (polymorphism + inheritance)

class shape:
    pass   # no need of common constructor

class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    

r = rectangle(16, 15)
print(r.area())

c = circle(4)
print(c.area())