def isperfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return num==sum
from time import sleep
i=1
while True:
    if isperfect(i):
        print(i)
        sleep(1)
    i+=1