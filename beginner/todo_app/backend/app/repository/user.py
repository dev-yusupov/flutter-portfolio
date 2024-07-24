from sqlalchemy.orm import Session

from app.db.models import User
from app.db.schemas import UserCreate
from app.core.security import get_password_hash

class UserRepository:
    def get_by_username(self, db: Session, username: str):
        return db.query(User).filter(User.username == username).first()
    
    def create(self, db: Session, user: UserCreate):
        db_user = User(username=user.username, password=user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user