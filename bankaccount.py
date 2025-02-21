#class creation
class BankAccount:
    def __init__(self, __account_holder, __account_balance = 00.0):
        self.__account_holder = __account_holder
        self.__account_balance = __account_balance
    def __str__(self):
        return f"{self.__account_holder}: {self.__account_balance}"
    def deposit(self, amount):
        if amount > 100000:
            self.__account_balance += amount
            print(f"The new balance is: {self.__account_balance}")
        else:
            print(" Please try another bank because this bank is not meant for broke people")
    def withdraw(self, amount):
        if amount < 100000:
            self.__account_balance -= amount

            print("Please stop wasting our time you cannot withdraw less than you had deposited")
        else:
            print("The new balance is: {self.account_balance}")
    def check_balance(self):
        print(f"Balance: {self.__account_balance}")

name=input("Enter your name: ")
account=BankAccount(name)
print()
account.balance =1000


#console program
while True:
    print(" WELCOME TO SAFARI BANK ")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Check balance")
    print("4. Exit")
    choice = int(input("Enter your choice:" ))
    if choice == 1:
        amount=(int(input("Enter amount to deposit: ")))
        account.deposit(amount)
    elif choice == 2:
        amount=(int(input("Enter amount to withdraw: ")))
        account.withdraw(amount)
    elif choice == 3:
        account.check_balance()
    elif choice == 4:
        print("Thank you for using Safari Bank services")
        break

    else:
        print("Kindly read what is written before entering your choice ")
