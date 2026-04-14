#Employee salary update
# What to do:
#Use setter to increase salary.

class employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary

    def get_salary(self):
        return self._salary
    
    def set_salary(self,value):
        self._salary=value
        print("the increased salary is:" , self._salary)

e1=employee("Akshat",50000)
print(e1.get_salary())
e1.set_salary(60000)