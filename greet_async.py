from fastapi import FastAPI
import uvicorn
import asyncio 

app = FastAPI()

@app.get('/hi')
async def greet():
    await asyncio.sleep(5)
    return "Hello World"

if __name__ == "__main__":
    uvicorn.run("greet_async:app")