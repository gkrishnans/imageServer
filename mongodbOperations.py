from database import mongo
from config import url

def getAllTags():
    result = mongo.db.tags.find()
    return(list(result))

def addTags(tags,image_name):
    result = list( mongo.db.tags.find({'name': tags}))
    img = {
        "url":url + "/getImage/" + image_name,
        "name":image_name
    }
    if(len(result) == 0):
        mongo.db.tags.insert_one({'name': tags, 'tagged_images': [img]})
    else:
        values = list(result)[0]['tagged_images']
        if(img not in values):
            values.append(img)
            mongo.db.tags.update_one({'name': tags}, {"$set": {'tagged_images': values}})
        else:
            return {"message":"same tag already added for the image"}    
    return {"message":"tag added successfully"}    

