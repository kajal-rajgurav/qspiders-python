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
