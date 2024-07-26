import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="mariadb",
    password="password",
    database="mydb",
    charset="utf8mb4",
)