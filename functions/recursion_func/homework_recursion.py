data=[87,"hai","python",8.3,"congratulations"]
new_lst=[]
for i in data:
    if type(i)==str:
        new_lst.append(i)
        print("yes it string")
    else:
        print("no a string")