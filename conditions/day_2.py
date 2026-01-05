
    #test case 1:if the percentage  less  than 35
#     print sory u r faild
#     case2: if the per is 35 or greater than35 upto 50 
#     print ur just pass
#    case3: if per is 50 or more than 50 upto 60 
#     print pass with second class
#     case4: if per 60 or above60 upto 80 
#     print passed first class
#     case5:if per80 is or above 80 including 100
#     print first with distiction
per=float(input('enter your percentage'))
if per<35:
    print("sorry your faield")
elif per<50:
    print("you are just pass")
elif per<60:
    print("you are passed with second class")
elif per<80:
    print("you are passed with first class")
elif per<=100:
    print("you are passed with first class with dist")
else:
    print("wrong input")
