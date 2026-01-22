#  Unpacking keyword arguments using **kwargs

# **kwargs allows a function to accept any number of keyword arguments.

def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_info(name="Kajal", age=21, course="CSE-AIML")
