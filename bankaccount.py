class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully.")
        print("Deposited Amount:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
            print("Withdrawn Amount:", amount)
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print("Current Balance:", self.balance)


# Create Bank Account object
account = BankAccount(1000)

# Display initial balance
account.display_balance()

# Deposit money
account.deposit(500)

# Display balance
account.display_balance()

# Withdraw money
account.withdraw(300)

# Display balance
account.display_balance()

# Try to withdraw more than balance
account.withdraw(2000)

# Display final balance
account.display_balance()