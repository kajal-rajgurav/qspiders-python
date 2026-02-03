# class BankAccount:
#     interst_rate=0.4
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#         self.transactions=[]
#         self.transactions.append(f'initial balance is{balance}')
#         print(f'name {self.name}')
#         print(f'name{self.name}')
#     def deposit(self,amount):
#         if amount<0:
#          raise ValueError('amount should be greater than zero')
#         self.balance+=amount
#         print("deposited",amount)
#     def widraw(self,amount):
#         if self.balance<amount:
#          raise ValueError('insufficient fund')
#         self.balance-=amount
#         print("widrawn",amount)
#     def transfer(self,other,amount):
#        self.widraw(amount)
#        other.deposit(amount)
       
#     #    if self.balance<amount:
          
#     #     raise ValueError('amount should be greater than zero')
#     #    if amount<0:
#     #      raise ValueError('amount should be greater than zero')
#     def roi(self):
#        interst_amount=self.balance*BankAccount.interst_rate
#        self.deposit(interst_amount) 
#     def statement(self):
#        print(f'hii {self.name}your bank statement')
#        for transaction in self.transactions:
#           print(transaction)
#        print('*'*40)
#        print(f'current balance is {self.balance}')
       
          
       
     

# c1=BankAccount('steve',1000)
# c2=BankAccount('bill',2000)
# c3=BankAccount('alex',3000)
# c1.deposit(2000)
# c1.widraw(1000)
# print(c1.transfer(c2,500))


#################################################
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
        interest_amount = self.balance * BankAccount.interest_rate
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
