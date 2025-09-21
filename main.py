from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

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