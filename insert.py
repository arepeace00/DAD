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

#insert data into table
sql = "INSERT INTO customer (custID, custName, telNo) VALUES ('B12', 'Alex LIM','017-310'),('B100','Ammar','017-109')"

#execute sQL statements on SQL dataoase
mycursor.execute(sql)

#save changes in database
mydb.commit()

print("Successfully Added")