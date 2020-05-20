# Python-with-database

import mysql.connector
import pandas as pd

#Read csv file
file = pd.read_csv("friends.csv")
print(file)

#Selection of Columns
col = [int(input(f"select column {i+1}:")) for i in range(4)]
head = [i for i in file]
selected_columns = ['name']
for i in col:
    selected_columns.append(head[i])

#Selection of data from selected Columns
l=[]
t=[]
for j in range(0,len(tb)):
    for i in selected_columns:
        t.append(file[i][j])
    l.append(tuple(t))
    t.clear()

#Connection to mysql
mydb = mysql.connector.connect(host="localhost", user="root",passwd="mysql@123", database="tutorial1")
mycursor = mydb.cursor()

#Executing Query(inserting the value from csv to mysql)
for i in l:
    mycursor.execute(f"insert into marks values{i}")     # marks is the table name
    mydb.commit()

#Showing the data in output console    
mycursor.execute("select * from marks")
data = mycursor.fetchall()
for i in data:
    print(i)
