# 2️⃣ filter() Function
# 👉 What is filter()?

# filter() is used to select elements based on condition.

# Simple words:

# “Condition check karo, jo pass ho usko rakho”

# 🔹 Example 1: Get even numbers
numbers = [1, 2, 3, 4, 5, 6]

def is_even(x):
    return x % 2 == 0

result = filter(is_even, numbers)

print(list(result))

# Using lambda
numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x > 3, numbers)

print(list(result))