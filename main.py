from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/drops/{num}', response_class=HTMLResponse)
def drop(num: int):
    return f'<h1>Drop collection you subscribed to: {num}</h1>'