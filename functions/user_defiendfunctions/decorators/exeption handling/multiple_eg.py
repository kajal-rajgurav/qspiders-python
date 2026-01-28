# Handling Multiple Exceptions
try:
    a = int("abc")
    b = 10 / 2
except ValueError:
    print("Value error occurred")
except ZeroDivisionError:
    print("Division by zero error")

# using else.
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", y)
