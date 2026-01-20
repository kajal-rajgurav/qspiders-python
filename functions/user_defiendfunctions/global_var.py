# Global Variable Used in Calculation
rate = 5   # global variable

def calculate(amount):
    total = amount * rate   # local variable
    return total

print("Total:", calculate(100))

