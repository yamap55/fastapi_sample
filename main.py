"""main"""
from logging import config

from fastapi import FastAPI

config.fileConfig("logging.conf", disable_existing_loggers=False)
app = FastAPI()

@app.get("/")
def main():
    print("Hello World!")
    return {"Hello": "World!"}
