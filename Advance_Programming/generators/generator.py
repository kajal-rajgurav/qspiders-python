# # wapt generate infinite numbers.
# def infinite_num():
#     i=1
#     while True:
#         yield i
#         i+=2





# wapt generate fibbonac  numbers.
 
# from time import sleep

# # def fibo_series():
# #     a,b=0,1
# #     while True:
# #         yield a
# #         next_num=a+b 
# #         a,b=b,next_num
# # print(fibo_series())
# # for v in fibo_series():
# #     print(v)
# #     sleep(1)


# # wapt to generate prime number.


# # def prime_nums():
# #     num=2
# #     while True:
# #         count=0
# #         for i in range(1,num+1):
# #             if num%i==0:
# #                 count+=1
# #         if count==2:
# #             yield num
# #         num+=1
# # g=prime_nums()
# # for v in g:
# #     print(v)
# #     sleep(1)

# # wapt generate perfect numbera.


# def perfect_nums():
#     num=1
#     while True:
#         sum=0
#         for i in range(1,num):
#             if num%i==0:
#                 sum+=1
#         if sum==num:
#             yield num
#         num+=1
# g=perfect_nums()
# for v in g:
#     print(v)
#     sleep(1)

# # wapt print list of only  squre of the even numbers present inside given list. .
numbers=[1,2,3,4,5,6,7,8,9,10]
squre_of_even=[]
i=0
while i<len(numbers):
    if numbers[i]%2==0:
        (squre_of_even.append(numbers[i]**2))
    i+=1
print(squre_of_even)

    ##########################################################
# print([number**2 for number in numbers if number%2==0])

# using function

# def lst_sq(numbers,square_of_even=[],i=0):
#     if i<len(numbers):
#         if numbers[i]%2==0:
#             square_of_even.append(numbers[i]**2)














# wapt get length of Name
# names=['apple','microsoft','tcs','yahoo','google']

# print(list(len(name) for name in names))######using generator 


# print({k:v for k,v in names} )
# print({i:len(i) for i in names.split()})

# print(dict(name,len(name)) for in name in names)









print([i for i in range(1,20)if i%2!=0 ])