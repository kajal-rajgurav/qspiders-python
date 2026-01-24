# wapt even   1 to 100 using recursion.
def numbers(num):
    if num>100:
        return
    if num%2==0:
        print(num, end=" ")
    numbers(num+1)
numbers(1)
# def print_even(n):
#     if n > 100:
#         return
#     if n % 2 == 0:
#         print(n, end=" ")
#     print_even(n + 1)

# print_even(1)
