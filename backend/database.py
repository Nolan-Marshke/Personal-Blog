import pymongo
from pymongo.mongo_client import MongoClient
from bson import ObjectId
import schemas
from datetime import datetime
from typing import List
import os
from dotenv import load_dotenv
from config import settings

load_dotenv()

# Connect to MongoDB using settings
cluster = MongoClient(settings.MONGO_URI)
db = cluster[settings.DATABASE_NAME]
article_collection = db[settings.COLLECTION_NAME]

def get_articles_collection() -> List[dict]:
    """Retrieve all articles from the collection"""
    articles = []
    for article in article_collection.find():
        article["id"] = str(article["_id"])
        del article["_id"]
        articles.append(article)
    return articles

def get_article_by_id(article_id: str) -> dict:
    """Retrieve a specific article by ID"""
    try:
        article = article_collection.find_one({"_id": ObjectId(article_id)})
        if article:
            article["id"] = str(article["_id"])
            del article["_id"]
            return article
        return None
    except:
        return None

def create_articles_collection(article: schemas.ArticleCreate) -> dict:
    """Create a new article in the collection"""
    article_dict = article.dict()
    article_dict["created_at"] = datetime.now()
    article_dict["updated_at"] = datetime.now()
    
    result = article_collection.insert_one(article_dict)
    article_dict["id"] = str(result.inserted_id)
    return article_dict

def update_articles_collection(article_id: str, article: schemas.ArticleCreate) -> dict:
    """Update an existing article in the collection"""
    try:
        article_dict = article.dict()
        article_dict["updated_at"] = datetime.now()
        
        article_collection.update_one(
            {"_id": ObjectId(article_id)},
            {"$set": article_dict}
        )
        
        updated_article = article_collection.find_one({"_id": ObjectId(article_id)})
        if updated_article:
            updated_article["id"] = str(updated_article["_id"])
            del updated_article["_id"]
            return updated_article
        return None
    except:
        return None

def delete_articles_collection(article_id: str) -> bool:
    """Delete an article from the collection"""
    try:
        result = article_collection.delete_one({"_id": ObjectId(article_id)})
        return result.deleted_count > 0
    except:
        return False












