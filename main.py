from fastapi import FastAPI, Header

app = FastAPI()

@app.get('/agent')
def greet(user_agent:str =  Header(), status_code=200):
    return user_agent, status_code

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)