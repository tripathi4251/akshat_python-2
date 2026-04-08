#Shopping Cart
# What to do:
#add items
#calculate total

class Cart:
    def __init__(self):
        self.total = 0

    def add(self, price):
        self.total += price

    def show(self):
        print(self.total)

c = Cart()
c.add(100)
c.add(200)
c.show()