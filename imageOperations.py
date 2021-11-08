from PIL import Image  
import os

from config import UPLOAD_FOLDER



def rotate():
    im = Image.open("./images/gk_image2.jpg")  
    im.show()  
    imim = im.rotate(45)  
    imim.show()


def smallImage(img_name):
    im = Image.open("./images/" + img_name)  
    im.thumbnail((220,220))  
    im.save('images/'+ "s_"+img_name)  
    #image1 = Image.open('images/smallImage.jpg')  
    #image1.show() 


def mediumImage(img_name):
    im = Image.open("./images/" + img_name)  
    im.thumbnail((400,400))  
    im.save('images/'+ "m_"+img_name)  


def largeImage(img_name):
    im = Image.open("./images/" + img_name)  
    im.thumbnail((1500,1500))  
    im.save('images/'+ "l_"+img_name)  


def imageSaver(file):
        filename = file.filename
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)
        smallImage(filename)
        mediumImage(filename)
        largeImage(filename)