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

# Example 3: Car Class
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(self.brand, "car is driving")

# Objects
car1 = Car("BMW", "Black")
car2 = Car("Audi", "White")

car1.drive()
car2.drive()


#  Same class, different objects, different data    

Example 4: Employee Class (with Salary)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increment(self):
        self.salary += 5000

    def show(self):
        print(self.name, "-", self.salary)

emp1 = Employee("Kajal", 30000)
emp1.increment()
emp1.show()
