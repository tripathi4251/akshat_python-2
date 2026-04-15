#Duck Typing
#Task:
#Write a function that works for different objects without checking type.

class bike:
    def start(self):
        print("bike start with kick")

class car:
    def start(self):
        print("car start with keys")
    
def vehicle(sound):
        sound.start()

vehicle(bike())
vehicle(car())