from flask import *  
app = Flask(__name__)  
import os

UPLOAD_FOLDER = './images'

@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        path = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(path)
        return render_template("success.html", name = f.filename)  



@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory=UPLOAD_FOLDER, filename=filename,path="./")



if __name__ == '__main__':  
    app.run(debug = True)