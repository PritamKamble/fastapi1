from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
def read_root():
    file_path = os.path.join(os.path.dirname(__file__), "index.html")
    return FileResponse(file_path)

@app.get('/user')
def get_user():
    return {
        'name': 'Pritam',
        'age': 28,
        'contact': '7276279026'
    }

@app.post('/add')
def add_numbers():
    return {
        "total": 10
    }