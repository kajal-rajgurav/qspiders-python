from time import sleep
from csv import reader,DictReader
def lst_emps_data(path):
    emps_data=[]
    with open (path)as file:
        head_row=next(file)
        rows=reader(file)
        for row in rows:
            emps_data.append(row)
        return emps_data
emps=lst_emps_data(r"C:\Users\rajgu\OneDrive\Desktop\Qspiders_practice\python\emp.csv")
print(emps)