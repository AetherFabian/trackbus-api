from flask_pymongo import pymongo
import os

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

client = pymongo.MongoClient(f'mongodb+srv://{DB_USER}:{DB_PASSWORD}@api.sc4h7.mongodb.net/{DB_NAME}?retryWrites=true&w=majority')
db = client.trackbus