from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def test():
    return 'hello world'
# https://youtu.be/9gpAtzQhYkY?si=z6PKradW4iYVhlCo&t=3897