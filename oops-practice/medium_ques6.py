#Car Speed Control
# What to do:
#Create methods to increase and decrease speed.

class car:
    def __init__(self,speed):
        self.speed=speed

    def increase (self):
        self.speed += 10

    def decrease (self):
        self.speed -= 10

c=car(50)
c.increase()
print(c.speed)
