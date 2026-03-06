import threading
from time import sleep
def numbers():
    for i in range(5):
     print("numbers:",i)

def letters():
   for letter in ['A','B','C','D']:
      print("letter:",letter)
t1=threading.Thread(target=numbers)
t2=threading.Thread(target=letters)
t1.start()
t2.start()
t1.is_alive()
t1.join()
t2.join()
sleep(1)
print("program finished")
