import mysql.connector

mydb= mysql.connector.connect(host="localhost", user="root", password="",database="test_db")
cursor = mydb.cursor()
cursor.execute("select * from customers")
result= cursor.fetchone()
for db in result:
    print(db)

mydb.close()