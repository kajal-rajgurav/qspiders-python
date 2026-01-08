# num=int(input("enter the number"))
# str_num=str(num)
# rev=''
# for digit in str_num:
#     rev=digit+rev
# if str_num==rev:
#     print("yes it pallindrome")
# else:
#     print("not it is not")


# wapt access one by one char from given list of string using while loop and also for loop.


names=['ibm','tcs','ey']
i=0
while i<len(names):
     j=0
     while j<len(names[i]):
        print(names[i][j])
        j+=1
     i+=1
# for ch in names:
#     for name in ch:
#          print(name)

