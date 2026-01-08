# wapt to run the loop contineusouly untill user enters proper password.

# saved_password='Py@123'
# while True:
#     my_pass=input("enter your password:")
#     if my_pass==saved_password:
#         print("login succesfull...")
#         break
#     else:
#         print("wrong password")

# wapt to guess the number.

saved_number=19
while True:
    num=int(input("enter your guessing number:-"))
    if num==saved_number:
        print("wow guess corrected")
        break
    elif num>saved_number:
        print("enter lesser than this number ")
    else:
        print("enter the greater than this number")

