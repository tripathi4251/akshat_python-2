#Account → Saving & Current
# What to do:
#Use different interest rates in child classes.

class Account:
    def __init__(self, balance):
        self.balance = balance

class SavingAccount(Account):
    def interest(self):
        print("Saving Interest:", self.balance * 0.05)

class CurrentAccount(Account):
    def interest(self):
        print("Current Interest:", self.balance * 0.02)

s = SavingAccount(1000)
c = CurrentAccount(1000)

s.interest()
c.interest()