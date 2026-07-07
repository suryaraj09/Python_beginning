class BalanceException(Exception):
    pass

class BankAccount:
    def __init__ (self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\n Account' {self.name}' created. \nBalance = ${self.balance: ,.2f}\n")

    def getBalance(self):
        print(f"\n Account '{self.name}' balance = ${self.balance:,.2f}\n")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"the amount deposisted => {amount} and now your total is = > {self.balance}")
        self.getBalance()

    def viableAmount(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Insufficient balance {self.name} only has ${self.balance}")
    
    def withdraw(self, amount):
        try:
            self.viableAmount(amount)
            self.balance = self.balance - amount
            print(f"withdrawal complete and yout current balance is {self.balance}")
        except BalanceException as error:
            print(f"Withdraw Interuppted: {error}")

    def transfer(self, amount, account):
        try:
            self.viableAmount(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\n Transation completed from {self.name} to {account.name}")
        except BalanceException as error:
            print(f"\n Transfer interrupted {error}")

class InterestRewardAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\n Deposit complete.")
        self.getBalance()

class SavingsAcct(InterestRewardAcct):
    def __init__(self, InitialAmount, accName):
        super().__init__(InitialAmount, accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableAmount(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("withdrawal complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\n Withdrawl Interrupted: {error}")
    
    
