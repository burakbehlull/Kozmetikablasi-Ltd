from flask import Flask, request, jsonify, url_for, redirect
from flask_cors import CORS, cross_origin
import mysql.connector

app = Flask(__name__)
cors = CORS(app)  

frontend_link = 'http://localhost:8080'

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

@app.route('/update', methods=['POST', 'GET'])
@cross_origin()
def update():
    if request.method == 'POST':
        title = request.form.get('title')
        subtitles = request.form.get('subtitles')
        data_update = f"UPDATE site_settings SET title = '{title}' WHERE subtitles = '{subtitles}'"
        cursor.execute(data_update)
        mydb.commit()
        
    return redirect(url_for(frontend_link))

if __name__ == "__main__":
    app.run(debug=True)