import mysql.connector

mydb = mysql.connector.connect(
    host= "127.0.0.1",
    user="root",
    password="",
    database="kozmetikabladb"
)  
mycursor = mydb.cursor()

# DATABASE YARATILDI
# mycursor.execute('CREATE DATABASE kozmetikablaDB') 

# BİR TABLO YARATILDI VE İÇERİSİNE DEĞER BASLIKLARI OLUSTURULDU
# mycursor.execute("CREATE TABLE site_settings (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), subtitles VARCHAR(255))");


# mycursor.execute("DROP TABLE site_settings");

# mydb.commit()
