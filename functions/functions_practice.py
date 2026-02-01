# 1️⃣ Program to Add Two Numbers using Function
def add(a, b):
    return a + b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = add(x, y)
print("Sum =", result)
# 2️⃣ Program to Find Factorial using Function
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))

# 3️⃣ Program to Check Even or Odd using Function
def even_odd(n):
    if n % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

num = int(input("Enter a number: "))
even_odd(num)


