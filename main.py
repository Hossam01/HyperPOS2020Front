# This is a sample Python script.
from mysql.connector import Error

import mysql.connector
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


connection = mysql.connector.connect(host='10.2.1.190', database='Hyper1_Retail', password='Hyper1@POS'
                                             , user='pos', port='3306')
sql_select_Query = "select * from SYS_USER where user_name = %s and user_password = %s and USER_STATUS  = 1"

x = ("admin", "123",)
mycursor = connection.cursor()
mycursor.execute(sql_select_Query, x)
record = mycursor.fetchone()
print(record)
