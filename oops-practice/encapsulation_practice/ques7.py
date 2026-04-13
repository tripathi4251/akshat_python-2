#Employee salary
# What to do:
#Keep salary private and access via method.

class employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary

    def show(self):
        print("the salary is:" , self._salary)

E=employee("akshat",600000)
E.show()
