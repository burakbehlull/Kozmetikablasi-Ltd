from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import mysql.connector

app = Flask(__name__)
cors = CORS(app)  

mydb = mysql.connector.connect(
    host= "127.0.0.1",
    user="root",
    password="",
    database="kozmetikabladb"
)  
cursor = mydb.cursor(dictionary=True)



@app.route('/')
@cross_origin()
def index():
    return "<h1>INDEX</h1>"

@app.route('/api')
@cross_origin()
def getUser():
    cursor.execute("SELECT * FROM site_settings")
    site_settings = cursor.fetchall()
    
    return jsonify(site_settings)


if __name__ == "__main__":
    app.run(debug=True)