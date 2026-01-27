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


# Example 3: Using *args and **kwargs (Most Used ⭐)

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Function execution started")
        result = func(*args, **kwargs)
        print("Function execution finished")
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(10, 20))


# 🔹 Example 4: Authorization / Login Check
def login_required(func):
    def wrapper(user):
        if user == "admin":
            func(user)
        else:
            print("Access Denied")
    return wrapper

@login_required
def dashboard(user):
    print("Welcome", user)

dashboard("admin")
dashboard("guest")

# Example 5: Function Execution Time (Very Popular ⏱️)
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Time taken:", end - start)
    return wrapper

@timer
def task():
    time.sleep(1)

task()

# Example 6: Logging Decorator
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        func(*args, **kwargs)
    return wrapper

@logger
def multiply(a, b):
    print(a * b)

multiply(4, 5)
# Example 7: Multiple Decorators
def decor1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decor2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decor1
@decor2
def show():
    print("Hello")

show()


# Example 8: Built-in Decorator @property

class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

s = Student(90)
print(s.marks)

