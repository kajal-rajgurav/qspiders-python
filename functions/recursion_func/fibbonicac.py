# Example 2: Fibonacci Series (Recursion)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
# how its works
# fibonacci(5)
# = fibonacci(4) + fibonacci(3)

# fibonacci(4)
# = fibonacci(3) + fibonacci(2)
# = 2 + 1
# = 3

# fibonacci(3)
# = fibonacci(2) + fibonacci(1)
# = 1 + 1
# = 2

# So,
# fibonacci(5) = 3 + 2 = 5


