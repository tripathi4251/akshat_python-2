#Vehicle → Car & Bike
# What to do:
#Add different methods in both child classes.

class vehicle:
    def start(self):
        print("vehicle starts")

class car(vehicle):
    def drive(self):
        print("car driving")

class bike(vehicle):
    def ride(self):
        print("bike riding")

c=car()
b=bike()

c.drive()
b.ride()
c.start()