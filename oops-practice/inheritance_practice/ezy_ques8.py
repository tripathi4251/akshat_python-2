#BankAccount → SavingsAccount
# What to do:
#Store balance in parent and display it in child.

class bankaccount:
    def __init__(self,balance):
        self.balance=balance

class savingsaccount(bankaccount):
    def display(self):
        print("salary:" , self.balance)

b=savingsaccount(300000)
b.display()