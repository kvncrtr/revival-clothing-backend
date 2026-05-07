from fastapi import FastAPI, Header, Response
from fastapi.encoders import jsonable_encoder

from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

# Different types of data sharing channels
# Data Sharing - Headers
@app.get('/auth')
def get_profile(authorization: str = Header()):
    return {
        'authorization_header': authorization
    }

# Data Sharing - URL String
@app.get('/users/{username}')
def get_username(username: str):
    return {
        'user': username
    }

# Data Sharing - Query Parameters
@app.get('/profile')
def get_query_params(query: str | None = None, city: str | None = None, limit: int = 10):
    return {
        'search_query': query,
        'city': city,
        'limit': limit
    }

# Data Sharing - Body Values
class UserCreate(BaseModel):
    username: str
    email: str
    number: str
    online: bool

class User(BaseModel):
    username: str
    email: str
    number: str
    online: bool
    card_number: int
    created_at: datetime

class UserOut(BaseModel):
    username: str
    email: str

@app.post('/users', response_model=UserOut)
def create_user(user: UserCreate):
    new_user = User(
        username=user.username,
        email=user.email,
        number=user.number,
        online=user.online,
        card_number=123456789,
        created_at=datetime.utcnow()
    )

    return new_user

# @app.get('/agent')
# def greet(user_agent:str =  Header(), status_code=200):
#     return user_agent, status_code

# @app.get('/header/{name}/{value}')
# def header(name: str, value: str, response: Response):
#     response.headers[name] = value
#     return 'normal body'

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)
