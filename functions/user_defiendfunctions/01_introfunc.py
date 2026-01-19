# 1.func without args and without return value.
def greet():
    print("hello world")
print(greet())

# 2.func with args and without return value.
def greeting(name):
    print(f'hello {name}')
print(greeting("yash"))

# 3.func without args and with return value.
def add():
    a=int(input("enter a"))
    b=int(input("enter b"))
    return a+b
print(add())
# 4.func with  args and with  return value.
def mul(a,b,c):
    return a*b*c
print(mul(1,2,3))
