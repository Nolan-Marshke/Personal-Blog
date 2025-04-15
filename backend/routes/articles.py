from fastapi import APIRouter, Depends, HTTPException
import schemas


router = APIRouter()





@router.get("/articles")
def get_articles():
    articles = get_articles_collection()
    return articles
    



@router.get("/articles/{article_id}")
def get_article(article_id: int):
    article = get_articles_collection()
    return article


@router.post("/articles")
def create_article(article: schemas.Article):
    article = create_articles_collection()
    return article


@router.delete("/articles/{article_id}")
def delete_article(article_id: int):
    article = delete_articles_collection()
    return article      


@router.put("/articles/{article_id}")
def update_article(article_id: int, article: schemas.Article):
    article = update_articles_collection()
    return article




