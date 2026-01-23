def isArmstrong(num):
    if num<10:
        return True
    digits=str(num)
    Sum=0
    for digit in digits:
        Sum+=int(digit)**len(digits)
    return Sum==num
from time import sleep
i=1
while True:
    if isArmstrong(i):
        print(i)
        sleep(1)
    i+=1