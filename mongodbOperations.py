from database import mongo

url = "http://127.0.0.1:5000"

def getAllTags():
    result = mongo.db.tags.find()
    print("$$@%#$%#$^%#$%^#^$^$#^%",result)
    return(list(result))

def addTags(tags,image_name):
    result = list( mongo.db.tags.find({'name': tags}))
    img = {
        "url":url + "/getImage/" + image_name,
        "name":image_name
    }
    print("^^^^^^",result)
    if(len(result) == 0):
        print("******",list(result))
        mongo.db.tags.insert_one({'name': tags, 'tagged_images': [img]})
    else:
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        values = list(result)[0]['tagged_images']
        if(img not in values):
            print("###",values)
            values.append(img)
            mongo.db.tags.update_one({'name': tags}, {"$set": {'tagged_images': values}})
        else:
            return {"message":"already added successfully"}    
    return {"message":"tag added successfully"}    

