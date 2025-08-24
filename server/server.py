from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/classify_image', methods=['POST','GET'])
def classify_image():
    image_data=request.form['image_data']
    result = util.classify_image(image_data)
    
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print("Server is running...")
    util.load_saved_artifacts()
    app.run(port=5000)
    
