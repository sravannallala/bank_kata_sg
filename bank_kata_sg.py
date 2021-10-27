from datetime import datetime
import pickle
# git learning

class Operation:
    def __init__(self, amount, effective_time, balance):
        self.amount = amount
        self.effective_time = effective_time
        self.balance = balance

#Credit
class Credit(Operation):
    def __init__(self, amount, effective_time, balance):
        super().__init__(amount, effective_time, balance)

    @property
    def operation_type(self):
        return "CREDIT"

#Debit
class Debit(Operation):
    def __init__(self, amount, effective_time, balance):
        super().__init__(amount, effective_time, balance)

    @property
    def operation_type(self):
        return "DEBIT"

#Account Class
class Account:
    def __init__(self, name):
        self.name = name
        self.operations = []
        self.current_balance = 0

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount should be greater than 0\n")
            return
        self.current_balance += amount
        credit = Credit(amount, datetime.now(), self.current_balance)
        self.operations.append(credit)
        print("Deposit Successful.\n")


    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount should be greater than 0\n")
            return
        if amount > self.current_balance:
            print("Insufficient balance in your Account\n")
            return
        self.current_balance -= amount
        debit = Debit(amount, datetime.now(), self.current_balance)
        self.operations.append(debit)
        print("Withdraw Successful.\n")
 

    def statement_history(self):
        print(f"\nAccount holder: {self.name}")
        print("\nOperation | Amount | Balance | Time")
        for operation in self.operations:
            print(
                f"{operation.operation_type} | {operation.amount} | {operation.balance} | {operation.effective_time}"
            )
        print("\n")

#Main Class
def main():
    exit = False
    account_name = input("Enter your name : \n")
    try:
        with open(account_name, "rb") as f:
            account = pickle.load(f)
    except Exception:
        print("Account not found, Creating new account.....")
        account = Account(account_name)
    print("Welcome to Societe Generale, ", account.name)
    while not exit:
        print("\nSelect your choice : \n1.Deposit\n2.Withdraw\n3.Statement history\n4.Exit\n")
        choice = int(input())
        if choice == 1:
            amount = int(input("Please type the Amount you want to deposit?\n"))
            account.deposit(amount)
        elif choice == 2:
            amount = int(input("Please type the Amount you want to withdraw?\n"))
            account.withdraw(amount)
        elif choice == 3:
            account.statement_history()
        elif choice == 4:
            exit = True
        else:
            print("Invalid choice!")
        with open(account_name, "wb") as f:
            pickle.dump(account, f)


if __name__ == "__main__":
    main()
