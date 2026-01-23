# wapt print one by one char from given string.
st='happy'
def chr_str(st,i=0):
    if i<len(st):
        print(st[i])
        chr_str(st,i=i+1)
chr_str("happy")
chr_str([1,2,34,5])


# wapt to extract all the string data from the list using Recursion.
