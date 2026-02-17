# file=open('sample.txt','w')
# file.write('python is esay\n')
# file.writelines(['abc\n','bcd\n','bv'])
# file.close()

# #####################writting another way to file ##########################
# with open('demo.txt','w')as f:
#     f.write('kajal\n')
#     f.writelines(['abc\n','bcd\n','bv'])
########################reading to file

# with open(r"C:\Users\rajgu\OneDrive\Desktop\Qspiders_practice\python\demo.txt",'r')as file:
#     # print(file.read())
#     # print(file.readline())
#     print(file.readlines())

##########appeding to a file
with open('demo.txt','a')as f:
    f.write('\nkajal\n')
    f.writelines(['abc\n','adsvd\n','adfs\n'])