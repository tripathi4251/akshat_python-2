#ATM Machine
# What to do:
#Deposit, withdraw, check balance.


class ATM:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        self.balance -= amt

atm = ATM(1000)
atm.deposit(500)
print(atm.balance)