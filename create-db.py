# import mysql.connector library
import mysql.connector

# create MySql connection Object
# to connect python file MySql server
mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "") 

#create cursor object using the cursor() method
mycursor = mydb.cursor()

#create database SQL statement
sql= "CREATE DATABASE staff_trainingDB"

#execute SQL statements on SQL database
mycursor.execute(sql)