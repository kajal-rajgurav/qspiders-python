num=int(input("enter your number:-"))
if 0<=num<9:
    print("yes it si single digit")
elif 10<=num<99:
    print("yes it is double digit")
elif 100<=num<999:
    print("yes it is having 3 digit")
else:
    print("yes it is having more than 3 digits")