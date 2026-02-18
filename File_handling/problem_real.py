from time import sleep
def ip_address_products_data(path):
    with open(path)as file:
        return [line.split()[2].strip(',') for line in file ]
IP_address=ip_address_products_data(r"C:\Users\rajgu\OneDrive\Desktop\Qspiders_practice\python\product_search_data_1000 (1).txt")
print(f'total number of ip address in file is{len(IP_address)}')

uniq_ip=set(IP_address)
print(f'total number of unique ip address is {len(uniq_ip)}')
ip_count={ip_ads:IP_address.count(ip_ads)for ip_ads in IP_address}
print(f'ip address and its count is{ip_count}')
s=sorted(ip_count,key=lambda IP:ip_count[IP])
print(f'most repeated tp address is {s[-1]}')
print(f'least repeated tp address is {s[0]}')