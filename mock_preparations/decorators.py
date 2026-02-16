# 1. What is a Decorator?

# 👉 A decorator is used to modify a function without changing its code.

# 💡 Real use:

# Login check

# Logging

# Timing execution/



# 2. How to create a Decorator?
#   decorators are functions that make use of hgher order functions and closures.

# REAL USE CASE (Login Check)
def login_required(func):
    def wrapper():
        print("Checking login...")
        func()
    return wrapper

@login_required
def dashboard():
    print("Dashboard loaded")

dashboard()
