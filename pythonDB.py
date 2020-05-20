# Python-with-database

import mysql.connector
import pandas as pd

file = pd.read_csv("friends.csv")
print(file)

tb = [int(input(f"select table {i+1}:")) for i in range(4)]
head = [i for i in file]
selected_columns = ['name']
for i in tb:
    selected_columns.append(head[i])

l=[]
t=[]
for j in range(0,len(tb)):
    for i in selected_columns:
        t.append(file[i][j])
    l.append(tuple(t))
    t.clear()

mydb = mysql.connector.connect(host="localhost", user="root",passwd="mysql@123", database="tutorial1")
mycursor = mydb.cursor()


for i in l:
    mycursor.execute(f"insert into marks values{i}")     # marks is the table name
    mydb.commit()
    
mycursor.execute("select * from marks")

data = mycursor.fetchall()
for i in data:
    print(i)
