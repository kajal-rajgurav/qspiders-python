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

# Example 4: Employee Class (with Salary)
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

# Example 5: Mobile Class
class Mobile:
    def __init__(self, model, price,loc=None):
        self.model = model
        self.price = price
        self.loc=loc

    def details(self):
        print("Model:", self.model)
        print("Price:", self.price)
        print("loc:",self.loc)

m1 = Mobile("iPhone", 80000,None)
m2 = Mobile("Samsung", 60000)

m1.details()
m2.details()
# 1. Constructor (__init__) 

# 👉 Constructor is a special method
# 👉 It automatically runs when an object is created
# 👉 Used to initialize data (values)
# Example 1: Constructor without parameters
class Demo:
    def __init__(self):
        print("Constructor called")

obj1 = Demo()
obj2 = Demo()

# Example 2: Constructor with parameters
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

p1 = Person("Kajal", 22)
p1.show()


# Example 3: Why self is important?
class Test:
    def __init__(self, x):
        self.x = x

t1 = Test(10)
t2 = Test(20)

print(t1.x)
print(t2.x)


# 👉 self ensures each object has its own data