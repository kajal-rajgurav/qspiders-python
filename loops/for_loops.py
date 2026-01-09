# wapt access the values from the multiple datatypes.

# st={10,20,30,40,80}
# for i in st:
#     print(i)

# lst=[10,30,'apple',40]
# for value in lst:
#     print(value)

# tp=(1,2,3,4,5)
# for item in tp:
#     print(item)

# s={10,20,30,40,80}
# for element in s:
#     print(element)

# d={'a':1,'b':2,'c':3}
# for k in d:
#     print(k)
#     print(d[k])




# wapt extract to all the even from list.


# lst=[1,2,3,4,5,8,6,10,20]
# lst_evens=[]
# for i in lst:
#     if(i%2==0):
#         lst_evens.append(i)
# print(lst_evens)
        
# wapt to exract the vowels from the given string .
# st='happy new year'
# new_st=''
# for i in st:
#     if i in 'AEIOUaeiou':
#         new_st+=i
# print(new_st)

# wapt extract upper case ,lowercase,digit,speacial separetely



# greet='Happy New Year!!@2026'
# upper=''
# lower=''
# digit=''
# special=''
# for char in greet:
#     if char.isupper():
#         upper+=char
#     elif char.islower():
#         lower+=char
#     elif char.isdigit():
#         digit+=char
#     else:
#         special+=char
# print(upper,lower,digit,special)
     
        
# wapt to extract only string data from list of data.

# data=[2,2.4,True,'apple',3+4j,'google',60,'microsoft']
# st=[]
# for i in data:
#     if type(i)==str:
#         st.append(i)
# print(st)


# wapt get to the only sum integer prensent in the tuple.


# tp=(2,'yash',3,True,5.6,'Tarak',5,6+4j)
# Sum=0
# for t in tp:
#     if type(t)==int:
#         Sum+=t
# print(Sum)


# wapt reverse the string 
 

# s='HAPPY'
# rev=''
# for i in s:
#     rev=i+rev
# print(rev)

# wapt to get foll output for foll input given input.
# input
# st='the only limit to our realiazation of tommorow will be our doubts of today'
# word_count={}
# for word in st.split():
#    count=0
#    for ch in st:
#         if ch in 'AEIOUaeiou:
#             count+=1
#    word_count[word]=count
# print(word_count)
# st='the only limit to our realiazation of tommorow will be our doubts of today'
# for word in st.split():

n=5
for i in range(n+1):
    for j in range(i):
        print(i,j)
     


#     o/p:
#     1,0
#     1,1
#     2,0
#     2,1
#     2,2
#     3,0
#     3,1
# 3,2 
# 3,3
# 4,0,1,2,3,4


for i in range(1, 5):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


    
* * * *
* * *
* *
*
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()


