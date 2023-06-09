from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas


def get_all(db: Session):
    return db.query(models.Blog).all()


def get_by_id(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")

    return blog


def create(req: schemas, db: Session):
    new_blog = models.Blog(title=req.title, body=req.body, creator_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not found")
    
    blog.delete(synchronize_session=False)
    db.commit()
    
    return 'done'


def update(id: int, req: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not found")
    
    blog.update({ 'title': req.title, 'body': req.body})
    db.commit()

    return 'updated successfully'






