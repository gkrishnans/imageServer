from flask import render_template,Flask, request
from flask.json import jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"


@app.route("/greeting")
def greeting():
    return render_template("index.html")

import os
UPLOAD_FOLDER = './images'


@app.route("/fileUpload", methods=['GET', 'POST'])
def fileUpload():
    if request.method == 'POST':
        file1 = request.files['file1']
        path = os.path.join(UPLOAD_FOLDER, file1.filename)
        file1.save(path)
        return jsonify({"message":"image uploaded successfully", "success":True})


@app.route("/getAllImages", methods=['GET', 'POST'])
def getAllImages():
        data = []
        return jsonify({"message":"image downloaded successfully", "data":data,"success":True})
