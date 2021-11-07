from types import MethodDescriptorType
from flask import *
import os
from fileOperations import getDataFromFile, writeDataToFile
from imageOperations import largeImage, mediumImage, smallImage  
from database import mongo
from mongodbOperations import addTags, getAllTags
app = Flask(__name__)  

url = "http://127.0.0.1:5000"
UPLOAD_FOLDER = './images'

@app.route('/')  
def upload():
    payload = {
        "total_number_of_images" : len(os.listdir(UPLOAD_FOLDER)),
        "total_number_of_upload" : getDataFromFile("total_no_of_upload"),
        "total_number_of_download" : getDataFromFile("total_no_of_download")
    }  
    return render_template("file_upload_form.html",payload=payload)  

@app.route('/getAllImages')
def getAllImages():
    org_images = [{"url":url + "/getImage/" + file , "name":file} for file in os.listdir(UPLOAD_FOLDER) if "m_" not in file and "s_" not in file and "l_" not in file ]
    images = [file for file in os.listdir(UPLOAD_FOLDER) if "m_" not in file and "s_" not in file and "l_" not in file]
    return render_template("view_images.html",payload = {'images' : org_images,'names':images})  


def imageSaver(file):
        filename = file.filename
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)
        smallImage(filename)
        mediumImage(filename)
        largeImage(filename)

@app.route('/uploadFiles', methods = ['POST'])  
def fileUpload():  
    print(1)
    if request.method == 'POST':  
        files = request.files.getlist("files")
        print("-----",files)
        for file in files:
            if file.filename.split(".")[-1] in ['jpg','jfif','jpeg','png']:
                imageSaver(file)
        writeDataToFile("total_no_of_upload",int(getDataFromFile("total_no_of_upload"))+1)
        return redirect(url_for('getAllImages'))


@app.route('/getImage/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory=UPLOAD_FOLDER, filename=filename,path="./")

@app.route('/downloads/image', methods = ['GET'])
def getImageDownload():
    image = request.args.get("file")
    writeDataToFile("total_no_of_download",int(getDataFromFile("total_no_of_download"))+1)
    return send_file(UPLOAD_FOLDER + "/" + image, as_attachment=True)

@app.route('/tags/add',methods = ['POST'])
def addTagss():
    image_name = request.values['addTag']
    data = {
        "url":url + "/getImage/s_" + image_name,
        'data': image_name,
        "state":'none'
    }
    return render_template("tagScreen.html",payload = data,data = json,state="TagListBlock",message="",tags=list(getAllTags()))  

@app.route('/addTag',methods = ['POST'])
def updateTags():
    tags = request.form.get("tag")
    image_name = request.form.get("image_name")
    message = addTags(tags,image_name)
    image_name = ""
    data = {
        "url":url + "/getImage/s_" + image_name,
        'data': image_name,
        "state":'none'
    }

    return render_template("tagScreen.html",payload = data,data = json,state="updateTagsBlock",message=message,tags=list(getAllTags()))  


@app.route('/tags')
def getTags():
    return render_template("tagScreen.html",payload = {},data = json,state="updateTagsBlock",message="",tags=list(getAllTags()))  




