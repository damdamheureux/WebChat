import mysql.connector
from starlette.responses import RedirectResponse
from fastapi.responses import JSONResponse
from fastapi import Form, Cookie, APIRouter, Body, Query
from typing import Annotated
import jwt
import time
from datetime import datetime
import os
from backend.utils.db import get_db_instance
router = APIRouter()
secret_key_router = os.getenv("PRIVATE_fastapi_token")
db = get_db_instance()
print("db from routers/auth is ", db)


@router.get("/login")
async def login(email: Annotated[str, Query()] = None, password: Annotated[str, Query()] = None, authtoken: Annotated[str | None, Cookie()] = None):
    try:
        if authtoken:
            return {"type": "error", "message": "Already logged in."}
    except:
        pass
    try:
        print(email, password)
        data = db.execute_query("SELECT id, email, verified FROM users WHERE email = %s AND password=%s", (email,password))
        print("query executed")
        row = data[0] if len(data) > 0 else None
        if row is None:
            return JSONResponse(content = {"type": "error", "message": "Invalid email or password.", "code": "ERR_AUTH_INVALIDCREDENTIALS"}, status_code=401)
        print("te")
        if row[2] == 0:
            return RedirectResponse("/nonverified")

        print("my row is", row)
        response = JSONResponse(content={"type": "success", "message": "Login success"})
        response.set_cookie(key="authtoken", value=jwt.encode({"user_id": row[0], "email": row[1]}, key=secret_key_router, algorithm="HS256"))
        return response
    except Exception as e:
        # In case the request fails ? (not supposed to be raised)
        return {"type": "error", "message": "An error occured.", "code": "ERR_UNK_UNKNOWN"}

@router.get("/register")
async def register(name: Annotated[str, Query()], firstname: Annotated[str, Query()], email: Annotated[str, Query()], password: Annotated[str, Query()]):
    try:
        InsertID = db.execute_query("INSERT INTO users (nom, prenom, email, password, verified) VALUES (%s, %s, %s, %s, %s)", (name, firstname, email, password, True))
        # tokenverifid = db.execute_query("INSERT INTO accverif (userid, token) VALUES (%s, %s) ", (InsertID, jwt.encode({"user_id": InsertID, "email": email, "timestamp": datetime.now().timestamp()}, key=secret_key_router, algorithm="HS256")))
        response = JSONResponse(content={"type": "success", "message": "Login success"})
        response.set_cookie(key="authtoken", value=jwt.encode({"user_id": InsertID, "email": email}, key=secret_key_router, algorithm="HS256"))
        return response
    except mysql.connector.Error as err:
        # Le compte existe déjà avec le même EMail
        if err.errno == mysql.connector.errorcode.ER_DUP_ENTRY:
            return {"type": "error", "message": "An account already exists for this email.", "code": "ERR_ACCOUNTCREATION_ALREADYEXISTS"}
        else:
            return {"type": "error", "message": "An internal error occured. Please, try again later.", "code": "ERR_UNK_UNKNOWN"}

@router.get("/account/verify")
async def verify_account(token: str = None):
    try:
        search = db.execute_query("SELECT userid FROM accverif WHERE token = %s", (token,))
        print(search)
        if len(search) > 0:
            db.execute_query("DELETE FROM accverif WHERE token = %s", (token,))
            db.execute_query("UPDATE users SET verified = 1 WHERE id = %s", (search[0][0],))
            return RedirectResponse("/")
        else:
            return {"type": "error", "message": "Token is invalid or expired."}
    except:
        return {"type": "error", "message": "An error occured."}