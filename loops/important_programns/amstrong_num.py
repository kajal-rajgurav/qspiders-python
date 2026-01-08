# the numbers that are two digits means greater than 9 
num=int(input("enter the number:-"))
if num>9:
    str_num=str(num)        #have to convert into string for getting length rather than it will print one by one
    sum=0
    for digit in str_num:
        sum+=int(digit)**len(str_num)
    if sum==num:
        print("yes it is prime number...")
    else:
        ("no it is not a prime number")