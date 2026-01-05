# wapt check whether given character is ALPHABET OR  not  if it is alpha char check is that char vowel or consonet.
# 
# char=input("enter your character")
# if char.isupper() or char.lower():
#     print("yes it is alphabet")
#     if char in 'AEIOUaeiou':
#         print("yes it is vowel")
#     else:
#         print("it is not vowel")
# else:
#     print("is it not alphabet only")

# # wapt check whether given data is string or not 
# # if is a string thrn chrck whether length of astring is multiple of 5

# st=eval(input("enter your data:-"))
# if type(st)==str:
#     print("yes it is string")
#     if len(st)%5==0:
#         print("yes is multiple of 5")
#     else:
#         print("is is not multiple of 5")
# else:
#     print("it is not string")
    # implement login page if user name valid then only collect the password n check the passwrod correct then print login succesfull if the pass is correct.

# reg_user_name='pyspider'
# password='py@123'
# user_name=str(input("enter your name:-"))
# if user_name==reg_user_name:
#     pass_word =str(input("enter your pass"))
#     if password==pass_word:
#         print("login successfull")
#     else:
#         print("wrong password")
# else:
#     print("invalid user name")

# wapt to check whether the given data is collection datatype or not if it is collection then check whether it is mutable or immutable>

data=eval(input("enter your data"))
if type(data)in(str,tuple,set,list,dict):
    print('yes it is collection')
    if type(data)in (str,tuple):
        print("yes it immutable")
    else:
        print("it is  mutable")
else:
    print("it is not collecton")


    