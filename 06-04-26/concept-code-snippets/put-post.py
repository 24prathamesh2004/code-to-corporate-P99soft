@app.post("/create")
def create_item(item: dict):
    return {"created": item}

@app.put("/update/{id}")
def update_item(id: int, item: dict):
    return {"updated_id": id, "item": item}