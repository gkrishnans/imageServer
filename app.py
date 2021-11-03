from flask import *

from imageOperations import largeImage, mediumImage, smallImage  
app = Flask(__name__)  
import os

url = "http://127.0.0.1:5000"

UPLOAD_FOLDER = './images'

@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  


@app.route('/os')  
def result():  
    data = {
        "original":url + "/uploads/acf.jpeg",
        "small":url + "/uploads/s_acf.jpeg",
        "medium":url + "/uploads/m_acf.jpeg",
        "large":url + "/uploads/l_acf.jpeg",

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
        "name" : filename,
        "original":url+"/getImage/" + filename,
        "small":url + "/getImage/s_" +filename,
        "medium":url + "/getImage/m_" + filename,
        "large":url + "/getImage/l_" + filename,
        }
        return render_template("result.html",data=data)



@app.route('/getImage/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory=UPLOAD_FOLDER, filename=filename,path="./")



if __name__ == '__main__':  
    app.run(debug = True)