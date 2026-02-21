# map() Function
# 👉 What is map()?

# map() is used to apply a function to each item of a list.

# Simple words:

# “Har element pe same kaam karna hai” → use map()

# 🔹 Example 1: Square of numbers
numbers = [1, 2, 3, 4]

def square(x):
    return x * x

result = map(square, numbers)

print(list(result))

# Example 2: Using lambda (short method)
numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(list(result))