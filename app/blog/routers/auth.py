from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from .. import schemas, database, models, JWToken
from ..hashing import Hash



router = APIRouter(
    tags=['Auth']
)

@router.post('/login')
def login(req: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.name == req.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid credentials")
    
    if not Hash.verify(user.password, req.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"Incorrect Password")
    
    # Generate JWT and return it
    access_token = JWToken.create_access_token(
        data={"sub": user.email}
    )
    
    return {'access_token': access_token, "token_type": "bearer"}