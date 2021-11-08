import os
#url = "http://127.0.0.1:5000"
url = "http://13.250.35.58:80"
UPLOAD_FOLDER = './images'
DATA_FILE = './data/data.txt'
#sDBNAME = os.getenv('db')
USERNAME = os.getenv('name')
PASSWORD = os.getenv('password')
MONGO_URL = "mongodb+srv://"+USERNAME+":"+PASSWORD+"@python-project.svaov.mongodb.net/imageServer?retryWrites=true&w=majority"