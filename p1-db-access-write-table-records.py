import mysql.connector
import pyodbc
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=F:\Python\Database1.accdb;')
cursor = conn.cursor()
#cursor.execute('select * from table1')
sql = "INSERT INTO table1 (name, marks) VALUES ('asad', 40)"
#val = ("asad", 40)
cursor.execute(sql)
conn.commit()
print(cursor.rowcount, "record inserted.")
