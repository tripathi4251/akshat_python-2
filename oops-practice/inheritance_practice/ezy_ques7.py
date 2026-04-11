#Bird → Parrot
# What to do:
#Create a method fly() and use it in child class.

class bird:
    def fly(self):
        print("flying..")

class parrot(bird):
     def fly(self):
      super().fly()
print("parrot flies..")

p=parrot()
p.fly()