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



# using finally 
try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("File operation completed")


    # Catching All Exceptions (Not Recommended Often ⚠️)

try:
    x = int(input("Enter number: "))
    print(10 / x)
except Exception as e:
    print("Error:", e)

# Custom Exception

# Create your own exception.

class InvalidMarksError(Exception):
    pass

marks = 120

if marks > 100:
    raise InvalidMarksError("Marks cannot exceed 100")

# Real-Life Example (User Input Validation)
try:
    num = int(input("Enter a number: "))
    print("Square:", num * num)
except ValueError:
    print("Please enter a valid integer")

