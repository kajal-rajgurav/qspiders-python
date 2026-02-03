# Updated BankAccount Class (with MORE methods)
class BankAccount:
    interest_rate = 0.04

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []
        self.active = True
        self.transactions.append(f"Initial balance: {balance}")
        print(f"Account created for {self.name}")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount should be greater than zero")
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print("Deposited", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transactions.append(f"Withdrawn: {amount}")
        print("Withdrawn", amount)

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)
        self.transactions.append(f"Transferred {amount} to {other.name}")
        return f"Transferred {amount} to {other.name}"

    def roi(self):
        interest = self.balance * BankAccount.interest_rate
        self.deposit(interest)
        self.transactions.append(f"Interest added: {interest}")

    # 🔹 NEW METHODS 🔹

    def check_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance

    def get_transaction_count(self):
        return len(self.transactions)

    def last_transaction(self):
        if not self.transactions:
            return "No transactions found"
        return self.transactions[-1]

    def change_name(self, new_name):
        old_name = self.name
        self.name = new_name
        self.transactions.append(f"Account holder changed from {old_name} to {new_name}")
        print("Name updated successfully")

    def is_rich(self):
        return self.balance >= 1_000_000

    def apply_penalty(self):
        if self.balance < 500:
            penalty = 50
            self.balance -= penalty
            self.transactions.append(f"Low balance penalty: {penalty}")
            print("Penalty applied")

    def close_account(self):
        if self.balance != 0:
            raise ValueError("Account balance must be zero to close account")
        self.active = False
        self.transactions.append("Account closed")
        print("Account closed successfully")

    def statement(self):
        print(f"\nHi {self.name}, your bank statement:")
        for t in self.transactions:
            print(t)
        print("*" * 40)
        print(f"Current balance: {self.balance}")
c1 = BankAccount("Steve", 1000)
c2 = BankAccount("Bill", 2000)

c1.deposit(500)
c1.withdraw(200)
c1.transfer(c2, 300)

print("Is Steve rich?", c1.is_rich())
print("Last transaction:", c1.last_transaction())
print("Total transactions:", c1.get_transaction_count())

c1.statement()
