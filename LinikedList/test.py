class Account:
    account_num = 0
    def __init__(self, user):
        self.name = user

user1 = Account("username") # self.name = username 
print(user1.name)