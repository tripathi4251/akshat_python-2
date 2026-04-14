#Student grade
# What to do:
#Use private marks and calculate grade.

class student:
    def __init__(self,name,marks):
        self.name=name
        self._marks=marks

    def get_marks(self):
        return self._marks

    def calculate_grade(self):
        if self._marks>=90:
            print("A")
        
        elif self._marks>=75:
            print("B")

        elif self._marks<=75:
            print("c")

        else:
            print("fail")

s1=student("Akshat",75)
s1.calculate_grade()
print(s1.get_marks())