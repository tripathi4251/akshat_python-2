class student:
    def __init__(self,marks):
        self.marks=marks

    def calculate_grade(self):
        if self.marks>=90:
            print("A")
        elif self.marks<=90 and self.marks>=75:
            print("B")
        elif self.marks<=75:
            print("C")
        else:
            print("D")

s1=student(85)
s1.calculate_grade()
