from fastapi import FastAPI
from app.controllers.drop import router as drop_router

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Revival Clothing API is running"} 

app.include_router(drop_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)
