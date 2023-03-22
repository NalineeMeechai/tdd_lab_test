from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "name"}


@app.get("/name/{name_id}")
def read_name(name_id: int, name: str = None):
    return {"name_id": name_id, "name": name}

@app.post("/hello/{name}")
def read_name(name: str = None):
    return {"hello": name}

@app.post("/")
def read_root():
    return {"hello": "name"}


@app.post("/name/{name_id}")
def read_name(name_id: int, name: str = None):
    return {"name_id": name_id, "name": name}

@app.post("/hello/{name}")
def read_name(name: str = None):
    return {"hello": name}

handler = Mangum(app)
