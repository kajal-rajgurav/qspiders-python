class BankAccount:
    interst_rate=0.4
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        print("balance",f'name',{self.name},self.balance)
    def deposit(self,amount):
        if amount<0:
         raise ValueError('amount should be greater than zero')
        self.balance+=amount
        print("deposited",amount)
    def widraw(self,amount):
        if self.balance<amount:
         raise ValueError('insufficient fund')
        self.balance-=amount
        print("widrawn",amount)
    def transfer(self,other,amount):
       self.widraw(amount)
       self.deposit(amount)
       
    #    if self.balance<amount:
          
    #     raise ValueError('amount should be greater than zero')
    #    if amount<0:
    #      raise ValueError('amount should be greater than zero')
    def roi(self):
       interst_amount=self.balance*BankAccount.interst_rate
       self.deposit(interst_amount) 
       
       
     

c1=BankAccount('steve',1000)
c2=BankAccount('bill',2000)
c3=BankAccount('alex',3000)
c1.deposit(2000)
c1.widraw(1000)
print(c1.transfer(c2.deposit))

