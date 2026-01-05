data=eval(input("enter your data:-"))
# li=['apple','google','yahoo','facebook','instagram']
if type(data)==list:
    print("yes it is list")
    if len(data)%2!=0:
        print("the given data have middle value")
    else:
        print(" but its not having middle value")
else:
    print("no, it is not a list")