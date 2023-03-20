from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from .. import database, schemas, models
from ..repository import user as userRepository

router = APIRouter(
    prefix="/user",
    tags=['Users']
)
get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(req: schemas.User, db: Session = Depends(get_db)):
    return userRepository.create(req, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return userRepository.get_by_id(id, db)


