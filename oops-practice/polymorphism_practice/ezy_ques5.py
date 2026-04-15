# Function Polymorphism
#What to do:
#Write a function make_sound(animal) that takes any object and calls its sound() method.

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

make_sound(Dog())
make_sound(Cat())