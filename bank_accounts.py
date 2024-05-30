class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, accountName):
        self.balance = initialAmount
        self.name = accountName
        print(
            f"\n Bank Account : {self.name} created. \n Balance=${self.balance:.2f}")

    def getBalance(self):
        print(f"Getting Balance : ${self.balance:.2f} \n")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposit of ${amount} is complete. New Balance ${self.balance}")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"Sorry, {self.name} has a balance of {self.balance:.2f} only.")

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("Withdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdraw interrupted : {error}")

    def transfer(self, amount, account):
        try:
            print("\n Begin Transfer")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(" \n Transaction Transfer complete")
        except BalanceException as error:
            print(f"Transfer interrupted {error}")


class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("Interest added")
        self.getBalance()


class SavingsAccount(InterestRewardsAccount):
    def __init__(self, initialAmount, accountName):
        super().__init__(initialAmount, accountName)
        self.fee = 5

        def withdraw(self, amount):
            try:
                self.viableTransaction(amount+self.fee)
                self.balance = self.balance - (amount + self.fee)
                print(f"New Balance ")
                self.getBalance()
            except BalanceException as error:
                print(f"Withdraw Incomplete {error}")
