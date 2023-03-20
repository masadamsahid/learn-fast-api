from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return { 'data': 'blog list' }


@app.get('/blog')
def getBlogs(limit=10, published: bool=True, sort: Optional[str] = None):
    if published:
        return { 'data': f'{limit} published blogs from the DB' }
    else:
        return { 'data': f'{limit} blogs from the DB' }


@app.get('/blog/unpublished')
def unpublishedBlog(id: int):
    # fetch blog with id = id
    return { 'data': 'all unpublished blogs' }


@app.get('/blog/{id}')
def showBlog(id: int):
    # fetch blog with id = id
    return { 'data': id }


@app.get('/blog/{id}/comments')
def showBlogComments(id):
    # fetch comments of blog with id = id
    return { 'data': ['1', -2] }


@app.get('/about')
def about():
    return { 'data': 'about page' }


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return { 'data': f"Blog is created with title as '{request.title}'" }


# if __name__ == "__main__":
#     uvicorn.run(app, host='127.0.0.1', port=9000)