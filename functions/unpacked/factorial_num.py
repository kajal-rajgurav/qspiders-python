# Factorial of even numbers only

def factorial_even(*args):
    for num in args:
        if num % 2 == 0:
            fact = 1
            for i in range(1, num + 1):
                fact *= i
            print(f"Factorial of even number {num} is {fact}")

factorial_even(3, 4, 5, 6)


# Even numbers by unpacking a list

def even_numbers(*nums):
    evens = [n for n in nums if n % 2 == 0]
    print("Even numbers:", evens)

values = [1, 2, 3, 4, 5, 6]
even_numbers(*values)
