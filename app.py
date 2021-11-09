from flask import *
import os
from fileOperations import getDataFromFile, writeDataToFile
from imageOperations import imageSaver
from database import mongo
from mongodbOperations import addTags, getAllTags, getSpecificTags
app = Flask(__name__)  
from config import url,UPLOAD_FOLDER


@app.route('/')  
def upload():

    #here getting informations like total no of uploads and downloads and no of images in image server
    payload = {
        "total_number_of_images" : len(os.listdir(UPLOAD_FOLDER)),
        "total_number_of_upload" : getDataFromFile("total_no_of_upload"),
        "total_number_of_download" : getDataFromFile("total_no_of_download")
    }  
    return render_template("file_upload_form.html",payload=payload)  


@app.route('/index')  
def uploads():

    #here getting informations like total no of uploads and downloads and no of images in image server
    payload = {
        "total_number_of_images" : len(os.listdir(UPLOAD_FOLDER)),
        "total_number_of_upload" : getDataFromFile("total_no_of_upload"),
        "total_number_of_download" : getDataFromFile("total_no_of_download")
    }  
    return render_template("file_upload_form.html",payload=payload)  


@app.route('/goback')
def goback():
    return redirect('/')


#getting all images 
@app.route('/getAllImages')
def getAllImages():
    org_images = [{"url":url + "/getImage/" + file , "name":file} for file in os.listdir(UPLOAD_FOLDER) if "m_" not in file and "s_" not in file and "l_" not in file ]
    return render_template("view_images.html",payload = {'images' : org_images})  

#uploading single or a multiple file 
@app.route('/uploadFiles', methods = ['POST'])  
def fileUpload():  
    file_count = 0
    if request.method == 'POST':  
        files = request.files.getlist("files")
        for file in files:
            #checking whether the given file is a image file else ignoring them silently
            if file.filename.split(".")[-1] in ['jpg','jfif','jpeg','png']:
                file_count+=1
                #storing image in (original, small, medium, large) sized image in the directory
                imageSaver(file)
        #writing the total no of uploads in a text file
        if(file_count != 0):
            writeDataToFile("total_no_of_upload",int(getDataFromFile("total_no_of_upload"))+1)
            return redirect(url_for('getAllImages'))
        else:
            return render_template("noFilesSelected.html")

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






#getting tag content / viewing all the tags
@app.route('/addTagContent',methods = ['POST'])
def addTagContent():
    image_name = request.values['addTag']
    data = {
        "url":url + "/getImage/s_" + image_name,
        'data': image_name,
    }
    return render_template("tagScreen(addTag).html",payload = data,tags=list(getAllTags()))  



#adding/updating tags for an image
@app.route('/tagSubmission',methods = ['POST'])
def tagSubmission():
    tags_name = request.form.get("tag")
    #to verify that /tagSubmission is called either by tag adding button or else view tag button
    if("home" == request.form.get("sideBar")):
        return render_template("tagScreenHome(viewTag).html",
            tags=list(getAllTags()),
            )  
    if("true" == request.form.get("sideBar")):
        return render_template("tagScreen(viewTag).html",
            tags=list(getAllTags()),
            data={
                "message":{"message":""},
                "tag":tags_name,
                "data":getSpecificTags(tags_name)
                }
            )  
    else:
        image_name = request.form.get("image_name")
        message = addTags(tags_name,image_name)
        return render_template("tagScreen(viewTag).html",
            tags=list(getAllTags()),
            data={
                "message":message,
                "tag":tags_name,
                "data":getSpecificTags(tags_name)
                }
            )  
