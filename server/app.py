from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)    

@app.route('/', methods=['POST'])
@cross_origin()
def index():
    if request.method == 'POST':
        request.form.get('username')
    
    return 

if __name__ == "__main__":
    app.run(debug=True)