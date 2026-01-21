implement login page if user name valid then only collect the password n check the passwrod correct then print login succesfull if the pass is correct.

reg_user_name='pyspider'
password='py@123'
user_name=str(input("enter your name:-"))
if user_name==reg_user_name:
    pass_word =str(input("enter your pass"))
    if password==pass_word:
        print("login successfull")
    else:
        print("wrong password")
else:
    print("invalid user name")