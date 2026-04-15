#Mixed Polymorphism
#Task:
#Use both overriding + function polymorphism together.

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

def animal_sound(animal):
    animal.sound()

animals = [Dog(), Cat()]

for a in animals:
    animal_sound(a)