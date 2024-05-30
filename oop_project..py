from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()

Sara.deposit(1000)

Dave.withdraw(400)

Dave.transfer(200, Sara)

Jim = InterestRewardsAccount(1500, "Jim")
Jim.deposit(1000)

Baze = SavingsAccount(2200, "Blaze")
Baze.deposit(500)
Baze.getBalance()
Baze.transfer(110, Sara)
