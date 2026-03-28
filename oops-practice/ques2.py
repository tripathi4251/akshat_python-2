#create a class called car add an init method with brand ,parameterand store it as properly


class Car:
  def __init__(self, brand):
    self.brand = brand

  def show(self):
    print(self.brand)

# Create an object
c1 = Car("Ford")
c1.show()