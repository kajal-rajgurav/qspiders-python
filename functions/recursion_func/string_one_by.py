# wapt print one by one char from given string.
st='happy'
def chr_str(st,i=0):
    if i<len(st):
        print(st[i])
        chr_str(st,i=i+1)
chr_str("happy")
chr_str([1,2,34,5])


# wapt to extract all the string data from the list using Recursion.
lst=[10,'apple',30,'google',45,'tcs','ibm',5.6,True]
out=[]
i=0
while i<len(lst):
    if type(lst[i])==str:
        out.append(lst[i])
    i+=1
print(out)
def str_elements(lst,out=[],i=i+1):
    if i<len(lst):
        if type(lst[i])==str:
          out.append(lst[i])
        str_elements(lst,out,i=i+1)
        return out
print(str_elements([10,'apple',30,'google',45,'tcs','ibm',5.6,True]))
