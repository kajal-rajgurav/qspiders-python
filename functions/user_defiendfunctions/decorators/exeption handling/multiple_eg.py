# Handling Multiple Exceptions
try:
    a = int("abc")
    b = 10 / 2
except ValueError:
    print("Value error occurred")
except ZeroDivisionError:
    print("Division by zero error")
