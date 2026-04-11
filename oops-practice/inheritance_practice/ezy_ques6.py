#Teacher → MathTeacher
# What to do:
#Add subject in child class and print it.

class teacher:
     def __init__(self,name):
          self.name=name

     def teaches(self):
        print("the teacher teaches the student")

class mathteacher(teacher):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject
        
m1=mathteacher("akshat" ,"maths")
print(m1.name)
print(m1.subject)
m1.teaches()