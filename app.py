from flask import *

from imageOperations import largeImage, mediumImage, smallImage  
app = Flask(__name__)  
import os


UPLOAD_FOLDER = './images'

@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  


@app.route('/os')  
def result():  
    data = {
        "original":"http://127.0.0.1:5000/uploads/acf.jpeg",
        "small":"http://127.0.0.1:5000/uploads/s_acf.jpeg",
        "medium":"http://127.0.0.1:5000/uploads/m_acf.jpeg",
        "large":"http://127.0.0.1:5000/uploads/l_acf.jpeg",

    }
    return render_template("result.html",data=data)  

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        filename = f.filename
        path = os.path.join(UPLOAD_FOLDER, filename)
        f.save(path)
        smallImage(filename)
        mediumImage(filename)
        largeImage(filename)
        #return render_template("success.html", name = f.filename)  
        data = {
        "original":"http://127.0.0.1:5000/uploads/" + filename,
        "small":"http://127.0.0.1:5000/uploads/s_" +filename,
        "medium":"http://127.0.0.1:5000/uploads/m_" + filename,
        "large":"http://127.0.0.1:5000/uploads/l_" + filename,
        }
        return render_template("result.html",data=data)



@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory=UPLOAD_FOLDER, filename=filename,path="./")



if __name__ == '__main__':  
    app.run(debug = True)