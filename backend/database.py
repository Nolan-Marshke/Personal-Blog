
import pymongo
from pymongo.mongo_client import MongoClient


cluster = MongoClient("mongodb+srv://NolanM:u0ISO3ALOT2bmldf@cluster0.phcn8.mongodb.net/?appName=Cluster0")
db = cluster["article"]
article_collection = db["articles"]

def get_articles_collection():
    return articles_collection






