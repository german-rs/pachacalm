# source ./venv/bin/activate  - cambiar el entorno
# fastapi dev main.py - ejecutar 
# deactivate para - salir


from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import LargeBinary, VARCHAR, TEXT, Column, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid
import bcrypt

app = FastAPI()

DATABASE_URL = 'postgresql://postgres@localhost:5432/pachacalmapp';

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(TEXT, primary_key = True)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(LargeBinary)

@app.post('/signup')
def signup_user(user: UserCreate):
    # check if user already exists in db
    user_db = db.query(User).filter(User.email == user.email).first()

    if user_db:
        return 'User with the same email already exists!'

    hashed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    #https://youtu.be/9gpAtzQhYkY?si=Yx18qJ-SAKsBVglM&t=6635
    user_db = User(id=str(uuid.uuid4()), email=user.email, password=hashed_pw, name=user.name) 
    # add the user to the db
    db.add(user_db)
    db.commit()

    return user_db


Base.metadata.create_all(engine)