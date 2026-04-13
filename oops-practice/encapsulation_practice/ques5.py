#Bank balance
# What to do:
#Store balance as private and print it.


class account:
    def __init__(self,balance):
        self._balance=balance

    def get_balance(self):
        return self._balance
    
    def show(self):
        print("the balance is:" , self._balance)

a=account(300000)
a.show()