# Python-with-database

import mysql.connector
import pandas as pd

file = pd.read_csv("friends.csv")
print(file)

head = [i for i in file]
print(head)
l=[]
t=[]
for j in range(0,len(file)):
    for i in head:
        t.append(file[i][j])
    l.append(tuple(t))
    t.clear()

mydb = mysql.connector.connect(host="localhost", user="root",passwd="mysql@123", database="tutorial1")
mycursor = mydb.cursor()


for i in l:
    mycursor.execute(f"insert into marks values{i}")
    mydb.commit()
    
mycursor.execute("select * from marks")

data = mycursor.fetchall()
for i in data:
    print(i)
