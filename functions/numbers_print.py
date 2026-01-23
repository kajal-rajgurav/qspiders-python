# wapt print 1 to 10 without any loop use functions
def numbers(num=1):
    if num<11:  ###if not given termination condition it will go RecursionError: maximum recursion depth exceeded
        print(num)
        num+=1
        numbers(num)
numbers()

