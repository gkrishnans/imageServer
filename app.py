from flask import *
import os
from fileOperations import getDataFromFile, writeDataToFile
from imageOperations import largeImage, mediumImage, smallImage  

app = Flask(__name__)  

url = "http://127.0.0.1:5000"
UPLOAD_FOLDER = './images'


@app.route('/')  
def upload():
    payload = {
        "total_number_of_images" : len(os.listdir(UPLOAD_FOLDER))*4,
        "total_number_of_upload" : getDataFromFile("total_no_of_upload"),
        "total_number_of_download" : getDataFromFile("total_no_of_download")
    }  
    return render_template("file_upload_form.html",payload=payload)  


@app.route('/getAllImages')
def getAllImages():
    org_images = [url + "/uploads/" + file for file in os.listdir(UPLOAD_FOLDER) if "_" not in file]
    print( org_images)

    return render_template("view_images.html",payload = {'images' : org_images})  

@app.route('/os')  
def result():  
    data = {
        "original":url + "/uploads/acf.jpeg",
        "small":url + "/uploads/s_acf.jpeg",
        "medium":url + "/uploads/m_acf.jpeg",
        "large":url + "/uploads/l_acf.jpeg",
    }
    return render_template("result.html",data=data)  

def imageSaver(f):
        print(f)
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

@app.route('/uploadFiles', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        files = request.files.getlist("files")
        for file in files:
            imageSaver(file)
        writeDataToFile("total_no_of_upload",int(getDataFromFile("total_no_of_upload"))+1)
        return {'success' : True}
        #return render_template("result.html",data=data)



@app.route('/getImage/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory=UPLOAD_FOLDER, filename=filename,path="./")



if __name__ == '__main__':  
    app.run(debug = True)