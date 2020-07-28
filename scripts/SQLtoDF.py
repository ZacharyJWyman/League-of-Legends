import pandas as pd
import mysql.connector

#Connect to SQL database. 
mydb = mysql.connector.connect(
user='dbmasteruser', 
password='#(KT.%KXF~?oa0((3C]B+c:D$_u|~%7%',
host='ls-ab4099840472652cffcf8a93ff831350de0b9549.cxjoxjn3ihvz.us-west-2.rds.amazonaws.com',
database='league',
port='3306')

mycursor = mydb.cursor()

#SQL Table 
table_name = 'champions'

#Convert table into dataframe.
mycursor.execute('SELECT * FROM' + ' ' + table_name)
names = mycursor.column_names
table_rows = mycursor.fetchall()
data = pd.DataFrame(table_rows)
data.columns = [i for i in names]
