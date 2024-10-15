# import mysql.connector library
import mysql.connector

# create MySql connection Object
# to connect python file MySql server
mydb = mysql.connector.connect(
host = "localhost",
user = "user",
password = "123456Qwert") 

print(mydb)

#test connection
if(mydb):
	print("Connection Successfully")
else:
	print("Connection unsuccessfully")