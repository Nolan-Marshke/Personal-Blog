from pydantic import BaseModel

class Article(BaseModel):
    title: str
    content: str
    published: bool = True
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


article = Article(title="My First Blog Post", content="This is my first blog post")
print(article.title)
