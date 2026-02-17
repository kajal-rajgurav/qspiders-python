file=open('sample.txt','w')
file.write('python is esay\n')
file.writelines(['abc\n','bcd\n','bv'])
file.close()

###############################################
with open('demo.txt','w')as f:
    f.write('kajal\n')
    f.writelines(['abc\n','bcd\n','bv'])