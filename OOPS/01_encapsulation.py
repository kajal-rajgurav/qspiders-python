# 1. Class & Object Example
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

# Creating object
s1 = Student("Kajal", 90)
s1.display()
# 2. Encapsulation Example (Data Hiding)
class Bank:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def show_balance(self):
        print("Balance:", self.__balance)

b = Bank(5000)
b.show_balance()
