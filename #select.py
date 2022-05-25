import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="employee_detail"
)
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult=mycursor.fetchall() # select all detail in custemer table
for x in myresult:
    print(x)

