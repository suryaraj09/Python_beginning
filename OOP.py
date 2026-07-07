from bank_accounts import SavingsAcct
from bank_accounts import InterestRewardAcct
from bank_accounts import BankAccount
from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance
Sara.getBalance

Dave.deposit(500)
print(Dave)
print(Sara)

Dave.withdraw(1000)

Sara.transfer(1000)

Dave.transfer(10, Sara)
Dave.transfer(100, Sara)

Jim = InterestRewardAcct(1000, "Jim")

Jim.getBalance()
Jim.deposit(100)

Jim.transfer(100, Dave)

Bla = SavingsAcct(1000, "Blah")

Bla.getBalance()
Bla.deposit(100)

Bla.transfer(100, Dave)

