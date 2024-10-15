# import mysql.connector library
import mysql.connector

# create MySql connection Object
# to connect python file MySql server
mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "",
database="staff_trainingDB") 

#create cursor object using the cursor() method
mycursor = mydb.cursor()

#create table in MySQL database
sql = "CREATE TABLE Staff_Training(staffID VARCCHAR(10) NOT NULL,custName VARCHAR(100),telNo CHAR(12), PRIMARY KEY(staffID))"

#execute SQL statements on SQL database
mycursor.execute(sql)

#save changes in database
mydb.commit()

print("Successfully Create Table")