from fastapi import FastAPI
from .utils.db import MySQLDatabase
from time import sleep

## Configuration
# db = None

# def get_db():
#     global db
#     print(db)
#     if db is None:
#         raise Exception("Database not initialized.")
#     return db

def create_app(**kwargs):
    app = FastAPI()
    # app.db = create_db(**kwargs)
    # print(app.db.execute_query("SELECT NOW();"))
    return app


