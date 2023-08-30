from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv('..env')

username = os.getenv('DBUSERNAME')
password = os.getenv('PASSWORD')

client = MongoClient("localhost", 27017)
db = client.server_db
ad_collection = db.ad_collection
