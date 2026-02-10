class BankAccount:
    interest_rate = 0.04  # 4%

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []
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
        interest_amount = self.balance *self.__class__.interest_rate
        self.deposit(interest_amount)
        self.transactions.append(f"Interest added: {interest_amount}")

    def statement(self):
        print(f"\nHi {self.name}, your bank statement:")
        for transaction in self.transactions:
            print(transaction)
        print("*" * 40)
        print(f"Current balance: {self.balance}")
c1 = BankAccount('Steve', 1000)
c2 = BankAccount('Bill', 2000)

c1.deposit(2000)
c1.withdraw(1000)
print(c1.transfer(c2, 500))

c1.statement()
c2.statement()
# creating here inheritance 
class savingAccount(BankAccount):
    interest_rate=0.5
    def __init__(self, name, balance,phno):
        super().__init__(name, balance)  #####all other method are out dated super() merthod wee have to use
        self.phno=phno

    def display(self):
        print("name", self.name)
        print("balance:", self.balance)
        print("phno",self.phno)
    def deposit(self, amount):
         if amount <= 1000:
            raise ValueError("Amount should be greater than or equal to  1000")
         super().deposit(amount)  
      

c4=savingAccount('alex',2000,9988776655)
c5=savingAccount('tim',1000,9702029199)
c4.display()
c4.deposit(300)