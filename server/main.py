# source ./venv/bin/activate  - cambiar el entorno
# fastapi dev main.py - ejecutar 
# deactivate para - salir

from fastapi import HTTPException, FastAPI
from models.base import Base
from routes import auth 
from database import engine

app = FastAPI()

app.include_router(auth.router, prefix='/auth')

Base.metadata.create_all(engine)