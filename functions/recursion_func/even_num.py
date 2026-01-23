# wapt even   1 to 100 using recursion.
def numbers(num=1):
    if num<=100:
     if num%2==0:

        print(num)
        num+=1
        numbers(num)
numbers()
