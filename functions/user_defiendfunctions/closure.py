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
