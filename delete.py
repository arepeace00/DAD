# import mysql.connector library
import mysql.connector

# create MySql connection Object
# to connect python file MySql server
mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "",
database="gym_db") 

#create cursor object using the cursor() method
mycursor = mydb.cursor()

#create cursor object using the cursor() method
mycursor = mydb. cursor()

#update table in MySql
sql="DELETE FROM customer WHERE custID ='B11'"

#execute SQL statements on SQL database
mycursor . execute (sql)

#save changes in database
mydb. commit()

print("Successfully Added")