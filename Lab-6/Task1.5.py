class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. Remaining Balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account Holder: {self.name}, Current Balance: {self.balance}")

account1 = BankAccount("Alice", 1000)
account1.check_balance()
account1.deposit(500)
account1.withdraw(300)
account1.withdraw(1500)  # Should show insufficient balance
account1.check_balance()