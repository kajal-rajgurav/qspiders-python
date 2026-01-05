a=int(input('enter your number:-'))#6
b=int(input('enter your number:-'))#3
c=int(input('enter your number:-'))#4

# a greater b, a greater c, b
# need to check which number is grater using nested if, 


if a<=b:
    print("entered in the first if block because the a is greater than b")
    if a<=c:
        print("Entered in the first if's if block because a is greater than c and b")
        print("a is greater")
    else:
        print("Entered in the first if's else block because a and b is less than c")
        print("c is grater")
else:
    print("entered in the outer else block because the a is not greater than b")
    if b<=c:
        print("Entered in the outer else block because b is greater than c and a")
        print("b is greater")
    else:
        print("Entered in the else block because c is greater than c and b")
        print("c is greater")