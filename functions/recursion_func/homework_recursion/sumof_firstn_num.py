# Example 3: Sum of First n Numbers
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)

print(sum_n(5))
