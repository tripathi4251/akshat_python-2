#simple example of polymorphism using dunder function

class student:
    def __init__(self,marks):
        self.marks=marks

    def __add__(self,other):
        return self.marks+other.marks
    
s1=student(80)
s2=student(90)

print(s1+s2)
