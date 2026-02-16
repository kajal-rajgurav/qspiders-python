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



# 2.Print something before & after function
def my_decorator(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@my_decorator
def hello():
    print("Hello Kajal")

hello()


# Deep understanding

# Python does:

# hello = my_decorator(hello)


# Now hello() actually calls wrapper().

# Original hello() is INSIDE wrapper.
# EXAMPLE 2 – DECORATOR WITH PARAMETERS
# =====================

# Function takes arguments.

def my_decorator(func):

    def wrapper(name):
        print("Welcome")
        func(name)
        print("Bye")

    return wrapper


@my_decorator
def greet(name):
    print("Hello", name)

greet("Kajal")

###########################################3
def decorator(func):

    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result

    return wrapper
