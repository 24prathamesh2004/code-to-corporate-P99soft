from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas, crud, auth
from logger import logger

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user.email)
    if db_user:
        raise HTTPException(400, "User exists")

    user = crud.create_user(db, user.email, user.password)
    logger.info(f"User created: {user.email}")
    return {"msg": "User created"}

@app.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user.email)
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(400, "Invalid credentials")

    access = auth.create_access_token({"sub": user.email})
    refresh = auth.create_refresh_token({"sub": user.email})

    crud.store_refresh_token(db, db_user.id, refresh)

    logger.info(f"User login: {user.email}")

    return {
        "access_token": access,
        "refresh_token": refresh,
        "token_type": "bearer"
    }

@app.post("/refresh")
def refresh_token(refresh_token: str, db: Session = Depends(get_db)):
    token = crud.validate_refresh_token(db, refresh_token)
    if not token:
        raise HTTPException(401, "Invalid refresh token")

    new_access = auth.create_access_token({"sub": "user"})
    return {"access_token": new_access}