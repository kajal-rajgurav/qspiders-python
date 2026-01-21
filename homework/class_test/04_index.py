# wapt to check whether the given data is collection datatype or not if it is collection then check whether it is mutable or immutable>
data=eval(input("enter your data :-"))
if type(data) in (str,list,tuple,set,dict):
    print("yes it is collection datatype")
    if type(data) in (str,tuple):
        print("it is immutable")
    else:
        print("it is mutable")
else:
    print(" no it is not a collection  of data type")