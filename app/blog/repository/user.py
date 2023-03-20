from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import schemas, models
from ..hashing import Hash

def create(req: schemas.Blog, db: Session):
    new_user = models.User(name=req.name, email=req.email, password=Hash.brcypt(req.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


def get_by_id(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not found")

    return user

