
import pymongo
from pymongo.mongo_client import MongoClient
import schemas


cluster = MongoClient("mongodb+srv://NolanM:u0ISO3ALOT2bmldf@cluster0.phcn8.mongodb.net/?appName=Cluster0")
db = cluster["article"]
article_collection = db["articles"]

def get_articles_collection():
    return article_collection

def delete_articles_collection(article: schemas.Article):
    article_collection.insert_one(article)
    return article

def delete_articles_collection(article_id: int):
    article_collection.delete_one({"_id": article_id})
    return article_id

def update_articles_collection(article_id: int, article: schemas.Article):
    article_collection.update_one({"_id": article_id}, {"$set": article})
    return article












