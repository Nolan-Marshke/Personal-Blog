from pydantic import BaseModel

class Article(BaseModel):
    title: str
    content: str
    published: bool = True


article = Article(title="My First Blog Post", content="This is my first blog post")
print(article.title)
