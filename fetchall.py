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

# Query statement
sql = "SELECT * FROM customer"

#execute SQL statements on SQL database
mycursor.execute (sql)

#fetch all data and store inside variable result
myresult = mycursor.fetchall()

#use for loop to fetch all data in the table
for row in myresult:
	print(row)

print("Successfully Added")