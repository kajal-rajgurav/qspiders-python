# 1️⃣ Program to Add Two Numbers using Function
def add(a, b):
    return a + b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = add(x, y)
print("Sum =", result)
# 2️⃣ Program to Find Factorial using Function
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))

# 3️⃣ Program to Check Even or Odd using Function
def even_odd(n):
    if n % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

num = int(input("Enter a number: "))
even_odd(num)

students = []

def add_student():
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    students.append({"roll": roll, "name": name, "marks": marks})
    print("Student added successfully!")

def display_students():
    if not students:
        print("No records found")
        return
    for s in students:
        print(s)

def search_student():
    roll = int(input("Enter Roll No to search: "))
    for s in students:
        if s["roll"] == roll:
            print("Found:", s)
            return
    print("Student not found")

def delete_student():
    roll = int(input("Enter Roll No to delete: "))
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted")
            return
    print("Student not found")

while True:
    print("\n1.Add  2.Display  3.Search  4.Delete  5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
###############################################################################
students = []

def add_student():
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    students.append({"roll": roll, "name": name, "marks": marks})
    print("Student added successfully!")

def display_students():
    if not students:
        print("No records found")
        return
    for s in students:
        print(s)

def search_student():
    roll = int(input("Enter Roll No to search: "))
    for s in students:
        if s["roll"] == roll:
            print("Found:", s)
            return
    print("Student not found")

def delete_student():
    roll = int(input("Enter Roll No to delete: "))
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted")
            return
    print("Student not found")

while True:
    print("\n1.Add  2.Display  3.Search  4.Delete  5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
#################################################################################

library = {}

def add_book():
    book_id = int(input("Enter Book ID: "))
    name = input("Enter Book Name: ")
    library[book_id] = {"name": name, "issued": False}
    print("Book added")

def issue_book():
    book_id = int(input("Enter Book ID: "))
    if book_id in library and not library[book_id]["issued"]:
        library[book_id]["issued"] = True
        print("Book issued")
    else:
        print("Book not available")

def return_book():
    book_id = int(input("Enter Book ID: "))
    if book_id in library and library[book_id]["issued"]:
        library[book_id]["issued"] = False
        print("Book returned")
    else:
        print("Invalid operation")

def display_books():
    for book in library.values():
        print(book)

while True:
    print("\n1.Add 2.Issue 3.Return 4.Display 5.Exit")
    c = int(input("Enter choice: "))

    if c == 1:
        add_book()
    elif c == 2:
        issue_book()
    elif c == 3:
        return_book()
    elif c == 4:
        display_books()
    elif c == 5:
        break
