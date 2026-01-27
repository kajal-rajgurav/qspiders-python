def addition(a, b):
    return a +b;

getAddition = addition(23, 11)
print(getAddition)


# decorators with arguments
def smart_decorator(func):
    def wrapper(name):
        print("Good Morning")
        func(name)
    return wrapper

@smart_decorator
def greet(name):
    print("Hello", name)

greet("Kajal")

# real time decorator 

import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time taken:", end-start)
    return wrapper

@timer
def task():
    for i in range(1000000):
        pass

task()

# 3. Authentication Example (Real Use Case)

def login_required(func):
    def wrapper(user):
        if user == "admin":
            func(user)
        else:
            print("Access Denied ❌")
    return wrapper

@login_required
def dashboard(user):
    print("Welcome to Dashboard", user)

dashboard("admin")
dashboard("guest")

# 🔹 Example 1: Simple Decorator (Before & After)

def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def hello():
    print("Hello World")

hello()

# Example 2: Decorator with Arguments
def decorator(func):
    def wrapper(name):
        print("Greeting starts")
        func(name)
        print("Greeting ends")
    return wrapper

@decorator
def greet(name):
    print("Hello", name)

greet("Kajal")

