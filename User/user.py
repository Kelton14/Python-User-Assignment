class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"{self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        # return self
    
Tom = User("Tom" , "bigtom@gmail.com")
Sally = User("Sally", "supersally@outlook.com")
Bob = User("Bob", "bobbyboberson@aol.com")


Tom.make_deposit(600)
Tom.make_deposit(1500)
Tom.make_deposit(1)
Tom.make_withdrawal(34)
Tom.display_user_balance()

Sally.make_deposit(450)
Sally.make_deposit(975)
Sally.make_withdrawal(15)
Sally.make_withdrawal(245)
Sally.display_user_balance()

Bob.make_deposit(1500)
Bob.make_withdrawal(15)
Bob.make_withdrawal(15)
Bob.make_withdrawal(15)
Bob.display_user_balance()

Bob.transfer_money(Sally, 500)
Sally.display_user_balance()
Bob.display_user_balance()

