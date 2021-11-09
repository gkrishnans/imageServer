from flask import Flask
from config import MONGO_URL
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = MONGO_URL
mongo = PyMongo(app)