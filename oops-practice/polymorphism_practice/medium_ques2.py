#Employee Salary
#What to do:
#Create base class Employee with method salary().
#Child classes: FullTime, PartTime.
#Each calculates salary differently.

class employee:
    def salary(self):
        pass

class fulltime:
    def salary(self):
        return 50000
    
class parttime:
    def salary(self):
        return 20000
    

f=fulltime()
print(f.salary())
p=parttime()
print(p.salary())