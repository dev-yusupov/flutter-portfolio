# app/dependencies/get_current_user.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.models import User
from app.repository import UserRepository
from app.services.user_service import UserService
from app.core.security import decode_access_token
from app.db.base import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Create an instance of UserRepository
user_repository = UserRepository()

# Pass the instance to UserService
user_service = UserService(user_repository=user_repository)

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
    token_data = decode_access_token(token)
    if token_data is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials.")
    
    username = token_data.username

    if username is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials.")
    
    # Use the instance of UserService
    user = user_service.get_by_username(db=db, username=username)

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials.")
    
    return user
