# source ./venv/bin/activate  - cambiar el entorno
# fastapi dev main.py - ejecutar 
# deactivate para - salir


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str


@app.post('/signup')
def signup_user(user: UserCreate):
    # extrac the data thats coming from rq
    print(user.name)
    print(user.email)
    print(user.password)
    # check if user already exists in db
    # add the user to the db
    pass
#https://youtu.be/9gpAtzQhYkY?si=TRwIiinQL8sSGnx1&t=5026