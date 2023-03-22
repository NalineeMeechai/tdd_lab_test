from fastapi import FastAPI
from mangum import Mangum
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World1"}

@app.get("/hello/{name}")
def read_name(name: str = None):
    return {"hello": name}

@app.get("/callname/{name}")
def read_name(name: str = None):
    return {"hello": {name}}

class Name(BaseModel):
    name: str

@app.post("/callname")
async def call_name(name: Name):
    return name

handler = Mangum(app)
