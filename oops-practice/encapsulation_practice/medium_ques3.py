#User password
# What to do:
#Keep password private and validate it.

class User:
    def __init__(self, password):
        self.__password = password

    def check(self, pwd):
        if pwd == self.__password:
            print("Correct password")
        else:
            print("Wrong password")

u = User("1234")
u.check("1234")