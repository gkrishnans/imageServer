from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://gokul:gokuldb@python-project.svaov.mongodb.net/imageServer?retryWrites=true&w=majority"
mongo = PyMongo(app)



