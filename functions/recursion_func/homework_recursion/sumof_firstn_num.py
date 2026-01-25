# Example 3: Sum of First n Numbers
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)

print(sum_n(5))
# how its working 
# sum_digits(123)
# = 3 + sum_digits(12)
# = 3 + 2 + sum_digits(1)
# = 3 + 2 + 1 + sum_digits(0)
# = 6
# 👉 Example: 123 → 1 + 2 + 3 = 6