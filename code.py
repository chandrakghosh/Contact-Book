import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ChandrAK77",
    database="my_database"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
conn.close()
