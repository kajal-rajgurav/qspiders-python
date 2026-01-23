# wapt print 1 to 10 without any loop use functions
def numbers(num=1):
    if num<11:
        print(num)
        num+=1
        numbers(num)
numbers()

