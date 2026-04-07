from sqlalchemy.orm import Session
from models import User, RefreshToken
from auth import hash_password

def create_user(db: Session, email: str, password: str):
    user = User(email=email, hashed_password=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def store_refresh_token(db: Session, user_id: int, token: str):
    db_token = RefreshToken(user_id=user_id, token=token)
    db.add(db_token)
    db.commit()

def validate_refresh_token(db: Session, token: str):
    return db.query(RefreshToken).filter(RefreshToken.token == token).first()