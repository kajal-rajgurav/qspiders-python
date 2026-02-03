# 1.func without args and without return value.
def greet():
    print("hello world")
print(greet())

# 2.func with args and without return value.
def greeting(name):
    print(f'hello {name}')
print(greeting("yash"))

# 3.func without args and with return value.
def add():
    a=int(input("enter a"))
    b=int(input("enter b"))
    return a+b
print(add())
# 4.func with  args and with  return value.
def mul(a,b,c):
    return a*b*c
print(mul(1,2,3))



###########################################################

1. Student Management System (Reduced)
students = []

while True:
    print("\n1.Add 2.Display 3.Search 4.Delete 5.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        students.append({
            "roll": int(input("Roll: ")),
            "name": input("Name: "),
            "marks": float(input("Marks: "))
        })

    elif ch == 2:
        print(students if students else "No records")

    elif ch == 3:
        r = int(input("Roll: "))
        print(next((s for s in students if s["roll"] == r), "Not found"))

    elif ch == 4:
        r = int(input("Roll: "))
        students[:] = [s for s in students if s["roll"] != r]

    elif ch == 5:
        break

#####################################################
2. Bank Management System (Reduced)
bank = {}

while True:
    print("\n1.Create 2.Deposit 3.Withdraw 4.Balance 5.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        bank[int(input("Acc No: "))] = 0

    elif ch in [2, 3]:
        acc = int(input("Acc No: "))
        amt = float(input("Amount: "))
        if acc in bank and (ch != 3 or bank[acc] >= amt):
            bank[acc] += amt if ch == 2 else -amt
        else:
            print("Error")

    elif ch == 4:
        acc = int(input("Acc No: "))
        print(bank.get(acc, "Not found"))

    elif ch == 5:
        break

#####################################################333
3. Library Management System (Reduced)
library = {}

while True:
    print("\n1.Add 2.Issue 3.Return 4.Display 5.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        library[int(input("ID: "))] = False

    elif ch in [2, 3]:
        i = int(input("ID: "))
        if i in library:
            library[i] = ch == 2

    elif ch == 4:
        print(library)

    elif ch == 5:
        break

###########################################
# 1. Simple Calculator (Reduced)
while True:
    a = float(input("A: "))
    b = float(input("B: "))
    op = input("+, -, *, / or x: ")

    if op == '+': print(a + b)
    elif op == '-': print(a - b)
    elif op == '*': print(a * b)
    elif op == '/': print(a / b if b != 0 else "Error")
    elif op == 'x': break
##########################################
# 2. Employee Payroll System
emps = {}

while True:
    print("\n1.Add 2.Salary 3.View 4.Exit")
    c = int(input())

    if c == 1:
        i = int(input("ID: "))
        emps[i] = float(input("Basic: "))

    elif c == 2:
        i = int(input("ID: "))
        print("Salary:", emps[i] + 0.2*emps[i])

    elif c == 3:
        print(emps)

    elif c == 4:
        break
