from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Hello Page</title>
        </head>
        <body>
            <h1>Hello World</h1>
            <p>Welcome to my FastAPI server 🚀</p>
        </body>
    </html>
    """

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