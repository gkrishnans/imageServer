from types import MethodDescriptorType
from flask import *
import os
from fileOperations import getDataFromFile, writeDataToFile
from imageOperations import imageSaver
from database import mongo
from mongodbOperations import addTags, getAllTags
app = Flask(__name__)  

url = "http://127.0.0.1:5000"
UPLOAD_FOLDER = './images'

@app.route('/')  
def upload():

    #here getting informations like total no of uploads and downloads and no of images in image server
    payload = {
        "total_number_of_images" : len(os.listdir(UPLOAD_FOLDER)),
        "total_number_of_upload" : getDataFromFile("total_no_of_upload"),
        "total_number_of_download" : getDataFromFile("total_no_of_download")
    }  
    return render_template("file_upload_form.html",payload=payload)  


#getting all images 
@app.route('/getAllImages')
def getAllImages():
    org_images = [{"url":url + "/getImage/" + file , "name":file} for file in os.listdir(UPLOAD_FOLDER) if "m_" not in file and "s_" not in file and "l_" not in file ]
    return render_template("view_images.html",payload = {'images' : org_images})  



#uploading single or a multiple file 
@app.route('/uploadFiles', methods = ['POST'])  
def fileUpload():  
    if request.method == 'POST':  
        files = request.files.getlist("files")
        for file in files:
            #checking whether the given file is a image file else ignoring them silently
            if file.filename.split(".")[-1] in ['jpg','jfif','jpeg','png']:
                #storing image in (original, small, medium, large) sized image in the directory
                imageSaver(file)
        #writing the total no of uploads in a text file
        writeDataToFile("total_no_of_upload",int(getDataFromFile("total_no_of_upload"))+1)
        return redirect(url_for('getAllImages'))


#getting image directly from a directory
@app.route('/getImage/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory=UPLOAD_FOLDER, filename=filename,path="./")


#downloads available for small, medium, large 
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




