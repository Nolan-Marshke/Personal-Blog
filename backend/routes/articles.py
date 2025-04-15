from fastapi import APIRouter, HTTPException, status
from typing import List
import schemas
from database import (
    get_articles_collection, 
    get_article_by_id,
    create_articles_collection, 
    delete_articles_collection, 
    update_articles_collection
)

router = APIRouter()

@router.get("/", response_model=List[schemas.Article])
def get_articles():
    articles = get_articles_collection()
    return articles
    
@router.get("/{article_id}", response_model=schemas.Article)
def get_article(article_id: str):
    article = get_article_by_id(article_id)
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with id {article_id} not found"
        )
    return article

@router.post("/", response_model=schemas.Article, status_code=status.HTTP_201_CREATED)
def create_article(article: schemas.ArticleCreate):
    created_article = create_articles_collection(article)
    return created_article

@router.delete("/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_article(article_id: str):
    deleted = delete_articles_collection(article_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with id {article_id} not found"
        )
    return {"detail": "Article deleted successfully"}

@router.put("/{article_id}", response_model=schemas.Article)
def update_article(article_id: str, article: schemas.ArticleCreate):
    updated_article = update_articles_collection(article_id, article)
    if not updated_article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with id {article_id} not found"
        )
    return updated_article




