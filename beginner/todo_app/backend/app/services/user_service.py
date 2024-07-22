from sqlalchemy.orm import Session

from app.db.schemas import UserCreate
from app.repository import UserRepository
from app.core.security import get_password_hash
from app.db.models import User

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_by_username(self, db: Session, username: str):
        return self.user_repository.get_by_username(db, username)

    def create(self, db: Session, user: UserCreate):
        hashed_password = get_password_hash(user.hashed_password)
        db_user = User(username=user.username, hashed_password=hashed_password)
        return self.user_repository.create(db, db_user)
