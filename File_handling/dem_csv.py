with open ("emp.csv",'w') as file:
    file.write('emp_id,name,age,salary,depmt\n')
    file.writelines(['101,steve,30,5000,hr\n',
                     '102,smith,25,4400,devops\n',
                     '103,rose,26,4800,dev\n'])