#Student marks
# What to do:
#Make marks private and display using getter method.

class student:
    def __init__(self,name,marks):
        self.name=name
        self._marks=marks

    def get_marks(self):
        return self._marks
    
    def display(self):
        print("the marks of the student is:" , self._marks)

s=student("Akshat",21)
s.display()
print(s.name)