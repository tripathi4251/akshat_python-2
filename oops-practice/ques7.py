#create account class with 2 attributes balance & account no. create methods for debit credi
#and printing the balance..

class account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc


    def debit(self, amount):
        self.balance=-amount
        print("rs.",amount , "was debited")
        print("total balance =", self.get_balance())

    def credit(self,amount):
        self.balance=+amount
        print("rs." , amount , "was credited")
        print("total balance=" , self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1 = account(100000 , 12345)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(400000)
