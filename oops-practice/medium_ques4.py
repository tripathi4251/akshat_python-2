#Employee Bonus
# What to do:
#Calculate bonus based on salary.

class employee:
    def __init__(self,salary):
        self.salary=salary

    def bonus(self):
        return self.salary*0.30
    
e1=employee(25000)
print(e1.bonus())