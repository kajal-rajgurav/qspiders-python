# import sqlite3
# conn=sqlite3.connect("my_databse.db")
# cursor=conn.cursor()
# print("database connect successsfullly")
# conn.close()

import sqlite3
conn=sqlite3.connect("my_databse.db")
cursor=conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               age INTEGER,
               email TEXT UNIQUE
               )'''

)
cursor.execute('''INSERT INTO users VALUES(101,'yash',23,'abc@gmail.com')''')
users=cursor.execute('''SELECT * FROM  users''')
for value in users.fetchall():
    print(value)
conn.commit()
conn.close()
print("USERS TABLE inserted SUCCESSFULLY")