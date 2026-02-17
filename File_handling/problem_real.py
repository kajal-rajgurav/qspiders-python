from time import sleep
ip_address=[]as file:
    for line in file:
        ip_address.append(line.split()[2].strip(','))
        print(len(ip_address))