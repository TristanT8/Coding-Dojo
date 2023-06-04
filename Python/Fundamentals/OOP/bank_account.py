class bank_account:
    def __init__(self):
        self.balance = 0
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


bob_account = bank_account()
alex_account = bank_account()

bob_account.deposit(300),bob_account.deposit(200),bob_account.deposit(150),bob_account.withdraw(100),bob_account.display_account_info(),bob_account.interest()

alex_account.deposit(5000),alex_account.deposit(1000),alex_account.withdraw(20),alex_account.withdraw(40),alex_account.withdraw(240)
alex_account.withdraw(600),alex_account.display_account_info(),alex_account.interest()
