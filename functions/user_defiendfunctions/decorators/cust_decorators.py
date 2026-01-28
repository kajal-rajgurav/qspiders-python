# custamize decorators are paramentrs decorators.
from time import sleep
def cus_delay(sec):
    def delay(func):
        def wrapper(*args,**kwargs):
            sleep(sec)
            return func(*args,**kwargs)
        return wrapper
    return delay
@cus_delay(1)  #greet==>delay(greet)==>wrapper
def greet():
    return 'hello world'
@cus_delay(2)
def greeting(name):
    return f'hello {name}'
@cus_delay(3)
def add(a,b):
    return a+b