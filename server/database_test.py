import mysql.connector

mydb = mysql.connector.connect(
    host= "127.0.0.1",
    user="root",
    password="",
    database="kozmetikabladb"
)  
mycursor = mydb.cursor()

# mycursor.execute('CREATE DATABASE kozmetikablaDB')
# mycursor.execute("CREATE TABLE site_settings (title VARCHAR(255), subtitles VARCHAR(255))")

sql = "INSERT INTO site_settings (title, subtitles) VALUES (%s, %s)"
val = ("Kozmetik Abla", "Test")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")