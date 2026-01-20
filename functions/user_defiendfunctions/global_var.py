# Global Variable Used in Calculation
rate = 5   # global variable

def calculate(amount):
    total = amount * rate   # local variable
    return total

print("Total:", calculate(100))

# Multiple Functions Using Same Global Variable

value = 100   # global variable

def add():
    global value
    value += 50

def subtract():
    global value
    value -= 20

add()
subtract()
print("Final value:", value)

