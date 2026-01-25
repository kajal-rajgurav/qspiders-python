# 2️⃣ Reverse a Number

# 👉 Example: 123 → 321

def reverse_num(n, rev=0):
    if n == 0:
        return rev
    return reverse_num(n // 10, rev * 10 + n % 10)

# working 
# rev = 0
# → 3
# → 32
# → 321
