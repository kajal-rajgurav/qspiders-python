
# Mini Project: Simple ATM System
class ATM:
    def __init__(self,name,balance,add):
        self.name=name
        print("account holder name:-",self.name)
        self.balance=balance
        self.add=add
    def check_balance(self):
       print("balance",self.balance)
    def deposit(self,amount):
        self.balance+=amount
        print("deposited",amount)
    def widrawl(self,amount):
        if amount<= self.balance:
            self.balance-=amount
            print("widrawn",amount)
        else:
            print("insufficient balace")
user1=ATM("kajal",5000,"malad")
# user1=ATM("riya",8000,"andheri")  ## this area

#####object####

user1.check_balance()
user1.deposit(int(input("enter your deposit amount:-")))
user1.widrawl(int(input("enter widrawl amount:-")))
user1.check_balance()


