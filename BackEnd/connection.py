# MySql connection data present here

import mysql.connector as mysql

connection = mysql.connect(
    host="localhost",
    user="root",
    password="DatabasePass@54",
    database="teamformationassistant",
    auth_plugin='mysql_native_password'
)