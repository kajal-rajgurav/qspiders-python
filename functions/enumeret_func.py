# enumerate is one of the iterable or builtin function which is used to generate index or value pairs of given collection 
# syntax:enumerate(collection)





# Q12. Add items of two lists
a = [1,2,3,4]
b = [5,6,7,8]
print([a[i]+b[i] for i in range(len(a))])

a=[1,2,3,4]  b=[5,6,7,8]
print(i + j  for i, j in zip(a,b))




# Q13. 
l = [1,2,3,4,5]
print([l[i]**i for i in range(len(l))])







# zip=example=print(zip ([1,2,3,4] , [5,6,7,8]))
# it is one of the iterable so we can acces the value by using for loop or by using type casting and also in interable modes

for v in zip([1,2,3,4] , [5,6,7,8]):
    print(v1,v2)



for v1,v2 in zip([1,2,3,4] , [5,6,7,8]):
    print(v1,v2)

list(zip('abc',[1,2,3,4,5]))
