num=int(input("enter the numebr"))
sum=0
for i in range(1,6):
    if num%i==0:
        sum+=i
if sum==num:
    print("yes it is perfect num")
else:
    print("no it is not ")