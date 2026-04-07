from fastapi import FastAPI, Header, Depends

app = FastAPI()

def get_token():
    return "sample_token"

@app.get("/")
def read_data(user_agent: str = Header(None), token: str = Depends(get_token)):
    return {"user_agent": user_agent, "token": token}