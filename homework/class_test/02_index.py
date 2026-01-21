# check whether char is upper ,lower or digit.

char=input('enter your character:-')
if char.isupper():
    print("yes, it is upper char")
elif char.islower():
    print("yes, it is lower char")
elif char.isdigit():
    print("yes, it is digit")
else:
    print("yes, it is speacial char")