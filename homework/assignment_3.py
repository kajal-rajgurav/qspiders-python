# wapt to find the greater  among 4 diffrent integer.

a=int(input("enter your first number:-"))
b=int(input("enter your second number:-"))
c=int(input("enter your third number:-"))
d=int(input("enter your fourth number:-"))
if a>b and a>c and a>d:
    print("greater nmuber:- a")
elif b>c and c>d:
    print ("greater number:- b")
elif c>d:
    print("greater number:- c")
else:
    print("grater number:- d")