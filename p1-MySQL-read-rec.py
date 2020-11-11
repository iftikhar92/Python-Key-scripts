import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="ali110ali110", 
  database="db11"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("Rayyan", "Lahore Pakistan")
#mycursor.execute(sql, val)

#mydb.commit()

#print(mycursor.rowcount, "record inserted.")