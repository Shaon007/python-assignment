class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance

class SavingsAccount(BankAccount):
    def account_type(self):
        print("This is a Savings Account")


class CurrentAccount(BankAccount):
    def account_type(self):
        print("This is a Current Account")

savings = SavingsAccount(1000)
current = CurrentAccount(2000)

savings.deposit()
current.withdraw()

print("Savings Balance:", savings.get_balance())
print("Current Balance:", current.get_balance())

for account in [savings, current]:
    account.account_type()