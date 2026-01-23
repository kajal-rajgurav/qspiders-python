# check whether prime or not 
# prime numbers series generation.

def isprime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
print(isprime(1))
print(isprime(2))
print(isprime(3))

from time import sleep
i=1
while True:
    if isprime(i):
        print(i)
        sleep(i)
    i+=1

# another way
def isprime(num):
    if num <=1:
        return False
    count=0
    for i in range(1,num+1):
        if num%1==0:
            count+=1
        return count==0
