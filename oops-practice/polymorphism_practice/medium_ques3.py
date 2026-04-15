# Vehicle Start System
#What to do:
#Create classes Car, Bike, Truck.
#Each has method start() with different behavior.

class car:
    def start(self):
        print("car starts with keys")
class bike:
    def start(self):
        print("bike starts with kick")

class truck:
    def start(self):
        print("truck starts with buttoon")

vehicles = [car(),bike(),truck()]
for v in vehicles:
    v.start()