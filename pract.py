# 1
# 22
# 333
# 4444
# 55555
num=5
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()


# A
# AB
# ABC
# ABCD
# ABCDE

for i in range(1,6):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()
