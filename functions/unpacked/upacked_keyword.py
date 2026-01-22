#  Unpacking keyword arguments using **kwargs

# **kwargs allows a function to accept any number of keyword arguments.

def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_info(name="Kajal", age=21, course="CSE-AIML")

# 3️ Unpacking a list or tuple into a function

# You can unpack a list/tuple using *.

def multiply(a, b, c):
    return a * b * c

nums = [2, 3, 4]
print(multiply(*nums))

