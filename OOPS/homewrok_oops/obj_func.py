#Explanation

# Student → Class (blueprint)

# s1, s2 → Objects

# self → Current object ko refer karta hai
class student:
    def __init__(self,name,roll_no,address):
        self.name=name
        self.roll_no=roll_no
        self.address=address
    def display(self):
        print("name:-",self.name)
        print("roll_no:-",self.roll_no)
        print("address:-",self.address)
##objects##
stud1=student("kajal",23,"andheri")
stud2=student("vidya",24,"malad")
stud1.display()
stud2.display()
# Example 2: Bank Account Class
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def show_balance(self):
        print("Balance:", self.balance)

# Object
acc1 = BankAccount("Kajal", 5000)
acc1.deposit(2000)
acc1.show_balance()
    