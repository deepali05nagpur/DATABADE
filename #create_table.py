import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="employee_detail"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE students(name VARCHAR (225),address VARCHAR(255))")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)