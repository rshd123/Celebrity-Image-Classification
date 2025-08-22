from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/classify_image', methods=['POST','GET'])
def classify_image():
    image_data=request.form['image_data'];
    res=jsonify(util.classify_image(image_data))

    return res.headers.add('Access-Control-Allow-Origin', '*')

if __name__ == '__main__':
    print("Server is running...")
    util.load_saved_artifacts()
    app.run(port=5000)
    
