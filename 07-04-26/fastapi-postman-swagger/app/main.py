from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# ROOT
@app.get("/")
def root():
    return {"message": "FastAPI CRUD with PostgreSQL"}

# CREATE (POST)
@app.post("/users", response_model=schemas.UserResponse)
def create(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

# GET ALL (Query Params)
@app.get("/users", response_model=list[schemas.UserResponse])
def read_users(
    skip: int = 0,
    limit: int = 10,
    min_age: int = None,
    db: Session = Depends(get_db)
):
    return crud.get_users(db, skip, limit, min_age)

# GET BY ID (Path Param)
@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# UPDATE (PUT)
@app.put("/users/{user_id}", response_model=schemas.UserResponse)
def update(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    updated = crud.update_user(db, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

# DELETE
@app.delete("/users/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}