a=10
def outer():
    b=20
    x=40
    print(b)
    def inner():
        nonlocal b
        c=30
        b=b+2
        print(b)
        print(c,x,a)
    inner()
    print(b)
outer()


######################
database=[]
def registration(name,phno,gmail,alt_phno=None,alt_gmail=None):
    database.append({'name':nam,
                     'phno':phno,
                     'alt_phno':alt_phno,
                     'gmail':gmail,
                     'alt_gmail':alt_gmail})
    return 'registration is succesfull'
print()


    

