from sqlalchemy.orm import Session
from app import models, schemas

# CREATE
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# READ ALL (with query params)
def get_users(db: Session, skip: int = 0, limit: int = 10, min_age: int = None):
    query = db.query(models.User)

    if min_age:
        query = query.filter(models.User.age >= min_age)

    return query.offset(skip).limit(limit).all()

# READ ONE
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# UPDATE
def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = get_user(db, user_id)

    if not db_user:
        return None

    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user

# DELETE
def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)

    if not db_user:
        return None

    db.delete(db_user)
    db.commit()
    return db_user