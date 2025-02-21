class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account1= BankAccount(12900129)
print(account1.get_balance())
# even in encapsulation our projects can still
account1.balance=000
print(account1.balance)