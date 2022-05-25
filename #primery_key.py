import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="employee_detail"
)

mycursor = mydb.cursor()


mycursor.execute("ALTER TABLE customer ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

