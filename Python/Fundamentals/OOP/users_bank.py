class bank_account:
    def __init__(self):
        self.balance = 200
        self.int_rate = 1.02

    def deposit(self, amount):
        self.balance = self.balance + amount
        print('Deposited:', amount)
        return self

    def withdraw(self, amount):
        if (self.balance >= amount):
            self.balance -= amount
            print('Withdrew:', amount)
        else:
            print("Insufficient Funds, Charging 5$ Fee", amount - 5)
        return self

    def interest(self):
        self.balance = self.balance * self.int_rate
        print(f'Your available balance after accrued interest is ${self.balance}')
        return self
        
    def display_account_info(self):
        print("Available Balance=", self.balance)
        return self


class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = bank_account()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(f'You deposited {amount}, total is now ${self.account.balance}')
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(f'You withdrew {amount}, total is now ${self.account.balance}')
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        print(self.account.display_account_info)
        return self

bob_account = User("Bob", "Bob@gmail.com")
alex_account = User("Alex", "Alex@live.com")



bob_account.make_deposit(300).make_withdrawal(100).display_user_balance()
