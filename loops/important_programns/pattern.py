# num=5
# for i in range(num,0,-1):
#     for j in range(i):
#         print('*',end='')
#     print()
#     # without nested for.
# num=6
# for i in range(1,6):
#     print('*'*i)
# # reverse

# num=6
# for i in range(num,0,-1):
#     print('*'*i)

# n=5
# for i in range(1,n+1):
#     print("  "*(n-i)+' *'*i)

# n=5
# for i in range(1,n+1):
#     print(" "*(n-i)+' *'*i)
# for i in range(n,0,-1):
#     print(" "*(n-i)+' *'*i)


# 1
# 22
# 333
# 4444
# 55555
# num=5
# for i in range(1,num+1):
#     for j in range(i):
#         print(i,end='')
#     print()

# 1
# 12
# 123
# 1234
# 12345
# num=5
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()


# A
# AB
# ABC
# ABCD
# ABCDE

# for i in range(1, 6):
#     for j in range(i):
#         print(chr(65 + j), end=" ")
#     print()

# for i in range(ord('A'),6):
#     for j in range(i):
#         print(chr(65+i),end='')
#     print()


# abc


* * * * *
*
*
*
* *









# *****
# *   *
# *   *
# *   *
# *****
row=10
col=10
for i in range(1,row+1):
    if i in (1,row):
        print("* "*col)
    else:
        print('*'+'  '*(col-2)+' *')


n=5
for i in range(1,n+1):
    for j in range(n,0)



