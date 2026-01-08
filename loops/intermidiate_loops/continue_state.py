# wapt tp orint nubers from 1 to 11 by skipping number 6 and 9.


for i in range(1,12):
    if i in(6,9):
        continue
    print(i)



# wapt to extract all even numbers between the range of 1 to 50 by using continue .

lst_evens=[]
for i in range(1,51):
    if i%2!=0:
        continue
    lst_evens.append(i)
print(lst_evens)


# wapt to extract all the data items from present list.

a=[1,2,3,4,5,8,'hello','haii']
lst=[]
for i in range()