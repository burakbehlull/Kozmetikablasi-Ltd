from flask import Flask, request, jsonify, render_template
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

@app.route('/api/settings')
@cross_origin()
def getUser():
    cursor.execute("SELECT * FROM site_settings")
    site_settings = cursor.fetchall()
    
    return jsonify(site_settings)

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/api/settings/update', methods=['POST', 'GET'])
@cross_origin()
def settingsUpdate():
    if request.method == 'POST':
        title = request.form.get('title')
        subtitles = request.form.get('subtitles')
        
        title_update = f"UPDATE site_settings SET title = '{title}' WHERE id = 1"
        subtitles_update = f"UPDATE site_settings SET subtitles = '{subtitles}' WHERE id = 1"
        
        cursor.execute(title_update)
        cursor.execute(subtitles_update)
        mydb.commit()
        return "basirili"
    else:
        return "basirisiz"
        

if __name__ == "__main__":
    app.run(debug=True)