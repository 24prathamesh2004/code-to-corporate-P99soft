@app.get("/user/{id}")
def get_user(id: int):
    return {"user_id": id}